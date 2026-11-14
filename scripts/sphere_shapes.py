"""Shapes: each tree's frontmatter, declared once, and the checks that read it.

Shared by `sphere` and `structure-check`. Every path here is relative to the
sphere root: callers change into the root first.
Standard library only; runs on Python 3.9.
"""

import datetime
import os
import re
import subprocess
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Optional

FOCUS = "layers/focus"
ARCHIVE = "layers/focus/archived"
FOCUS_FOLDER_NAME = re.compile(r"^(f[0-9]+)-([a-z0-9]+(?:-[a-z0-9]+)*)$")
KEY_LINE = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*):")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


# ---------------------------------------------------------------- the declaration


@dataclass
class Tree:
    """One tree's shape, as declared in the shapes file."""

    name: str
    node_kind: str = ""  # "folder": each subfolder is a node; "file": each .md file is
    folder: str = ""
    deep: bool = False  # file nodes at any depth, not only directly in the folder
    current_file: str = ""  # folder nodes: the file that carries the frontmatter
    history_file: str = ""  # folder nodes: the history file
    keys: list[str] = field(default_factory=list)
    optional_keys: list[str] = field(default_factory=list)
    key_order: list[str] = field(default_factory=list)  # from `keys`, optional ones included, in order
    archived_keys: list[str] = field(default_factory=list)  # keys a node has exactly when it's archived
    allowed_values: dict[str, list[str]] = field(default_factory=dict)
    formats: dict[str, list[str]] = field(default_factory=dict)  # key → [kind, argument...]
    name_pattern: str = ""  # node names (file name without .md, or folder name)
    skip: list[str] = field(default_factory=list)

    @property
    def archive(self) -> str:
        return f"{self.folder}/archived"

    def is_archived(self, node: str) -> bool:
        return node.startswith(self.archive + "/")


@dataclass
class Shapes:
    """The whole declaration: the trees, plus which files are history and which are reference."""

    trees: list[Tree]
    history_files: list[str]  # file names: append-only, merged by union, never reversed
    reference_prefixes: list[str]  # path prefixes: changed only on the human's yes

    def tree(self, name: str) -> Optional[Tree]:
        for tree in self.trees:
            if tree.name == name:
                return tree
        return None

    def tree_of(self, path: str) -> Optional[Tree]:
        """The tree whose folder holds this path; the most specific one when folders nest."""
        holding = [tree for tree in self.trees if path.startswith(tree.folder + "/")]
        return max(holding, key=lambda tree: len(tree.folder), default=None)

    def is_history(self, path: str) -> bool:
        return os.path.basename(path) in self.history_files

    def is_reference(self, path: str) -> bool:
        return any(path.startswith(prefix) for prefix in self.reference_prefixes)


def read_shapes(path: str) -> Shapes:
    """Read a shapes file. The format is described at the top of the file itself."""
    trees: list[Tree] = []
    history_files: list[str] = []
    reference_prefixes: list[str] = []
    with open(path, encoding="utf-8") as handle:
        for raw_line in handle:
            words = raw_line.split()
            if not words or words[0].startswith("#"):
                continue
            word, rest = words[0], words[1:]
            if word == "tree":
                trees.append(Tree(name=" ".join(rest)))
            elif word == "kind" and rest[:1] == ["history"]:
                history_files += rest[1:]
            elif word == "kind" and rest[:1] == ["reference"]:
                reference_prefixes += rest[1:]
            elif trees:
                apply_tree_line(trees[-1], word, rest)
    return Shapes(trees, history_files, reference_prefixes)


def apply_tree_line(tree: Tree, word: str, rest: list[str]) -> None:
    if word == "nodes":
        tree.node_kind, tree.folder = rest[0], rest[1]
        tree.deep = rest[2:3] == ["deep"]
    elif word == "current":
        tree.current_file = rest[0]
    elif word == "history":
        tree.history_file = rest[0]
    elif word == "keys":
        tree.key_order = [key.rstrip("?") for key in rest]
        tree.keys = [key for key in rest if not key.endswith("?")]
        tree.optional_keys += [key[:-1] for key in rest if key.endswith("?")]
    elif word == "optional":
        tree.optional_keys += rest
    elif word == "archived":
        tree.archived_keys = rest
    elif word == "values":
        tree.allowed_values[rest[0]] = rest[1:]
    elif word == "format":
        tree.formats[rest[0]] = rest[1:]
    elif word == "name":
        tree.name_pattern = rest[0]
    elif word == "skip":
        tree.skip = rest


# ---------------------------------------------------------------- frontmatter: one-line `key: value`


