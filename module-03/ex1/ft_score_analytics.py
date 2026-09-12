import sys


def print_usage_message() -> None:
    print(
        "No scores provided. "
        "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
    )


def print_score_analytics(scores: list[int]) -> None:
    total_score = sum(scores)
    high_score = max(scores)
    low_score = min(scores)

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total_score}")
    print(f"Average score: {total_score / len(scores)}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {high_score - low_score}")


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print_usage_message()
        return

    scores: list[int] = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if len(scores) == 0:
        print_usage_message()
        return

    print_score_analytics(scores)


if __name__ == "__main__":
    main()
