# Python Module 06 — Evaluation Notes

These notes follow `en.subject.pdf` (Version 2.0) and this repository's implementation.

## Run the demonstrations

Run commands from the repository root:

```bash
python3 ft_alembic_0.py
python3 ft_alembic_1.py
python3 ft_alembic_2.py
python3 ft_alembic_3.py
python3 ft_alembic_4.py  # Expected AttributeError
python3 ft_alembic_5.py
python3 ft_distillation_0.py
python3 ft_distillation_1.py
python3 ft_transmutation_0.py
python3 ft_transmutation_1.py
python3 ft_transmutation_2.py
python3 ft_kaboom_0.py
python3 ft_kaboom_1.py  # Expected circular-import ImportError
```

Checks:

```bash
python3 -m flake8 .
python3 -m mypy --exclude 'ft_alembic_4\.py$' .
```

`ft_alembic_4.py` deliberately calls a hidden attribute, so its mypy error is intentional.

## Part I — The Alembic: modules, packages, and `__init__.py`

- A **module** is a Python file, for example `elements.py`.
- A **package** is a directory that contains `__init__.py`, for example `alchemy/`.
- `import elements` imports the module and requires the `elements.create_fire()` form.
- `from elements import create_water` imports one name, so it can be called as `create_water()`.
- `import alchemy.elements` imports a nested module and uses `alchemy.elements.create_earth()`.
- `from alchemy.elements import create_air` imports one nested-module name directly.

`alchemy/__init__.py` defines the public package interface. It imports and exposes `create_air`, but does not expose `create_earth`. Therefore:

- `alchemy.create_air()` works.
- `alchemy.create_earth()` raises `AttributeError`.

## Part II — Distillation: imports across package boundaries

`alchemy/potions.py` needs all four elements:

- `from .elements import create_air, create_earth` is a **relative import** of a sibling module inside `alchemy`.
- `from elements import create_fire, create_water` is an **absolute import** of the root-level module.

`healing_potion()` combines earth and air. `strength_potion()` combines fire and water.

The top-level package re-exports:

- `strength_potion`
- `healing_potion` with the alias `heal`

That is why `alchemy.strength_potion()` and `alchemy.heal()` work.

## Part III — The Great Transmutation: absolute vs relative imports

`alchemy/transmutation/recipes.py` intentionally uses both import styles:

- Absolute: imports `create_air` and `create_fire` through their project paths.
- Relative: `from .. import potions` reaches the parent `alchemy` package.

`lead_to_gold()` combines air, the strength potion, and fire.

Exports are layered:

1. `transmutation/__init__.py` re-exports `lead_to_gold` from `recipes.py`.
2. `alchemy/__init__.py` re-exports it again.

This enables three access paths:

- `alchemy.transmutation.recipes.lead_to_gold()`
- `alchemy.transmutation.lead_to_gold()`
- `alchemy.lead_to_gold()`

### Absolute vs relative imports

- Use an **absolute import** when the complete project path is clearest, especially across package areas.
- Use a **relative import** for nearby sibling or parent modules within the same package.
- Consistency and readability matter; both styles resolve modules, but relative imports express the local package relationship.

## Part IV — Avoid the Explosion: circular imports

A circular import happens when two modules require each other while Python is still loading one of them. The second module then tries to access a name that has not been defined yet.

### Light grimoire: avoid the cycle

1. `light_validator.py` imports `light_spell_allowed_ingredients` from `light_spellbook.py`.
2. `light_spellbook.py` imports `validate_ingredients` **inside** `light_spell_record()`.
3. The local (late) import runs only after `light_spellbook.py` has fully loaded, so no circular-import failure occurs.

The validator is case-insensitive and returns the original ingredient text with ` - VALID` or ` - INVALID` appended. A spell is recorded for valid ingredients and rejected otherwise.

### Dark grimoire: intentionally create the cycle

1. `dark_spellbook.py` imports `validate_ingredients` from `dark_validator.py` at top level.
2. `dark_validator.py` immediately imports `dark_spell_allowed_ingredients` from `dark_spellbook.py` at top level.
3. `dark_spellbook.py` has not yet defined that function, so importing it raises `ImportError` for a partially initialized module.

`ft_kaboom_1.py` is supposed to fail this way. It demonstrates the problem; it is not a bug in the assignment.

## Likely evaluation questions

### What does `__init__.py` do?

It marks a directory as a package and runs when the package is imported. It can re-export selected names to define a clean public package API.

### What is the difference between `import module` and `from module import name`?

`import module` keeps the module namespace, so use `module.name()`. `from module import name` imports that specific name, so use `name()` directly.

### Why does `alchemy.create_earth()` fail?

`create_earth` exists in `alchemy/elements.py`, but `alchemy/__init__.py` does not re-export it. Importing the package only exposes its selected public names.

### Why use `as heal`?

It creates a public alias: `healing_potion` remains the implementation name, while the package exposes it as `alchemy.heal()`.

### Why are circular imports problematic?

Imports execute module code. If two modules import each other at top level, one can request a name before the other module has finished defining it.

### How did the light grimoire break the cycle?

It deferred one dependency with a function-local import, so Python loads both modules fully before the validator is imported and called.