def read_frontmatter(path: str) -> tuple[list[str], str]:
    """The lines between the first two `---` lines, and a problem ("" when there is none)."""
    with open(path, encoding="utf-8") as handle:
        lines = handle.read().split("\n")
    if lines[0] != "---":
        return [], "no frontmatter"
    for index in range(1, len(lines)):
        if lines[index] == "---":
            body = lines[1:index]
            return (body, "") if body else ([], "no frontmatter")
    return [], "frontmatter isn't closed with ---"


def frontmatter_value(path: str, key: str) -> str:
    """The value of `key`, with any trailing `# comment` removed; "" when absent."""
    try:
        lines, _ = read_frontmatter(path)
    except OSError:
        return ""
    for line in lines:
        if line.startswith(key + ":"):
            value = line[len(key) + 1 :].strip()
            return re.sub(r"\s+#.*$", "", value).strip()
    return ""


def set_frontmatter_value(path: str, key: str, value: str) -> None:
    """Rewrite the `key:` line inside the frontmatter. Everything else stays as it was."""
    with open(path, encoding="utf-8") as handle:
        lines = handle.read().split("\n")
    for index in range(1, len(lines)):
        if lines[index] == "---":
            break
        if lines[index].startswith(key + ":"):
            lines[index] = f"{key}: {value}".rstrip()
            break
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines))


def parse_list(value: str) -> list[str]:
    """`[a, b]` or `a,b` → ["a", "b"]."""
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        value = value[1:-1]
    return [item.strip() for item in value.split(",") if item.strip()]


def format_list(items: list[str]) -> str:
    return "[" + ", ".join(items) + "]"


# ---------------------------------------------------------------- checks: they report, never fix


@dataclass
class Finding:
    where: str
    problem: str

    def __str__(self) -> str:
        return f"{self.where}: {self.problem}"


def check_node(tree: Tree, node: str) -> list[Finding]:
    """One node against its tree's shape: its files exist and its frontmatter has exactly the tree's keys."""
    findings: list[Finding] = []
    if tree.node_kind == "folder":
        path = f"{node}/{tree.current_file}"
        if not os.path.isfile(path):
            return [Finding(node, f"missing {tree.current_file} (current state)")]
        if tree.history_file and not os.path.isfile(f"{node}/{tree.history_file}"):
            findings.append(Finding(node, f"missing {tree.history_file} (history)"))
    else:
        path = node
    lines, problem = read_frontmatter(path)
    if problem:
        return findings + [Finding(path, problem)]

    seen: list[str] = []
    for line in lines:
        match = KEY_LINE.match(line)
        if not match:
            continue
        key = match.group(1)
        if key in seen:
            findings.append(Finding(path, f"key '{key}' appears twice"))
        seen.append(key)
        if key not in tree.keys and key not in tree.optional_keys:
            findings.append(Finding(path, f"key '{key}' isn't in the {tree.name} shape"))
    for key in tree.keys:
        if key not in seen:
            findings.append(Finding(path, f"missing key '{key}'"))
    ordered = [key for key in seen if key in tree.key_order]
    if ordered != sorted(ordered, key=tree.key_order.index):
        order = " ".join(tree.key_order)
        findings.append(Finding(path, f"keys out of order; the {tree.name} shape's order is: {order}"))
    archived = tree.is_archived(node)
    for key in tree.archived_keys:
        if archived and key not in seen:
            findings.append(Finding(path, f"archived, so it needs '{key}'"))
        if not archived and key in seen:
            findings.append(Finding(path, f"'{key}' belongs only to archived nodes"))
    for key, allowed in tree.allowed_values.items():
        if key not in seen:
            continue
        value = frontmatter_value(path, key)
        first_word = value.split(" ")[0]
        if first_word not in allowed:
            findings.append(Finding(path, f"{key} is '{value}', expected one of: {' '.join(allowed)}"))
    name = node_name(tree, node)
    if tree.name_pattern and not re.match(tree.name_pattern, name):
        findings.append(Finding(path, f"name '{name}' doesn't match {tree.name_pattern}"))
    for key, rule in tree.formats.items():
        value = frontmatter_value(path, key)
        if key in seen and (value or key not in tree.optional_keys):  # an optional key may be left empty
            problem = format_problem(value, rule, name)
            if problem:
                findings.append(Finding(path, f"{key} {problem}"))
    tree_rules = TREE_RULES.get(tree.name)
    if tree_rules:
        values = {key: frontmatter_value(path, key) for key in seen}
        findings += [Finding(path, problem) for problem in tree_rules(tree, node, values)]
    return findings


def node_name(tree: Tree, node: str) -> str:
    name = os.path.basename(node.rstrip("/"))
    return name[:-3] if tree.node_kind == "file" and name.endswith(".md") else name


