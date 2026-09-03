class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def __init__(
        self, name: str, height: float, age: int, growth_rate: float = 0.8
    ) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self._growth_rate = growth_rate

        self._statistics = self.Statistics()

        self.set_height(height)
        self.set_age(age)

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

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

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        self._statistics.record_show()

        height = round(self.get_height(), 1)
        age = self.get_age()
        print(f"{self._name}: {height}cm, " f"{age} days old")

    def grow(self) -> None:
        self._statistics.record_grow()

        self.set_height(self.get_height() + self._growth_rate)

    def age(self, days: int = 1) -> None:
        self._statistics.record_age()

        self.set_age(self.get_age() + days)

    def display_statistics(self) -> None:
        self._statistics.display()


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


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        seed_yield: int = 42,
        growth_rate: float = 0.8,
    ) -> None:
        super().__init__(name, height, age, color, growth_rate)
        self._seed_count = 0
        self._seed_yield = seed_yield

    def bloom(self) -> None:
        super().bloom()
        self._seed_count = self._seed_yield

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seed_count}")


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
        self._shade_calls = 0

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self._trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(
            f"Tree {self._name} now produces a shade of "
            f"{round(self.get_height(), 1)}cm long and "
            f"{round(self._trunk_diameter, 1)}cm wide."
        )

    def display_statistics(self) -> None:
        super().display_statistics()
        print(f" {self._shade_calls} shade")


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

    def age(self, days: int = 1) -> None:
        super().age(days)
        self._nutritional_value += days


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.display_statistics()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(
        "Is 30 days more than a year? "
        f"-> {Plant.is_older_than_year(30)}"
    )
    print(
        "Is 400 days more than a year? "
        f"-> {Plant.is_older_than_year(400)}"
    )

    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red", growth_rate=8.0)
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print()
    print("=== Seed")
    sunflower = Seed(
        "Sunflower",
        80.0,
        45,
        "yellow",
        seed_yield=42,
        growth_rate=30.0,
    )
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print()
    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_statistics(anonymous)


if __name__ == "__main__":
    main()
