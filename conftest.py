"""
Shared fixtures and config for tests.
"""

from __future__ import annotations

import shutil
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import copier
import pytest
import yaml

TEMPLATE_ROOT = Path(__file__).parent.resolve()


@pytest.fixture
def template(tmp_path_factory: pytest.TempPathFactory) -> Iterator[Path]:
    """
    Build a package from the template in a temporary directory,
    yield the directory back to the caller, and then clean it up.
    """
    template = tmp_path_factory.mktemp("function")
    copier.run_copy(
        src_path=str(TEMPLATE_ROOT),
        dst_path=str(template),
        data={
            "name": "testy",
            "slug": "testy",
            "description": "A test package for testing",
            "license": "MIT",
            "github_username": "TestUser",
            "github_url": "https://github.com/TestUser/testy",
            "author_name": "Test McTest",
            "author_email": "testmctest@gmail.com",
        },
        vcs_ref="HEAD",
    )

    yield template

    shutil.rmtree(template)


@pytest.fixture
def template_vars() -> list[str]:
    """
    Fixture to return a list of all copier template tags to check
    for in build projects to ensure we don't have any partial renders.
    """
    copier_yaml = TEMPLATE_ROOT.joinpath("copier.yml")
    with copier_yaml.open() as f:
        data: dict[str, Any] = yaml.safe_load(f)

    return ["{{" + f"{key}" + "}}" for key in data]
