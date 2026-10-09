from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    if any(
        allowed.lower() in ingredients.lower()
        for allowed in dark_spell_allowed_ingredients()
    ):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
