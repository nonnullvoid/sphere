"""Reading a sphere's lenses and frames: the manifest they build, and the reactions they hold.

Shared by `sphere` (which builds the manifest and prints reactions) and `manifest-check`
(which confirms them). Everything here is computed from the lens and frame files on disk,
so nothing it produces can disagree with them.
Standard library only; runs on Python 3.9.
"""

import glob
import hashlib
import os
import re
from dataclasses import dataclass
from typing import Optional

from sphere_shapes import frontmatter_value

REACTING_ROW = re.compile(r"^\| `([a-z][a-z0-9-]*)(?: ([a-z][a-z0-9-]*))?`(.*?)\| *(.*?) *\|\s*$")
APPLIES = re.compile(r"^\*\*Applies to:\*\* *(.+)$", re.M)
TITLE = re.compile(r"^# (.+)$", re.M)
MANIFEST = "core/manifest.md"
LINE_LIMIT = 140  # characters of a frame's Applies-to the manifest keeps
# The tools every sphere carries in scripts/: new-sphere ships them, update-sphere refreshes them.
TOOLS = [
    "sphere",
    "structure-check",
    "manifest-check",
    "sphere_shapes.py",
    "sphere_protocol.py",
    "sphere_views.py",
    "shapes",
]


@dataclass
class Reaction:
    sense: str
    tree: str  # "" reacts to the sense on every tree
    frame: str
    guard: str  # "" means always
    action: str
    path: str  # the frame, relative to the protocol folder


def section(text: str, heading: str) -> str:
    """The body of a `## heading` section, up to the next `## `; "" when absent."""
    match = re.search(rf"\n## {re.escape(heading)}\n(.*?)(?=\n## |\Z)", text, re.S)
    return match.group(1) if match else ""


def protocol_hash(protocol: str) -> str:
    """sha256 over every lens and frame file (path, then content), sorted by path; the first 12 hex digits."""
    digest = hashlib.sha256()
    paths = glob.glob(f"{protocol}/lenses/**/*", recursive=True) + glob.glob(f"{protocol}/frames/**/*", recursive=True)
    for path in sorted(p for p in paths if os.path.isfile(p)):
        digest.update(os.path.relpath(path, protocol).encode())
        with open(path, "rb") as handle:
            digest.update(handle.read())
    return digest.hexdigest()[:12]


def frame_paths(protocol: str) -> list[str]:
    return [p for p in sorted(glob.glob(f"{protocol}/frames/**/*.md", recursive=True)) if frontmatter_value(p, "frame")]


def lens_paths(protocol: str) -> list[str]:
    return [p for p in sorted(glob.glob(f"{protocol}/lenses/*.md")) if frontmatter_value(p, "lens")]


def read(path: str) -> str:
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def clean(text: str) -> str:
    """Markdown down to plain words: links to their text, emphasis and code marks dropped."""
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    return re.sub(r"[*_`]", "", text).strip()


def shorten(text: str) -> str:
    limit = LINE_LIMIT
    text = clean(text)
    first = re.split(r"(?<=[.!?])\s", text, maxsplit=1)[0].rstrip(".:")
    first = re.sub(r",? including$", "", first)  # a line that goes on as a list keeps only its lead
    if len(first) <= limit:
        return first
    cut = first[:limit].rsplit(" ", 1)[0].rstrip(",;:")
    return cut + "…"


def reactions(protocol: str) -> list[Reaction]:
    """Every When/do row that starts with a sense in backticks, in every frame."""
    found: list[Reaction] = []
    for path in frame_paths(protocol):
        name = frontmatter_value(path, "frame")
        for line in section(read(path), "When / do").splitlines():
            match = REACTING_ROW.match(line)
            if match:
                sense, tree, guard, action = match.groups()
                guard = clean(guard).lstrip(",").strip()
                found.append(Reaction(sense, tree or "", name, guard, clean(action), os.path.relpath(path, protocol)))
    return found


def reactions_to(protocol: str, sense: str, about: str = "") -> list[Reaction]:
    """The rows for one sense. `about` is a link (`knowledge:money.taxes`) or a tree (`knowledge`);
    rows written for that tree, and rows with no tree, both apply."""
    tree = about.split(":")[0] if about else ""
    return [r for r in reactions(protocol) if r.sense == sense and (not r.tree or r.tree == tree)]


def format_reactions(sense: str, rows: list[Reaction]) -> str:
    if not rows:
        return f"reactions: none for {sense}"
    lines = [f"reactions: {sense}"]
    for row in rows:
        when = row.guard or "always"
        lines.append(f"  {row.frame} ({when}): {row.action}")
    return "\n".join(lines)


def build_manifest(protocol: str, today: str) -> str:
    """The sphere's routing table: what it can do and when each thing applies, one line each.
    Loaded in every window, so it carries no mechanics: those stay in the frames."""
    always: list[str] = []
    by_folder: dict[str, list[str]] = {}
    for path in frame_paths(protocol):
        name = frontmatter_value(path, "frame")
        applies = APPLIES.search(read(path))
        line = f"- `{name}`: {shorten(applies.group(1)) if applies else '(no Applies to line)'}"
        folder = os.path.relpath(os.path.dirname(path), f"{protocol}/frames").split(os.sep)[0]
        by_folder.setdefault(folder, []).append(line)
        if frontmatter_value(path, "always") == "true":
            always.append(line)
    out = [
        "# Capability manifest",
        "",
        f"_Built {today} by `scripts/sphere manifest` from `core/protocol/`. Never edited by hand: improve a line"
        " by improving the frame's **Applies to:**, then rebuild._  ",
        f"Hash: {protocol_hash(protocol)}",
        "",
        "## Always on",
        "",
        "_Guards that hold in every window, for every persona and mode._",
        "",
        *always,
        "",
        "## Lenses",
        "",
        "_Why the sphere works the way it does. Read one when the why is in question: a judgment call, a change._",
        "",
    ]
    for path in lens_paths(protocol):
        title: Optional[re.Match[str]] = TITLE.search(read(path))
        name = frontmatter_value(path, "lens")
        out.append(f"- `{name}`: {clean(title.group(1)) if title else ''}")
    out += [
        "",
        "## Frames",
        "",
        "_How each thing is done. Open `core/protocol/frames/<folder>/<frame>.md` only when you're about to do it._",
    ]
    for folder in sorted(by_folder):
        out += ["", f"### {folder}", "", *by_folder[folder]]
    out += [
        "",
        "## Reactions",
        "",
        "_When a sense fires, `scripts/sphere reactions <sense> [link]` prints what to do. Open and attach print"
        " theirs already._",
        "",
    ]
    return "\n".join(out)
