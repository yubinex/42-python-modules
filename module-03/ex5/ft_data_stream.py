import random
import typing

players = ["alice", "bob", "charlie", "dylan"]
actions = ["run", "eat", "sleep", "grab"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        player, action = events.pop(index)
        yield (player, action)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    generator = gen_event()
    for i in range(1000):
        player, action = next(generator)
        print(f"Event {i}: Player {player} did action {action}")

    events: list[tuple[str, str]] = []
    for _ in range(10):
        events.append(next(generator))
    print(f"Built list of {len(events)} events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
