"""Shapes: each tree's frontmatter, declared once, and the checks that read it.

Shared by `sphere` and `structure-check`. Every path here is relative to the
sphere root: callers change into the root first.
Standard library only; runs on Python 3.9.
"""

import datetime
import fnmatch
import os
import re
import subprocess
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Optional

FOCUS = "layers/focus"
PERSONAS = "core/ai/personas"
OPERATING_MODES = "core/operating-modes"
ARCHIVE = "layers/focus/archived"
FOCUS_FOLDER_NAME = re.compile(r"^(f[0-9]+)-([a-z0-9]+(?:-[a-z0-9]+)*)$")
KEY_LINE = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*):")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


# ---------------------------------------------------------------- the declaration


@dataclass
class Tree:
    """One tree's shape, as declared in the shapes file."""

    name: str
    node_kind: str = ""  # "folder": each subfolder is a node; "file": each .md file is; "either": both
    folder: str = ""
    deep: bool = False  # file nodes at any depth, not only directly in the folder
    grouped: bool = False  # file nodes directly in the folder, or one level down in a group folder
    current_file: str = ""  # folder nodes: the file that carries the frontmatter; {name} is the folder's name
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

    def is_folder_node(self, node: str) -> bool:
        return self.node_kind == "folder" or (self.node_kind == "either" and os.path.isdir(node))

    def current_path(self, node: str) -> str:
        """The file that carries a node's frontmatter: the node itself, or its current file."""
        if not self.is_folder_node(node):
            return node
        return f"{node}/{self.current_file.replace('{name}', os.path.basename(node.rstrip('/')))}"


@dataclass
class Shapes:
    """The whole declaration: the trees, plus which files are history and which are reference."""

    trees: list[Tree]
    history_files: list[str]  # append-only, merged by union, never reversed: a file name, a folder/ or a pattern
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
        """A bare name matches the file's name anywhere; `dir/` everything under it; else a pattern (* ?)."""
        for entry in self.history_files:
            if entry.endswith("/"):
                if path.startswith(entry):
                    return True
            elif "/" in entry:
                if fnmatch.fnmatchcase(path, entry):
                    return True
            elif os.path.basename(path) == entry:
                return True
        return False

    def union_merge_lines(self) -> list[str]:
        """The .gitattributes lines for the history kinds, derived from `kind history` so the two can't drift."""
        return [
            f"{entry}** merge=union" if entry.endswith("/") else f"{entry} merge=union" for entry in self.history_files
        ]

    def is_reference(self, path: str) -> bool:
        """History wins: a history file inside a reference folder (a persona's journal) is history."""
        return not self.is_history(path) and any(path.startswith(prefix) for prefix in self.reference_prefixes)


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
        tree.deep = "deep" in rest[2:]
        tree.grouped = "grouped" in rest[2:]
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
            return "" if value.startswith("#") else re.sub(r"\s+#.*$", "", value).strip()
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
    path = tree.current_path(node)
    if tree.is_folder_node(node):
        if not os.path.isfile(path):
            return [Finding(node, f"missing {os.path.basename(path)} (current state)")]
        if tree.history_file and not os.path.isfile(f"{node}/{tree.history_file}"):
            findings.append(Finding(node, f"missing {tree.history_file} (history)"))
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
        if key not in tree.keys and key not in tree.optional_keys and key not in tree.archived_keys:
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
    if "until" in seen:  # an end date to how open it is; private has nothing to end
        sharing = frontmatter_value(path, "sharing")
        if frontmatter_value(path, "until") and sharing not in ("protected", "public"):
            findings.append(
                Finding(path, f"until only goes with sharing protected or public (sharing is {sharing or 'empty'})")
            )
    tree_rules = TREE_RULES.get(tree.name)
    if tree_rules:
        values = {key: frontmatter_value(path, key) for key in seen}
        facts = NodeFacts(tree, node, name, tree.is_archived(node), values, lines)
        findings += [Finding(path, problem) for problem in tree_rules(facts)]
    return findings


def node_name(tree: Tree, node: str) -> str:
    name = os.path.basename(node.rstrip("/"))
    return name[:-3] if not tree.is_folder_node(node) and name.endswith(".md") else name


def format_problem(value: str, rule: list[str], name: str) -> str:
    """What's wrong with a value under a `format` rule ("" when nothing). Kinds:
    name (the node's own name), date (YYYY-MM-DD), int (0 or more), version (<major>.<minor>),
    list [item-pattern], list+ [item-pattern] (at least one item), pattern <regex>."""
    kind, argument = rule[0], (rule[1] if len(rule) > 1 else "")
    if kind == "name" and value != name:
        return f"is '{value}', but the node is named '{name}'"
    if kind == "date" and not is_date(value):
        return f"is '{value}', expected a date (YYYY-MM-DD)"
    if kind == "int" and not value.isdigit():
        return f"is '{value}', expected a whole number (0 or more)"
    if kind == "version" and not re.match(r"^\d+\.\d+$", value):
        return f"is '{value}', expected <major>.<minor>"
    if kind == "pattern" and not re.match(argument, value):
        return f"is '{value}', expected to match {argument}"
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


