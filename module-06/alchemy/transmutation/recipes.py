from alchemy.elements import create_air
from elements import create_fire

from .. import potions


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew '{create_air()}' and "
        f"'{potions.strength_potion()}' mixed with '{create_fire()}'"
    )
