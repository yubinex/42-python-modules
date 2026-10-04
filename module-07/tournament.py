from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)

Opponent = tuple[CreatureFactory, BattleStrategy]


def battle(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    try:
        for first_index, first_opponent in enumerate(opponents):
            first_factory, first_strategy = first_opponent

            remaining_start = first_index + 1
            remaining_opponents = opponents[remaining_start:]
            for second_factory, second_strategy in remaining_opponents:
                first_creature = first_factory.create_base()
                second_creature = second_factory.create_base()

                print("\n* Battle *")
                print(first_creature.describe())
                print(" vs.")
                print(second_creature.describe())
                print(" now fight!")
                print(first_strategy.act(first_creature))
                print(second_strategy.act(second_creature))

    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle(
        [
            (flame_factory, normal_strategy),
            (healing_factory, defensive_strategy),
        ]
    )

    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(
        [
            (flame_factory, aggressive_strategy),
            (healing_factory, defensive_strategy),
        ]
    )

    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(
        [
            (aqua_factory, normal_strategy),
            (healing_factory, defensive_strategy),
            (transform_factory, aggressive_strategy),
        ]
    )


if __name__ == "__main__":
    main()
