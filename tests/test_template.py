"""
Tests for the template generation.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_expected_files(template: Path) -> None:
    """
    Tests that a sample of the correct files have indeed
    been rendered.
    """
    expected_files = [
        ".github/ISSUE_TEMPLATE/bug.yml",
        ".github/ISSUE_TEMPLATE/feature.yml",
        ".github/ISSUE_TEMPLATE/question.yml",
        ".github/workflows/CI.yml",
        ".github/workflows/labeler.yml",
        ".github/workflows/release-drafter.yml",
        ".github/workflows/release.yml",
        ".github/dependabot.yml",
        ".github/labels.yml",
        ".github/pull_request_template.md",
        ".github/release-drafter.yml",
        ".gitattributes",
        ".gitignore",
        "Taskfile.yml",
        "README.md",
        "pyproject.toml",
        "src/testy/__init__.py",
        "src/testy/testy.py",
        "tests/test_obvious.py",
    ]

    for file in expected_files:
        absolute_path = template.joinpath(file)
        assert absolute_path.exists(), f"{file} did not exist in generated template"


def test_no_template_tags_remaining(template: Path, template_vars: list[str]) -> None:
    """
    Tests that no Jinja template tags remain in any of the
    rendered files.
    """
    for path in template.rglob("*"):
        if not path.is_dir():
            contents = path.read_text(encoding="utf-8")
            for var in template_vars:
                assert var not in contents, f"Found template tag ({var}) in {path}"


def test_project_passes_ruff_format(template: Path) -> None:
    """
    Tests that a freshly rendered template passes ruff formatting.
    """
    # Will raise an exception if ruff format fails
    subprocess.run(
        ["ruff", "format", ".", "--check"],
        check=True,
        stderr=sys.stderr,
        stdout=sys.stdout,
        shell=False,
        cwd=str(template),
    )


def test_project_passes_ruff(template: Path) -> None:
    """
    Tests that a freshly rendered template passes ruff linting.
    """
    # Will raise an exception if ruff fails
    subprocess.run(
        ["ruff", "check", "."],
        check=True,
        stderr=sys.stderr,
        stdout=sys.stdout,
        shell=False,
        cwd=str(template),
    )
