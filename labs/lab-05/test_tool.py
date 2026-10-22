from tools import read_github_files


def show(title, files):
    print(f"\n===== {title} =====")
    content = read_github_files(files)
    # Long files would flood the terminal; the start and the end (where a
    # truncation note goes) are enough to check the output.
    if len(content) > 1500:
        print(content[:700] + "\n\n[... middle of output omitted by test_tool.py ...]\n\n" + content[-500:])
    else:
        print(content)


def test():
    print("Testing read_github_files...\n")

    show("Single file (README example from the lab)", [
        {"owner": "microsoft", "repo": "vscode", "path": "package.json", "ref": "main"},
    ])
    show("File that doesn't exist", [
        {"owner": "microsoft", "repo": "vscode", "path": "does-not-exist.json", "ref": "main"},
    ])
    show("Misspelled repo name", [
        {"owner": "microsoft", "repo": "vscodee", "path": "package.json", "ref": "main"},
    ])
    show("Very large file (3,700+ lines)", [
        {"owner": "python", "repo": "cpython", "path": "Python/pystate.c", "ref": "main"},
    ])
    show("Two files in one call, one at a tag and one at a commit SHA", [
        {"owner": "microsoft", "repo": "vscode", "path": "package.json", "ref": "1.99.0"},
        {
            "owner": "pallets",
            "repo": "click",
            "path": "src/click/_winconsole.py",
            "ref": "94f17e276fbdd7348b88b05170923ecacb7b32bf",
        },
    ])
    show("Missing ref (defaults to main) and a missing path", [
        {"owner": "pallets", "repo": "flask", "path": "README.md"},
        {"owner": "pallets", "repo": "flask", "ref": "main"},
    ])
    show("Binary file", [
        {"owner": "python", "repo": "cpython", "path": "PC/icons/logox128.png", "ref": "main"},
    ])


if __name__ == "__main__":
    test()
