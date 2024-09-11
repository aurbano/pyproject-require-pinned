# Require Pinned Dependencies in `pyproject.toml`

Ensure that all your dependencies listed are pinned:

```toml
[tool.poetry.dependencies]
toml = "^0.10.2"      # <- Error: Dependency version is not pinned
pre-commit = "3.6.2"  # Ok
```

## Usage

Add the following to your `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/aurbano/pyproject-require-pinned
    rev: v1.0.0
    hooks:
    -   id: pyproject-require-pinned
```