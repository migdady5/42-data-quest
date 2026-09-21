import random


def run_data_alchemist() -> None:
    print("=== Game Data Alchemist ===\n")

    player_names = [
        'Alice', 'bob', 'Charlie', 'dylan',
        'Emma', 'Gregory', 'john', 'kevin', 'Liam'
    ]

    print(f"Initial list of players: {player_names}")

    capitalized_names = [name.capitalize() for name in player_names]
    print(f"New list with all names capitalized: {capitalized_names}")

    original_capitalized_names = [
        name for name in player_names if name[0].isupper()
    ]
    print(f"New list of capitalized names only: {original_capitalized_names}")

    score_dict = {
        name: random.randint(0, 999) for name in capitalized_names
    }
    print(f"\nScore dict: {score_dict}")

    score_average = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(score_average, 2)}")

    high_scores = {
        name: score_dict[name]
        for name in score_dict.keys()
        if score_dict[name] > score_average
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    run_data_alchemist()