@dataclass
class NodeFacts:
    """What a tree's own rules get to look at: one node's place and its frontmatter, never its body."""

    tree: Tree
    node: str
    name: str
    archived: bool
    values: dict[str, str]  # key → value, as frontmatter_value reads it
    lines: list[str]  # the raw frontmatter lines, for nested maps like an agent's trust


def idea_rules(facts: NodeFacts) -> list[str]:
    problems: list[str] = []
    name = facts.name
    captured = facts.values.get("captured", "")
    if re.match(r"^\d{8}", name) and captured and captured.replace("-", "") != name[:8]:
        problems.append(f"captured is '{captured}', but the name starts with {name[:8]}")
    stage, refinements = facts.values.get("stage", ""), facts.values.get("refinements", "")
    if stage == "raw" and refinements not in ("0", ""):
        problems.append(f"stage is raw, so refinements should be 0 (it's {refinements})")
    if refinements == "0" and stage not in ("raw", ""):
        problems.append(f"refinements is 0, so stage should be raw (it's {stage})")
    if refinements.isdigit() and int(refinements) > 0 and not facts.values.get("refined"):
        problems.append("refined once or more, so it needs 'refined' (the date of the last refinement)")
    outcome = facts.values.get("outcome", "").split(" ", 1)
    if outcome[0] == "graduated" and not re.match(r"^[a-z]+:\S+$", outcome[-1] if len(outcome) > 1 else ""):
        problems.append("outcome 'graduated' needs where it went: graduated <tree:name>")
    if outcome[0] == "parked" and len(outcome) < 2:
        problems.append("outcome 'parked' needs a reason: parked <reason>")
    return problems


def plan_rules(facts: NodeFacts) -> list[str]:
    problems: list[str] = []
    state = facts.values.get("state", "")
    if facts.archived and state not in ("done", "dropped", ""):
        problems.append(f"archived, so state should be done or dropped (it's {state})")
    if not facts.archived and state not in ("active", ""):
        problems.append(f"state is {state}, so it belongs in {facts.tree.archive}/")
    created, updated = facts.values.get("created", ""), facts.values.get("updated", "")
    if is_date(created) and is_date(updated) and updated < created:
        problems.append(f"updated ({updated}) is before created ({created})")
    parent = facts.values.get("parent", "")
    if parent == facts.name:
        problems.append("a plan isn't its own parent")
    elif parent and not any(os.path.isdir(f"{place}/{parent}") for place in (facts.tree.folder, facts.tree.archive)):
        problems.append(f"parent plan '{parent}' doesn't exist")
    return problems


TRUST_RUNGS = ("together", "supervised", "unattended")


def agent_rules(facts: NodeFacts) -> list[str]:
    """`trust:` is a map, one `  <kind of work>: <rung>` line each; an empty map is fine (everything at together)."""
    problems: list[str] = []
    if facts.values.get("trust", "") not in ("", "{}"):
        problems.append("trust is a map: one indented '<kind of work>: <rung>' line each")
    inside = False
    for line in facts.lines:
        if KEY_LINE.match(line):
            inside = line.startswith("trust:")
        elif inside and line.strip() and not line.strip().startswith("#"):
            kind, _, rung = line.strip().partition(":")
            rung = re.sub(r"\s+#.*$", "", rung).strip()
            if rung not in TRUST_RUNGS:
                problems.append(f"trust for '{kind}' is '{rung}', expected one of: {' '.join(TRUST_RUNGS)}")
    return problems


def operating_mode_rules(facts: NodeFacts) -> list[str]:
    persona = facts.values.get("persona", "")
    if persona and persona != "any" and not os.path.isdir(f"{PERSONAS}/{persona}"):
        return [f"persona '{persona}' doesn't exist (any, or a folder in {PERSONAS}/)"]
    return []


def persona_rules(facts: NodeFacts) -> list[str]:
    mode = facts.values.get("operating-mode", "")
    if mode and not os.path.isfile(f"{OPERATING_MODES}/{mode}.md"):
        return [f"operating-mode '{mode}' isn't a file in {OPERATING_MODES}/"]
    return []


