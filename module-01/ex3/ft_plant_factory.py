class Plant:
    def __init__(
        self, name: str, height: float, age_days: int, growth_rate: float = 0.8
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
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
