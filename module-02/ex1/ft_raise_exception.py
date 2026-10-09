def input_temperature(temp_str: str) -> int:
    temp_int: int = int(temp_str)
    if temp_int < 0:
        raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
    elif temp_int > 40:
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
    return temp_int


def test_temperature() -> None:
    input1: str = "25"
    input2: str = "abc"
    input3: str = "100"
    input4: str = "-50"

    try:
        print(f"Input data is '{input1}'")
        print(f"Temperature is now {input_temperature(input1)}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    try:
        print(f"\nInput data is '{input2}'")
        print(f"Temperature is now {input_temperature(input2)}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    try:
        print(f"\nInput data is '{input3}'")
        print(f"Temperature is now {input_temperature(input3)}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    try:
        print(f"\nInput data is '{input4}'")
        print(f"Temperature is now {input_temperature(input4)}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
    print("\nAll tests completed - program didn't crash!")
