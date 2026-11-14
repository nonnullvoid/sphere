"""Shared helpers for the sphere tests: each test gets a throwaway sphere in a temp folder.

Run the suite with: python3 -m unittest discover scripts/tests
Lint and type-check (dev-time only, the tools stay stdlib): uvx ruff check scripts;
uvx ruff format --check scripts; uvx basedpyright -p scripts
"""

import datetime
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from dataclasses import dataclass
from typing import Optional

SCRIPTS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPHERE = os.path.join(SCRIPTS, "sphere")
STRUCTURE_CHECK = os.path.join(SCRIPTS, "structure-check")
SHAPES_TEMPLATE = os.path.join(SCRIPTS, "shapes")
REPO = os.path.dirname(SCRIPTS)


@dataclass
class Result:
    code: int
    out: str
    err: str

    @property
    def text(self) -> str:
        return self.out + self.err


def run(args: list[str], cwd: str, env: Optional[dict[str, str]] = None, input: Optional[str] = None) -> Result:
    full_env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    for key in ("SPHERE_FOCUS", "SPHERE_CLIENT", "SPHERE_ROOT", "SPHERE_NO_GIT"):
        full_env.pop(key, None)
    full_env.update(env or {})
    done = subprocess.run(
        args, cwd=cwd, env=full_env, capture_output=True, text=True, input=input if input is not None else ""
    )
    return Result(done.returncode, done.stdout, done.stderr)


class SphereCase(unittest.TestCase):
    """A fresh sphere with git and a bare remote (so pull and push run), made by `sphere init`."""

    use_git: bool = True
    base: str  # pyright: ignore[reportUninitializedInstanceVariable]  # set in setUp, the unittest way
    root: str  # pyright: ignore[reportUninitializedInstanceVariable]  # set in setUp, the unittest way

    def setUp(self):
        self.base = tempfile.mkdtemp(prefix="sphere-test-")
        self.root = os.path.join(self.base, "sphere")
        os.makedirs(self.root)
        if self.use_git:
            self.git("init", "-q", "-b", "main")
            self.git("config", "user.email", "test@example.com")
            self.git("config", "user.name", "Test")
            self.git("init", "-q", "--bare", os.path.join(self.base, "remote"), cwd=self.base)
            self.git("remote", "add", "origin", os.path.join(self.base, "remote"))
        self.ok("init")
        if self.use_git:
            self.git("push", "-q", "-u", "origin", "main")

    def tearDown(self):
        shutil.rmtree(self.base, ignore_errors=True)

    # ---- running things

    def sphere(
        self,
        *args: str,
        focus: Optional[str] = None,
        client: Optional[str] = None,
        env: Optional[dict[str, str]] = None,
    ) -> Result:
        extra = dict(env or {})
        if focus:
            extra["SPHERE_FOCUS"] = focus
        if client:
            extra["SPHERE_CLIENT"] = client
        return run([sys.executable, SPHERE] + list(args), self.root, extra)

    def ok(
        self,
        *args: str,
        focus: Optional[str] = None,
        client: Optional[str] = None,
        env: Optional[dict[str, str]] = None,
    ) -> Result:
        result = self.sphere(*args, focus=focus, client=client, env=env)
        self.assertEqual(result.code, 0, f"sphere {' '.join(args)} failed:\n{result.text}")
        return result

    def check(self, *args: str, root: Optional[str] = None) -> Result:
        return run([sys.executable, STRUCTURE_CHECK, "--root", root or self.root] + list(args), self.root)

    def git(self, *args: str, cwd: Optional[str] = None) -> str:
        done = subprocess.run(["git"] + list(args), cwd=cwd or self.root, capture_output=True, text=True)
        self.assertEqual(done.returncode, 0, f"git {' '.join(args)}: {done.stderr}")
        return done.stdout.strip()

    # ---- files

    def path(self, relative: str) -> str:
        return os.path.join(self.root, relative)

    def read(self, relative: str) -> str:
        with open(self.path(relative), encoding="utf-8") as handle:
            return handle.read()

    def write(self, relative: str, text: str) -> None:
        os.makedirs(os.path.dirname(self.path(relative)), exist_ok=True)
        with open(self.path(relative), "w", encoding="utf-8") as handle:
            handle.write(text)

    def append(self, relative: str, text: str) -> None:
        self.write(relative, (self.read(relative) if os.path.exists(self.path(relative)) else "") + text)

    def exists(self, relative: str) -> bool:
        return os.path.exists(self.path(relative))

    def entry(self, ref: str, did: str, next_step: str = "Keep going.", date: Optional[str] = None) -> None:
        """What the AI writes before a ground: a new entry at the top of the focus's history."""
        folder = f"layers/focus/{ref}" if self.exists(f"layers/focus/{ref}") else f"layers/focus/archived/{ref}"
        stamp = date or datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        old = self.read(f"{folder}/history.md")
        self.write(f"{folder}/history.md", f"## {stamp} — grounded\n\n**Did:** {did}\n**Next:** {next_step}\n\n{old}")

    def field(self, relative: str, key: str) -> str:
        for line in self.read(relative).split("\n"):
            if line.startswith(key + ":"):
                return line[len(key) + 1 :].strip()
        return ""

    # ---- git facts

    def subjects(self, count: int = 1, ref: str = "HEAD") -> list[str]:
        return self.git("log", f"-{count}", "--format=%s", ref).split("\n")

    def files_in(self, ref: str = "HEAD") -> list[str]:
        return sorted(self.git("show", "--name-only", "--format=", ref).split("\n"))

    def unsaved(self) -> str:
        return self.git("status", "--porcelain", "--untracked-files=all")

    def set_heartbeat_age(self, number: str, minutes: float) -> None:
        path = self.path(f"surface/state/focus/{number}.json")
        moment = datetime.datetime.now().timestamp() - minutes * 60
        os.utime(path, (moment, moment))

    # ---- a common start: a kitchen focus with a plumbing child

    def kitchen_and_plumbing(self) -> None:
        self.ok(
            "open",
            "kitchen-renovation",
            "-i",
            "Renovate the kitchen by spring",
            "--holds",
            "work:home.kitchen,work:home.kitchen.plumbing",
            "--attach",
        )
        self.write("layers/work/home.kitchen/work.md", "# Kitchen\n")
        self.write("layers/work/home.kitchen.plumbing/work.md", "# Plumbing\n")
        self.ok(
            "open",
            "plumbing-quotes",
            "-i",
            "Get three plumbing quotes",
            "--parent",
            "f1",
            "--holds",
            "work:home.kitchen.plumbing",
            "--attach",
        )
        self.entry("f1-kitchen-renovation", "Started the kitchen.")
        self.entry("f2-plumbing-quotes", "Started on quotes.")
        self.ok("ground", "f1")
        self.ok("ground", "f2")
