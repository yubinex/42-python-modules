import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")

    filename = sys.argv[1]
    file_obj: typing.IO[str] | None = None
    print(f"Accessing file '{filename}'")
    try:
        file_obj = open(filename, "r")
        content = file_obj.read()
        lines = content.splitlines(keepends=True)
        new_content = "".join(
            line[:-1] + "#\n" if line.endswith("\n") else line + "#"
            for line in lines
        )

        print("---\n")
        print(content, end="")
        print("\n---")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return
    finally:
        if file_obj is not None:
            file_obj.close()
            print(f"File '{filename}' closed.")

    try:
        print("\nTransform data:")
        print("---\n")
        print(new_content, end="")
        print("\n---")

        file_obj = None
        new_filename = input("Enter new file name (or empty): ").strip()
        if new_filename == "":
            print("Not saving data.")
            return

        print(f"Saving data to '{new_filename}'")
        file_obj = open(new_filename, "w")
        file_obj.write(new_content)
        print(f"Data saved in file '{new_filename}'.")
    except (OSError, UnicodeError) as e:
        print(f"Error writing to file '{new_filename}': {e}")
        return
    finally:
        if file_obj is not None:
            file_obj.close()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
