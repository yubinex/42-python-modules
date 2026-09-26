import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")

    filename = sys.argv[1]
    file_obj: typing.IO[str] | None = None
    print(f"Accessing file '{filename}'")
    try:
        file_obj = open(filename, "r")
        content = file_obj.read()
        lines = [line + "#\n" for line in content.splitlines()]
        new_content = "".join(lines)

        print("---\n")
        print(content, end="")
        print("\n---")
    except OSError as e:
        # flush buffered stdout so earlier output appears before the error
        sys.stdout.flush()
        print(
            f"[STDERR] Error opening file '{filename}': {e}", file=sys.stderr
        )
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
        # no newline, so flush to show the prompt before reading
        print("Enter new file name (or empty): ", end="", flush=True)
        new_filename = sys.stdin.readline().strip()
        if new_filename == "":
            print("Not saving data.")
            return

        print(f"Saving data to '{new_filename}'")
        file_obj = open(new_filename, "w")
        file_obj.write(new_content)
        print(f"Data saved in file '{new_filename}'.")
    except OSError as e:
        # flush buffered stdout so earlier output appears before the error
        sys.stdout.flush()
        print(
            f"[STDERR] Error opening file '{new_filename}': {e}",
            file=sys.stderr,
        )
        print("Data not saved.")
        return
    finally:
        if file_obj is not None:
            file_obj.close()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
