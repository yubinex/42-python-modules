def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    input1: str = "25"
    input2: str = "abc"

    try:
        print(f"Input data is '{input1}'")
        print(f"Temperature is now {input_temperature(input1)}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    try:
        print(f"\nInput data is '{input2}'")
        print(f"Temperature is now {input_temperature(input2)}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("\nAll tests completed - program didn't crash!")
