from pyproject_require_pinned.check_dependencies import _are_dependencies_valid


def test_valid() -> None:
    assert _are_dependencies_valid("test/data/valid.toml") is True


def test_invalid() -> None:
    assert _are_dependencies_valid("test/data/invalid.toml") is False


def test_invalid_list() -> None:
    assert _are_dependencies_valid("test/data/invalid_list.toml") is False


def test_invalid_dict() -> None:
    assert _are_dependencies_valid("test/data/invalid_dict.toml") is False
