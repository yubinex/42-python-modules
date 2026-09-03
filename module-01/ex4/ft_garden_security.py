class Plant:
    def __init__(
        self, name: str, height: float, age: int, growth_rate: float = 0.8
    ) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self._growth_rate = growth_rate

        self.set_height(height)
        self.set_age(age)

        print("Plant created: ", end="")
        self.show()

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            return False
        self._height = height
        return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            return False
        self._age = age
        return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        height = round(self.get_height(), 1)
        age = self.get_age()
        print(f"{self._name}: {height}cm, " f"{age} days old")

    def grow(self) -> None:
        self.set_height(self.get_height() + self._growth_rate)

    def age(self) -> None:
        self.set_age(self.get_age() + 1)


def main() -> None:
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.0, 10)

    print()
    if plant.set_height(25.0):
        print(f"Height updated: {round(plant.get_height())}cm")
    if plant.set_age(30):
        print(f"Age updated: {plant.get_age()} days")

    print()
    if not plant.set_height(-5.0):
        print("Height update rejected")
    if not plant.set_age(-10):
        print("Age update rejected")

    print()
    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    main()
