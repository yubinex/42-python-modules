def secure_archive(
    filename: str, action: str = "r", content: str = ""
) -> tuple[bool, str]:
    if action not in ("r", "w"):
        return (False, "Invalid action")

    try:
        with open(filename, action) as file:
            if action == "r":
                return (True, file.read())
            else:
                file.write(content)
                return (True, "Content successfully written to file")

    except (OSError, UnicodeError) as e:
        return (False, f"{e}")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    res = secure_archive(__file__)
    print(res)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    ok, content = res
    if ok:
        print(secure_archive("new_file.txt", "w", content))
