import sys

from pyproject_require_pinned.check_versions_pinned import check_versions_pinned
from pyproject_require_pinned.load_pyproject import load_pyproject


def check_dependencies(project_path: str):
    if _are_dependencies_valid(project_path):
        sys.exit(0)
    else:
        sys.exit(1)


def _are_dependencies_valid(project_path: str):
    try:
        data = load_pyproject(project_path)
    except Exception as e:
        print(f"Error loading file: {e}")
        return False

    dependencies = data.get("dependencies", {})
    poetry_dependencies = data.get("tool", {}).get("poetry", {}).get("dependencies", {})

    all_dependencies = {**dependencies, **poetry_dependencies}

    if not all_dependencies:
        print("No dependencies found.")
        return True

    unpinned_dependencies, non_develop_local_dependencies = check_versions_pinned(
        all_dependencies
    )

    if unpinned_dependencies or non_develop_local_dependencies:
        print("Error in " + project_path)
        if unpinned_dependencies:
            print("The following dependencies do not have pinned versions:")

            for package, version in unpinned_dependencies:
                print(f"- {package}: {version}")

        if non_develop_local_dependencies:
            print("The following local dependencies are not set to develop = True:")

            for package, version in non_develop_local_dependencies:
                print(f"- {package}")
        return False
    else:
        return True
