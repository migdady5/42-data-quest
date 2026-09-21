import random
import typing


players: list[str] = ["alice", "bob", "charlie", "dylan"]
actions: list[str] = [
    "run",
    "jump",
    "sleep",
    "eat",
    "move",
    "grab",
    "swim",
    "climb",
    "release",
    "use",
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    game_events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while game_events:
        index = random.randrange(len(game_events))
        yield game_events.pop(index)


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_generator = gen_event()

    for event_number in range(1000):
        player_name, player_action = next(event_generator)
        print(
            f"Event {event_number}: Player {player_name} "
            f"did action {player_action}"
        )

    game_events = [next(event_generator) for _ in range(10)]
    print(f"Built list of 10 events: {game_events}")

    for event in consume_event(game_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {game_events}")


if __name__ == "__main__":
    main()
