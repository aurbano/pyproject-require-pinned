import re


def check_versions_pinned(dependencies):
    unpinned_dependencies = []
    non_develop_local_dependencies = []

    for package, version in dependencies.items():
        check_version_pinned(
            unpinned_dependencies, non_develop_local_dependencies, package, version
        )

    return unpinned_dependencies, non_develop_local_dependencies


def check_version_pinned(
    unpinned_dependencies,
    non_develop_local_dependencies,
    package,
    version,
):
    if package == "python":
        return

    version_pattern = re.compile(r"^\d+\..*$")  # Matches versions like '1.0.0'

    if isinstance(version, list):
        for each_version in version:
            check_version_pinned(
                unpinned_dependencies,
                non_develop_local_dependencies,
                package,
                each_version,
            )

    elif isinstance(version, dict):
        # Local packages must be set to develop = True
        if "path" in version and not version.get("develop", False):
            non_develop_local_dependencies.append((package, version))
        elif "version" in version:
            check_version_pinned(
                unpinned_dependencies,
                non_develop_local_dependencies,
                package,
                version["version"],
            )

    elif not version_pattern.match(version):
        unpinned_dependencies.append((package, version))
