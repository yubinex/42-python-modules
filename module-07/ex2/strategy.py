import abc

from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    """Raised when a strategy cannot act on a creature."""


class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool: ...

    @abc.abstractmethod
    def act(self, creature: Creature) -> str: ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for "
                "this aggressive strategy"
            )

        # `is_valid` guarantees this; assert narrows the type for mypy.
        assert isinstance(creature, TransformCapability)
        return (
            f"{creature.transform()}\n{creature.attack()}\n{creature.revert()}"
        )


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for "
                f"this defensive strategy"
            )

        # `is_valid` guarantees this; assert narrows the type for mypy.
        assert isinstance(creature, HealCapability)
        return f"{creature.attack()}\n{creature.heal()}"
