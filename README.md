# Python Package Template

A modern template for python package development 🚀

## Features

### [uv]

`uv` now supports being a full python package project management tool!

- `uv run pytest`
- `uv sync`

### [GitHub Actions]

The project template comes with a great default GitHub Actions CI/CD pipeline:

- 🧪 Unit testing with [pytest]
- ✅ Linting and formatting with [ruff]
- 📦 Packaging and publishing to PyPI with [OIDC]

### Great Docs

Production ready docs with [mkdocs], [mkdocs-material] and [GitHub Pages]

> [!TIP]
> The docs will be built and deployed to GitHub Pages on every release, or do it manually at any time with `mkdocs gh-deploy`

## Usage

- Ensure you have [copier] installed:

```shell
uv tool install copier
```

- Call copier with this template and answer all the questions

```shell
copier copy gh:FollowTheProcess/python-package-template ./path/to/new/project
```

- Create a new virtual environment with `task dev` and start developing!

[uv]: https://docs.astral.sh/uv/
[GitHub actions]: https://docs.github.com/en/free-pro-team@latest/actions
[pytest]: https://docs.pytest.org/en/stable/
[ruff]: https://github.com/charliermarsh/ruff
[OIDC]: https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-pypi
[mkdocs]: https://www.mkdocs.org
[mkdocs-material]: https://squidfunk.github.io/mkdocs-material/
[GitHub Pages]: https://pages.github.com
[copier]: https://copier.readthedocs.io/en/stable/
