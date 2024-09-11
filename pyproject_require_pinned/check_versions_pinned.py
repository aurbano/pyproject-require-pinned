import re


def check_versions_pinned(dependencies):
    version_pattern = re.compile(r"^\d+\..*$")  # Matches versions like '1.0.0'
    unpinned_dependencies = []
    non_develop_local_dependencies = []

    for package, version in dependencies.items():
        if package == "python":
            continue

        if isinstance(version, dict):
            # Local packages must be set to develop = True
            if "path" in version and not version.get("develop", False):
                non_develop_local_dependencies.append((package, version))

        elif not version_pattern.match(version):
            unpinned_dependencies.append((package, version))

    return unpinned_dependencies, non_develop_local_dependencies
