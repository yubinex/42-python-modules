class Plant:
    name: str
    height: int
    age: int

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, " f"{self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    plant1 = Plant()
    plant2 = Plant()
    plant3 = Plant()

    plant1.name = "Rose"
    plant1.height = 25
    plant1.age = 30

    plant2.name = "Sunflower"
    plant2.height = 80
    plant2.age = 40

    plant3.name = "Cactus"
    plant3.height = 15
    plant3.age = 120

    plant1.show()
    plant2.show()
    plant3.show()
