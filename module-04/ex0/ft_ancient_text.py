import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")

    filename = sys.argv[1]
    file_obj: typing.IO[str] | None = None
    print(f"Accessing file '{filename}'")
    try:
        file_obj = open(filename, "r")
        content = file_obj.read()

        print("---\n")
        print(content, end="")
        print("\n---")
    except (OSError, UnicodeError) as e:
        print(f"Error opening file '{filename}': {e}")
    finally:
        if file_obj is not None:
            file_obj.close()
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
