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


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        growth_rate: float = 0.8,
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._color = color
        self._is_blooming = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._is_blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")

    def bloom(self) -> None:
        self._is_blooming = True


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
        growth_rate: float = 0.8,
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self._trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{round(self.get_height(), 1)}cm long and "
            f"{round(self._trunk_diameter, 1)}cm wide."
        )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        nutritional_value: int,
        growth_rate: float = 0.8,
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    flower.show()
    print("[asking the rose to bloom]")
    flower.bloom()
    flower.show()

    print()
    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()

    print()
    print("=== Vegetable")
    vegetable = Vegetable("Tomato", 5.0, 10, "April", 0, 2.1)
    vegetable.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(1, 21):
        vegetable.grow()
        vegetable.age()
    vegetable.show()


if __name__ == "__main__":
    main()
