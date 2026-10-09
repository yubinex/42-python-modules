import random

players = [
    "Okabe",
    "kurisu",
    "Mayuri",
    "daru",
    "Suzuha",
    "moeka",
    "Faris",
    "ruka",
    "Maho",
    "kagari",
]


def main() -> None:
    all_caps = [name.capitalize() for name in players]
    only_caps = [name for name in players if name == name.capitalize()]

    print("=== Game Data Alchemist ===")
    print()
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {all_caps}")
    print(f"New list of capitalized names only: {only_caps}")
    print()

    score_dict = {name: random.randint(0, 1000) for name in all_caps}
    score_avg = sum(score_dict.values()) / len(score_dict)
    high_scores = {
        name: score for name, score in score_dict.items() if score > score_avg
    }

    print(f"Score dict: {score_dict}")
    print(f"Score average is {round(score_avg, 2)}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
