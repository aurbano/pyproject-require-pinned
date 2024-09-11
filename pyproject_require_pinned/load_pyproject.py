import toml


def load_pyproject(file_path):
    with open(file_path, "r") as f:
        return toml.load(f)
