import math


def calculate_distance(
    first: tuple[float, float, float],
    second: tuple[float, float, float],
) -> float:
    return math.sqrt(
        (second[0] - first[0]) ** 2
        + (second[1] - first[1]) ** 2
        + (second[2] - first[2]) ** 2
    )


def get_player_pos() -> tuple[float, float, float]:
    while True:
        parts = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        ).split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        coordinates: list[float] = []
        for part in parts:
            try:
                coordinates.append(float(part))
            except ValueError as e:
                print(f"Error on parameter '{part}': {e}")
                break
        else:
            return (coordinates[0], coordinates[1], coordinates[2])


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    pos_1 = get_player_pos()
    print(f"Got first tuple: {pos_1}")
    print(f"It includes: X={pos_1[0]}, Y={pos_1[1]}, Z={pos_1[2]}")
    print(
        f"Distance to center: "
        f"{round(calculate_distance(pos_1, (0.0, 0.0, 0.0)), 4)}"
    )
    print()
    print("Get a second set of coordinates")
    pos_2 = get_player_pos()
    print(
        f"Distance between the 2 sets of coordinates: "
        f"{round(calculate_distance(pos_1, pos_2), 4)}"
    )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n> Program interrupted.")
