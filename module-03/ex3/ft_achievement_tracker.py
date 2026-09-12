import random

ACHIEVEMENTS = [
    "The Choice of Steins Gate",
    "Prologue of the Beginning and the End",
    "Time Travel Paranoia",
    "Butterfly Effect's Divergence",
    "Chaos Theory Homeostasis",
    "Dogma in Event Horizon",
    "Irreversible Reboot",
    "Open The Steins Gate",
    "All Worldlines Complete",
    "Skyclad Observer",
    "Stardust Sky",
    "Isolated Jamais Vu",
    "Warrior Girl's Pride",
    "Paradox Meltdown",
    "Genius Girl's Melancholy",
]


def gen_player_achievements() -> set[str]:
    rand_amount = random.randint(8, 11)
    achievements = random.sample(ACHIEVEMENTS, rand_amount)
    return set(achievements)


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()

    all_possible = set(ACHIEVEMENTS)
    all_distinct = set.union(alice, bob, charlie, dylan)
    common = set.intersection(alice, bob, charlie, dylan)

    alice_only = alice.difference(bob.union(charlie, dylan))
    alice_missing = all_possible.difference(alice)

    bob_only = bob.difference(alice.union(charlie, dylan))
    bob_missing = all_possible.difference(bob)

    charlie_only = charlie.difference(alice.union(bob, dylan))
    charlie_missing = all_possible.difference(charlie)

    dylan_only = dylan.difference(alice.union(bob, charlie))
    dylan_missing = all_possible.difference(dylan)

    print(f"All distinct achievements: {all_distinct}")
    print()
    print(f"Common achievements: {common}")
    print()
    print(f"Only Alice has: {alice_only}")
    print(f"Only Bob has: {bob_only}")
    print(f"Only Charlie has: {charlie_only}")
    print(f"Only Dylan has: {dylan_only}")
    print()
    print(f"Alice is missing: {alice_missing}")
    print(f"Bob is missing: {bob_missing}")
    print(f"Charlie is missing: {charlie_missing}")
    print(f"Dylan is missing: {dylan_missing}")


if __name__ == "__main__":
    main()