def format_problem(value: str, rule: list[str], name: str) -> str:
    """What's wrong with a value under a `format` rule ("" when nothing). Kinds:
    name (the node's own name), date (YYYY-MM-DD), int (0 or more), version (<major>.<minor>),
    list [item-pattern], list+ [item-pattern] (at least one item)."""
    kind, argument = rule[0], (rule[1] if len(rule) > 1 else "")
    if kind == "name" and value != name:
        return f"is '{value}', but the node is named '{name}'"
    if kind == "date" and not is_date(value):
        return f"is '{value}', expected a date (YYYY-MM-DD)"
    if kind == "int" and not value.isdigit():
        return f"is '{value}', expected a whole number (0 or more)"
    if kind == "version" and not re.match(r"^\d+\.\d+$", value):
        return f"is '{value}', expected <major>.<minor>"
    if kind in ("list", "list+"):
        items = parse_list(value)
        if kind == "list+" and not items:
            return "needs at least one item"
        wrong = [item for item in items if argument and not re.match(argument, item)]
        if wrong:
            return f"has items that don't match {argument}: {' '.join(wrong)}"
    return ""


def is_date(value: str) -> bool:
    if not DATE.match(value):
        return False
    try:
        datetime.date.fromisoformat(value)
    except ValueError:
        return False
    return True


# ---------------------------------------------------------------- rules a tree has beyond its declared shape
# Frontmatter only: these never read a node's body, so the check stays cheap.


def idea_rules(tree: Tree, node: str, values: dict[str, str]) -> list[str]:
    problems: list[str] = []
    name = node_name(tree, node)
    captured = values.get("captured", "")
    if re.match(r"^\d{8}", name) and captured and captured.replace("-", "") != name[:8]:
        problems.append(f"captured is '{captured}', but the name starts with {name[:8]}")
    stage, refinements = values.get("stage", ""), values.get("refinements", "")
    if stage == "raw" and refinements not in ("0", ""):
        problems.append(f"stage is raw, so refinements should be 0 (it's {refinements})")
    if refinements == "0" and stage not in ("raw", ""):
        problems.append(f"refinements is 0, so stage should be raw (it's {stage})")
    if refinements.isdigit() and int(refinements) > 0 and not values.get("refined"):
        problems.append("refined once or more, so it needs 'refined' (the date of the last refinement)")
    outcome = values.get("outcome", "").split(" ", 1)
    if outcome[0] == "graduated" and not re.match(r"^[a-z]+:\S+$", outcome[-1] if len(outcome) > 1 else ""):
        problems.append("outcome 'graduated' needs where it went: graduated <tree:name>")
    if outcome[0] == "parked" and len(outcome) < 2:
        problems.append("outcome 'parked' needs a reason: parked <reason>")
    return problems


def plan_rules(tree: Tree, node: str, values: dict[str, str]) -> list[str]:
    problems: list[str] = []
    state = values.get("state", "")
    if tree.is_archived(node) and state not in ("done", "dropped", ""):
        problems.append(f"archived, so state should be done or dropped (it's {state})")
    if not tree.is_archived(node) and state not in ("active", ""):
        problems.append(f"state is {state}, so it belongs in {tree.archive}/")
    created, updated = values.get("created", ""), values.get("updated", "")
    if is_date(created) and is_date(updated) and updated < created:
        problems.append(f"updated ({updated}) is before created ({created})")
    parent = values.get("parent", "")
    if parent == node_name(tree, node):
        problems.append("a plan isn't its own parent")
    elif parent and not any(os.path.isdir(f"{place}/{parent}") for place in (tree.folder, tree.archive)):
        problems.append(f"parent plan '{parent}' doesn't exist")
    return problems


TREE_RULES: dict[str, Callable[[Tree, str, dict[str, str]], list[str]]] = {
    "idea": idea_rules,
    "plan": plan_rules,
}


def node_paths(tree: Tree, include_archive: bool = False) -> list[str]:
    """Every node of a tree: its subfolders, or its .md files. The archive (<dir>/archived) only when asked."""
    if not os.path.isdir(tree.folder):
        return []
    places = [tree.folder] + ([tree.archive] if include_archive else [])
    if tree.node_kind == "folder":
        nodes: list[str] = []
        for parent in places:
            if not os.path.isdir(parent):
                continue
            for name in sorted(os.listdir(parent)):
                path = f"{parent}/{name}"
                if os.path.isdir(path) and path != tree.archive and name not in tree.skip:
                    nodes.append(path)
        return nodes
    files: list[str] = []
    for place in places:
        for folder, subfolders, names in os.walk(place):
            if not tree.deep:
                subfolders.clear()
            if folder == tree.folder and "archived" in subfolders:
                subfolders.remove("archived")  # walked on its own, when asked
            for name in names:
                if name.endswith(".md") and name not in tree.skip:
                    files.append(f"{folder}/{name}")
    return sorted(files)


