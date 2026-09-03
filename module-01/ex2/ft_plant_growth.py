class Plant:
    def __init__(
        self, name: str, height: float, age_days: int, growth_rate: float
    ) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 1)}cm, {self.age_days} days old"
        )

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.age_days += 1


def main() -> None:
    growth_cycle: int = 7

    plant = Plant("Rose", 25.0, 30, 0.8)

    print("=== Garden Plant Growth ===")
    starting_height = plant.height
    for day in range(1, growth_cycle + 1):
        print(f"=== Day {day} ===")
        plant.show()
        plant.grow()
        plant.age()
    print(f"Growth this week: {round(plant.height - starting_height)}cm")


if __name__ == "__main__":
    main()
