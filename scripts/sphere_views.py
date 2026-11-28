"""Generated files a sphere declares: tree indexes and dashboard views.

Nothing here knows what any one sphere shows. A tree declares an index in core/shapes
(`index <file> <key> <key>…`); a projection declares its panels in its definition's
Panels table, one rule per row. This module only follows those declarations, so a sphere
changes what it shows by editing text, never code. A view with a panel that has no rule
is left to the AI, which renders it with judgment.
Standard library only; runs on Python 3.9.
"""

import datetime
import glob
import json
import os
import re
from dataclasses import dataclass
from typing import Optional

from sphere_shapes import Shapes, Tree, frontmatter_value, node_name, node_paths, parse_list, read_frontmatter

FOCUS = "layers/focus"
MAIN = "f0-main"
PROJECTIONS = "layers/projections"
MIRROR = "surface/projections/assets/registry.js"

Record = dict[str, str]


# ---------------------------------------------------------------- records: what rules read


def frontmatter_dict(path: str) -> Record:
    lines, _ = read_frontmatter(path)
    record: Record = {}
    for line in lines:
        key, sep, value = line.partition(":")
        if sep and not line.startswith(" "):
            record[key.strip()] = value.split("  #")[0].strip()
    return record


def tree_records(tree: Tree, include_archive: bool = False) -> list[Record]:
    records: list[Record] = []
    for node in node_paths(tree, include_archive):
        path = tree.current_path(node)
        if not os.path.isfile(path):
            continue
        record = frontmatter_dict(path)
        record["name"] = node_name(tree, node)
        record["archived"] = "yes" if tree.is_archived(node) else "no"
        records.append(record)
    return records


