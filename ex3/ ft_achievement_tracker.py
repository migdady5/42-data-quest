import random


all_achievements: list[str] = [
    "First Steps",
    "Boss Slayer",
    "Master Explorer",
    "Treasure Hunter",
    "Untouchable",
    "World Savior",
    "Crafting Genius",
    "Strategist",
    "Speed Runner",
    "Survivor",
    "Collector Supreme",
    "Sharp Mind",
    "Hidden Path Finder",
    "Unstoppable",
]


def gen_player_achievements() -> set[str]:
    count: int = random.randint(5, 9)
    selected: list[str] = random.sample(all_achievements, count)
    return set(selected)


def main() -> None:
    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()

    print("=== Achievement Tracker System ===")
    print("Player Alice:", alice)
    print("Player Bob:", bob)
    print("Player Charlie:", charlie)
    print("Player Dylan:", dylan)

    all_distinct: set[str] = alice.union(bob, charlie, dylan)
    print("All distinct achievements:", all_distinct)

    common: set[str] = alice.intersection(bob, charlie, dylan)
    print("Common achievements:", common)

    only_alice: set[str] = alice.difference(bob, charlie, dylan)
    only_bob: set[str] = bob.difference(alice, charlie, dylan)
    only_charlie: set[str] = charlie.difference(alice, bob, dylan)
    only_dylan: set[str] = dylan.difference(alice, bob, charlie)

    print("Only Alice has:", only_alice)
    print("Only Bob has:", only_bob)
    print("Only Charlie has:", only_charlie)
    print("Only Dylan has:", only_dylan)

    all_possible: set[str] = set(all_achievements)

    missing_alice: set[str] = all_possible.difference(alice)
    missing_bob: set[str] = all_possible.difference(bob)
    missing_charlie: set[str] = all_possible.difference(charlie)
    missing_dylan: set[str] = all_possible.difference(dylan)

    print("Alice is missing:", missing_alice)
    print("Bob is missing:", missing_bob)
    print("Charlie is missing:", missing_charlie)
    print("Dylan is missing:", missing_dylan)


if __name__ == "__main__":
    main()
