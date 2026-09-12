# MyPy errors are expected here
def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            int("abc")
        case 1:
            1 / 0
        case 2:
            open("/non/existent/file")
            return
        case 3:
            "temperature: " + 25
        case _:
            return


def test_error_types() -> None:
    for operation in (0, 1, 2, 3, 4):
        print(f"Testing operation {operation}...")
        try:
            garden_operations(operation_number=operation)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        else:
            print("Operation completed successfully")

    print("\nTesting combined exception handling...")
    for operation in (0, 3):
        try:
            garden_operations(operation)
        except (ValueError, TypeError) as e:
            print(f"Caught combined error: {e}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")
