from ex0.creature import Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capability import HealCapability, TransformCapability


def test_healing_creature(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")

    base_creature: Creature = factory.create_base()
    print(" base:")
    print(base_creature.describe())
    print(base_creature.attack())
    if isinstance(base_creature, HealCapability):
        print(base_creature.heal())

    evolved_creature: Creature = factory.create_evolved()
    print(" evolved:")
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    if isinstance(evolved_creature, HealCapability):
        print(evolved_creature.heal())


def test_transformation_creature(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")

    base_creature: Creature = factory.create_base()
    print(" base:")
    print(base_creature.describe())
    print(base_creature.attack())
    if isinstance(base_creature, TransformCapability):
        print(base_creature.transform())
        print(base_creature.attack())
        print(base_creature.revert())

    evolved_creature: Creature = factory.create_evolved()
    print(" evolved:")
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    if isinstance(evolved_creature, TransformCapability):
        print(evolved_creature.transform())
        print(evolved_creature.attack())
        print(evolved_creature.revert())


def main() -> None:
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    test_healing_creature(healing_factory)
    print()
    test_transformation_creature(transform_factory)


if __name__ == "__main__":
    main()