def check_focus_tree(include_archive: bool = False) -> list[Finding]:
    """The focus tree's own rules: folder names, unique numbers, parents, and status by place."""
    if not os.path.isdir(FOCUS):
        return []
    findings: list[Finding] = []
    if not os.path.isfile(f"{FOCUS}/f0-main/focus.md"):
        findings.append(Finding(FOCUS, "no f0-main (the root focus)"))
    folders = focus_folders(include_archive)
    all_numbers = [frontmatter_value(f"{d}/focus.md", "number") for d in folders]
    numbers_seen: list[str] = []
    for folder in folders:
        match = FOCUS_FOLDER_NAME.match(os.path.basename(folder))
        if not match:
            findings.append(Finding(folder, "folder isn't named f<number>-<name>"))
            continue
        focus_file = f"{folder}/focus.md"
        if not os.path.isfile(focus_file):
            continue
        number = frontmatter_value(focus_file, "number")
        name = frontmatter_value(focus_file, "name")
        parent = frontmatter_value(focus_file, "parent")
        status = frontmatter_value(focus_file, "status")
        archived = folder.startswith(ARCHIVE + "/")
        if number != match.group(1):
            findings.append(Finding(folder, f"number '{number}' doesn't match the folder"))
        if name != match.group(2):
            findings.append(Finding(folder, f"name '{name}' doesn't match the folder"))
        if number in numbers_seen:
            findings.append(Finding(folder, f"number {number} is used twice"))
        numbers_seen.append(number)
        if number == "f0":
            if parent:
                findings.append(Finding(folder, "main has no parent"))
            if archived:
                findings.append(Finding(folder, "main is never archived"))
        elif not parent:
            findings.append(Finding(folder, "no parent (top-level foci have parent: f0)"))
        elif parent not in all_numbers and (include_archive or not archived_focus_exists(parent)):
            findings.append(Finding(folder, f"parent {parent} doesn't exist"))
        if archived and status not in ("closed", ""):
            findings.append(Finding(folder, f"archived but status is '{status}'"))
        if not archived and status == "closed":
            findings.append(Finding(folder, "closed but not moved to archived/"))
    return findings


def archived_focus_exists(number: str) -> bool:
    """Whether archived/ has a folder for this number: one folder listing, no files read."""
    return os.path.isdir(ARCHIVE) and any(name.startswith(number + "-") for name in os.listdir(ARCHIVE))


def focus_folders(include_archive: bool = False) -> list[str]:
    folders: list[str] = []
    for parent in (FOCUS, ARCHIVE) if include_archive else (FOCUS,):
        if os.path.isdir(parent):
            for name in sorted(os.listdir(parent)):
                path = f"{parent}/{name}"
                if os.path.isdir(path) and path != ARCHIVE:
                    folders.append(path)
    return folders


def check_sphere_files() -> list[Finding]:
    """A sphere's repository lines: history merges by union, and heartbeats are never committed."""
    if not os.path.isdir(FOCUS) or not is_git_top_level():
        return []
    findings: list[Finding] = []
    attributes = read_lines(".gitattributes")
    for name in ("history.md", "progress.md"):
        if not any(re.match(rf"^{re.escape(name)}\s+merge=union", line) for line in attributes):
            findings.append(Finding(".gitattributes", f"no union merge for {name}"))
    ignored = subprocess.run(["git", "check-ignore", "-q", "surface/state/focus/x.json"], capture_output=True)
    if ignored.returncode != 0:
        findings.append(Finding(".gitignore", "surface/state/ isn't ignored (heartbeats must never be committed)"))
    return findings


def check_everything(shapes: Shapes, include_archive: bool = False) -> list[Finding]:
    """Every live node of every tree (archived ones too, when asked), the focus tree, and the repository lines."""
    findings: list[Finding] = []
    for tree in shapes.trees:
        for node in node_paths(tree, include_archive):
            findings += check_node(tree, node)
    return findings + check_focus_tree(include_archive) + check_sphere_files()


# ---------------------------------------------------------------- small helpers


def is_git_top_level() -> bool:
    result = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    return result.returncode == 0 and os.path.realpath(result.stdout.strip()) == os.path.realpath(".")


def read_lines(path: str) -> list[str]:
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read().split("\n")
    except OSError:
        return []
