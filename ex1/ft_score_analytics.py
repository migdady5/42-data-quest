import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    scores: list[int] = []

    for arg in sys.argv[1:]:
        try:
            score = int(arg)

            if score <= 0:
                continue

            scores = scores + [score]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if len(scores) == 0:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1>"
        )
        print("<score2> ...")
    else:
        total_score = sum(scores)
        total_players = len(scores)
        average_score = total_score / total_players
        high_score = max(scores)
        low_score = min(scores)
        score_range = high_score - low_score

        print("Scores processed:", scores)
        print("Total players:", total_players)
        print("Total score:", total_score)
        print("Average score:", average_score)
        print("High score:", high_score)
        print("Low score:", low_score)
        print("Score range:", score_range)


if __name__ == "__main__":
    main()
