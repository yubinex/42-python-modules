class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        Exception.__init__(self, message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        Exception.__init__(self, message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        Exception.__init__(self, message)


def check_plant_health() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water_supply() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("Testing PlantError...")
    try:
        check_plant_health()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print()
    print("Testing WaterError...")
    try:
        check_water_supply()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print()
    print("Testing catching all garden errors...")
    try:
        check_plant_health()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water_supply()
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_custom_errors()
    print("\nAll custom error types work correctly!")