def section_first_line(text: str, heading: str) -> str:
    match = re.search(rf"^## {re.escape(heading)}\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    lines = [line.strip() for line in (match.group(1) if match else "").split("\n") if line.strip()]
    return lines[0] if lines else ""


def focus_records() -> list[Record]:
    """Open foci other than main: their name, intention, Now, latest Next, and whether one is waiting on the human."""
    records: list[Record] = []
    for folder in sorted(glob.glob(f"{FOCUS}/f*-*")):
        if os.path.basename(folder) == MAIN or not os.path.isfile(f"{folder}/focus.md"):
            continue
        record = frontmatter_dict(f"{folder}/focus.md")
        with open(f"{folder}/focus.md", encoding="utf-8") as handle:
            record["now"] = section_first_line(handle.read(), "Now")
        history = f"{folder}/history.md"
        latest = ""
        if os.path.isfile(history):
            with open(history, encoding="utf-8") as handle:
                text = handle.read()
            starts = [m.start() for m in re.finditer(r"^## \d{4}-\d{2}-\d{2}", text, re.M)]
            latest = text[starts[0] : starts[1] if len(starts) > 1 else len(text)] if starts else ""
        found = re.search(r"^\*\*Next:\*\* *(.+)$", latest, re.M)
        record["next"] = found.group(1).strip() if found else ""
        record["waiting"] = "yes" if "waiting on you" in latest.lower() else "no"
        records.append(record)
    return records


WITNESS = "layers/witness/ledger"


def witness_records() -> list[Record]:
    """The growth ledger's entries (`### <date> · <lane>`, then what happened): date as `updated`, lane, title."""
    records: list[Record] = []
    for path in sorted(glob.glob(f"{WITNESS}/*.md"), reverse=True):
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        for match in re.finditer(r"^### (\d{4}-\d{2}-\d{2}) · (.+)\n((?:(?!### ).*\n?)*)", text, re.M):
            body = [line.strip() for line in match.group(3).split("\n") if line.strip()]
            what = next((line for line in body if not re.match(r"^(by|evidence):", line)), "")
            records.append({"updated": match.group(1), "lane": match.group(2).strip(), "title": what})
    return records


def records_for(source: str, shapes: Shapes) -> list[Record]:
    """`foci`, `witness` (the growth ledger), or a tree's name from core/shapes (`<tree>+archived`: with archive)."""
    if source == "foci":
        return focus_records()
    if source == "witness":
        return witness_records()
    name, _, extra = source.partition("+")
    tree = next((tree for tree in shapes.trees if tree.name == name), None)
    if tree is None:
        raise ValueError(f"no tree or source called '{name}'")
    return tree_records(tree, include_archive=extra == "archived")


# ---------------------------------------------------------------- rules


@dataclass
class Condition:
    key: str
    op: str  # "=", "!=", ">=" (days), "has"
    values: list[str]

    def holds(self, record: Record, today: datetime.date) -> bool:
        value = record.get(self.key, "")
        if self.op == "has":
            return bool(value)
        if self.op == ">=":  # updated>=7d: within the last N days
            try:
                return (today - datetime.date.fromisoformat(value[:10])).days < int(self.values[0].rstrip("d"))
            except ValueError:
                return False
        return (value in self.values) == (self.op == "=")


def parse_conditions(text: str) -> list[Condition]:
    conditions: list[Condition] = []
    for part in [p.strip() for p in text.split(" and ") if p.strip()]:
        match = re.match(r"^([a-z_-]+)\s*(!=|>=|=)\s*(.+)$", part)
        if match:
            conditions.append(Condition(match.group(1), match.group(2), match.group(3).split("|")))
        else:
            conditions.append(Condition(part, "has", []))
    return conditions


def select(source: str, where: str, shapes: Shapes, today: datetime.date) -> list[Record]:
    conditions = parse_conditions(where)
    return [record for record in records_for(source, shapes) if all(c.holds(record, today) for c in conditions)]


LIST_RULE = re.compile(
    r"^list (?P<source>\S+)(?: where (?P<where>.+?))?(?: order (?P<order>\S+)(?P<desc> desc)?)?"
    r"(?: limit (?P<limit>\d+))? show (?P<show>[^\"]+?)(?: empty \"(?P<empty>[^\"]*)\")?$"
)
COUNT_PART = re.compile(r"^count (?P<source>\S+)(?: where (?P<where>.+?))? as (?P<label>.+)$")


def run_rule(rule: str, shapes: Shapes, today: datetime.date) -> tuple[str, list[dict[str, object]], str]:
    """A panel's rule → (kind, items, empty text). Raises ValueError for a rule it can't read."""
    rule = rule.strip()
    if rule.startswith("list "):
        match = LIST_RULE.match(rule)
        if not match:
            raise ValueError(f"can't read this list rule: {rule}")
        rows = select(match["source"], match["where"] or "", shapes, today)
        if match["order"]:
            rows.sort(key=lambda r: r.get(match["order"], ""), reverse=bool(match["desc"]))
        if match["limit"]:
            rows = rows[: int(match["limit"])]
        fields = [f.strip() for f in match["show"].split(",")]
        items: list[dict[str, object]] = []
        for row in rows:
            item: dict[str, object] = {"text": row.get(fields[0], "") or row.get("name", "")}
            meta = " · ".join(row.get(f, "") for f in fields[1:] if row.get(f, ""))
            if meta:
                item["meta"] = meta
            items.append(item)
        return "list", items, match["empty"] or ""
    if rule.startswith("count "):
        empty = ""
        found = re.search(r' empty "([^"]*)"$', rule)
        if found:
            empty, rule = found.group(1), rule[: found.start()]
        counts: list[dict[str, object]] = []
        for part in rule.split(";"):
            match = COUNT_PART.match(part.strip())
            if not match:
                raise ValueError(f"can't read this count: {part.strip()}")
            counts.append(
                {
                    "label": match["label"].strip(),
                    "value": len(select(match["source"], match["where"] or "", shapes, today)),
                }
            )
        nothing = all(item["value"] == 0 for item in counts)
        return "stats", [] if nothing else counts, empty
    raise ValueError(f"a rule starts with list or count: {rule}")


# ---------------------------------------------------------------- views


def panel_rules(definition: str) -> Optional[list[tuple[str, str]]]:
    """(title, rule) for each Panels row; None when any row has no rule (the AI renders that view)."""
    with open(definition, encoding="utf-8") as handle:
        text = handle.read()
    match = re.search(r"^## Panels\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not match:
        return None
    header: list[str] = []
    rows: list[tuple[str, str]] = []
    for line in match.group(1).split("\n"):
        if not line.startswith("|") or set(line) <= set("|- "):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not header:
            header = [cell.lower() for cell in cells]
            continue
        if "rule" not in header:
            return None
        rule = cells[header.index("rule")].strip("` ") if len(cells) > header.index("rule") else ""
        if not rule:
            return None
        rows.append((re.sub(r"[*_]", "", cells[0]), rule))
    return rows or None


def js(value: object) -> str:
    return json.dumps(value, ensure_ascii=False)


def view_data(definition: str, shapes: Shapes, now: datetime.datetime) -> Optional[str]:
    rules = panel_rules(definition)
    if rules is None:
        return None
    sources = parse_list(frontmatter_value(definition, "sources"))
    lines = [
        "// Derived view data, rendered by `scripts/sphere render` from the rules in its definition.",
        "// Rewritten at every render; never edited by hand.",
        "window.VIEW_DATA = {",
        f"  title: {js(frontmatter_value(definition, 'title'))},",
        f"  subtitle: {js(frontmatter_value(definition, 'subtitle'))},",
        f"  generated: {js(now.strftime('%Y-%m-%dT%H:%M:%S'))},",
        f"  sources: {js(sources)},",
        "  panels: [",
    ]
    for title, rule in rules:
        kind, items, empty = run_rule(rule, shapes, now.date())
        lines.append(f"    {{ title: {js(title)}, kind: {js(kind)}, items: {js(items)}, empty: {js(empty)} }},")
    lines += ["  ],", "};", ""]
    return "\n".join(lines)


def without_time(text: str) -> str:
    return re.sub(r'^  generated: ".*",$', "", text, flags=re.M)


def stamp_mirror(name: str, now: datetime.datetime) -> None:
    if not os.path.isfile(MIRROR):
        return
    with open(MIRROR, encoding="utf-8") as handle:
        text = handle.read()
    pattern = re.compile(rf'(\{{ name: "{re.escape(name)}",.*?rendered: )"[^"]*"')
    updated = pattern.sub(rf'\g<1>"{now.strftime("%Y-%m-%dT%H:%M:%S")}"', text)
    if updated != text:
        with open(MIRROR, "w", encoding="utf-8") as handle:
            handle.write(updated)


# ---------------------------------------------------------------- indexes


def build_index(tree: Tree) -> str:
    """A tree's declared index: its nodes as a tree (by `parent`), one line each, then the archive."""
    records = tree_records(tree, include_archive=True)
    live = [r for r in records if r["archived"] == "no"]
    names = {r["name"] for r in live}
    children: dict[str, list[Record]] = {}
    for record in live:
        parent = record.get("parent", "")
        children.setdefault(parent if parent in names else "", []).append(record)

    def line(record: Record, depth: int) -> list[str]:
        shown = " · ".join(record.get(key, "") for key in tree.index_show if record.get(key, ""))
        title = record.get("title", "") or record["name"]
        out = [f"{'  ' * depth}- **{title}** `[{record['name']}]`" + (f" · {shown}" if shown else "")]
        for child in sorted(children.get(record["name"], []), key=lambda r: r["name"]):
            out += line(child, depth + 1)
        return out

    out = [
        f"# {tree.name.capitalize()}",
        "",
        "_Built by `scripts/sphere render` from each node's frontmatter, at every ground that changed one."
        " Never edited by hand: if it disagrees with the nodes, the nodes win._",
        "",
    ]
    tops = sorted(children.get("", []), key=lambda r: r["name"])
    for record in tops:
        out += line(record, 0)
    if not tops:
        out.append("_Nothing yet._")
    archived = sorted((r for r in records if r["archived"] == "yes"), key=lambda r: r["name"])
    if archived:
        out += ["", "## Archived", ""]
        out += [
            f"- {r.get('title', '') or r['name']} `[{r['name']}]` · {r.get('state', '')}".rstrip(" ·") for r in archived
        ]
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- rendering everything declared


def write_if_changed(path: str, text: str, compare: bool = True) -> bool:
    old = ""
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as handle:
            old = handle.read()
    if compare and without_time(old) == without_time(text):
        return False
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return True


def render_all(shapes: Shapes, now: Optional[datetime.datetime] = None) -> tuple[list[str], list[str]]:
    """Rebuild every declared index and every view whose panels all have rules.
    Returns (files that changed, views left to the AI). A file is rewritten only when its content changed."""
    now = now or datetime.datetime.now()
    changed: list[str] = []
    for tree in shapes.trees:
        if tree.index_file and os.path.isdir(tree.folder) and write_if_changed(tree.index_file, build_index(tree)):
            changed.append(tree.index_file)
    left: list[str] = []
    for definition in sorted(glob.glob(f"{PROJECTIONS}/*.md")):
        name = frontmatter_value(definition, "projection")
        home = frontmatter_value(definition, "home")
        if not name or not home or frontmatter_value(definition, "template") != "dashboard":
            continue
        data = view_data(definition, shapes, now)
        if data is None:
            left.append(name)
            continue
        target = os.path.join(home, "data.js")
        if write_if_changed(target, data):
            changed.append(target)
            stamp_mirror(name, now)
            if MIRROR not in changed:
                changed.append(MIRROR)
    return changed, left