def library_rules(facts: NodeFacts) -> list[str]:
    sharing, perspective = facts.values.get("sharing", ""), facts.values.get("perspective", "")
    if sharing in ("public", "protected") and perspective != "generic":
        perspective = perspective or "none"
        return [f"sharing is {sharing}, but only a generic artifact can be opened up (perspective: {perspective})"]
    return []


TREE_RULES: dict[str, Callable[[NodeFacts], list[str]]] = {
    "idea": idea_rules,
    "plan": plan_rules,
    "agent": agent_rules,
    "operating-mode": operating_mode_rules,
    "persona": persona_rules,
    "library": library_rules,
}


# ---------------------------------------------------------------- rules across a tree's nodes (frontmatter only)


def one_default_persona(tree: Tree, nodes: list[str]) -> list[Finding]:
    defaults = [node for node in nodes if frontmatter_value(tree.current_path(node), "default") == "true"]
    if nodes and len(defaults) != 1:
        found = " ".join(node_name(tree, node) for node in defaults) or "none"
        return [Finding(tree.folder, f"exactly one persona has default: true (found: {found})")]
    return []


def unique_names(tree: Tree, nodes: list[str]) -> list[Finding]:
    """Names are unique across the tree: group folders and the archive included (node-names)."""
    findings: list[Finding] = []
    first: dict[str, str] = {}
    for node in nodes:
        name = node_name(tree, node)
        if name in first:
            findings.append(Finding(node, f"name '{name}' is already used by {first[name]}"))
        else:
            first[name] = node
    return findings


TREE_SET_RULES: dict[str, Callable[[Tree, list[str]], list[Finding]]] = {
    "persona": one_default_persona,
}


def node_paths(tree: Tree, include_archive: bool = False) -> list[str]:
    """Every node of a tree: its subfolders, or its .md files. The archive (<dir>/archived) only when asked."""
    if not os.path.isdir(tree.folder):
        return []
    places = [tree.folder] + ([tree.archive] if include_archive else [])
    if tree.node_kind in ("folder", "either"):
        nodes: list[str] = []
        for parent in places:
            if not os.path.isdir(parent):
                continue
            for name in sorted(os.listdir(parent)):
                path = f"{parent}/{name}"
                if path == tree.archive or name in tree.skip:
                    continue
                if os.path.isdir(path) or (tree.node_kind == "either" and name.endswith(".md")):
                    nodes.append(path)
        return nodes
    files: list[str] = []
    for place in places:
        for folder, subfolders, names in os.walk(place):
            if not tree.deep and not (tree.grouped and folder == place):
                subfolders.clear()  # grouped: one level of group folders, no deeper
            subfolders[:] = [name for name in subfolders if name not in tree.skip]
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


def default_persona() -> str:
    """The persona with default: true ("" when there are none): one listing, one frontmatter each."""
    if not os.path.isdir(PERSONAS):
        return ""
    for name in sorted(os.listdir(PERSONAS)):
        if frontmatter_value(f"{PERSONAS}/{name}/{name}.md", "default") == "true":
            return name
    return ""


def persona_operating_mode(persona: str) -> str:
    """The operating mode a new focus starts in under this persona ("" when it names none)."""
    return frontmatter_value(f"{PERSONAS}/{persona}/{persona}.md", "operating-mode") if persona else ""


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


def check_sphere_files(shapes: Shapes) -> list[Finding]:
    """A sphere's repository lines: every history kind merges by union, and heartbeats are never committed."""
    if not os.path.isdir(FOCUS) or not is_git_top_level():
        return []
    findings: list[Finding] = []
    attributes = [" ".join(line.split()) for line in read_lines(".gitattributes")]
    for line in shapes.union_merge_lines():
        if line not in attributes:
            findings.append(Finding(".gitattributes", f"no union merge for {line.split()[0]} (add: {line})"))
    ignored = subprocess.run(["git", "check-ignore", "-q", "surface/state/focus/x.json"], capture_output=True)
    if ignored.returncode != 0:
        findings.append(Finding(".gitignore", "surface/state/ isn't ignored (heartbeats must never be committed)"))
    return findings


def check_everything(shapes: Shapes, include_archive: bool = False) -> list[Finding]:
    """Every live node of every tree (archived ones too, when asked), the focus tree, and the repository lines."""
    findings: list[Finding] = []
    for tree in shapes.trees:
        nodes = node_paths(tree, include_archive)
        for node in nodes:
            findings += check_node(tree, node)
        set_rules = TREE_SET_RULES.get(tree.name)
        if set_rules:
            findings += set_rules(tree, [node for node in nodes if os.path.isfile(tree.current_path(node))])
        # Names are never reused, so the archive is always listed for this one (folder listings only, still cheap).
        findings += unique_names(tree, node_paths(tree, include_archive=True))
    return findings + check_focus_tree(include_archive) + check_sphere_files(shapes)


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
