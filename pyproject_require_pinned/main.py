import sys

from pyproject_require_pinned.check_dependencies import check_dependencies


def main():
    filenames = sys.argv[1:]

    if not filenames:
        print("No files passed to the hook.")
        sys.exit(0)

    for filename in filenames:
        check_dependencies(filename)


if __name__ == "__main__":
    main()
