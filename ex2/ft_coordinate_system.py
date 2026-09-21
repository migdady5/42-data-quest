import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        data = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = data.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        for p in parts:
            try:
                float(p.strip())
            except ValueError:
                value = p.strip()
                print(
                    f"Error on parameter '{value}': "
                    f"could not convert string to float: '{value}'"
                )
                break
        else:
            x, y, z = [float(p.strip()) for p in parts]
            return (x, y, z)


def distance(
    p1: tuple[float, float, float],
    p2: tuple[float, float, float],
) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return math.sqrt(
        (x2 - x1) ** 2
        + (y2 - y1) ** 2
        + (z2 - z1) ** 2
    )


def distance_from_origin(p: tuple[float, float, float]) -> float:
    x, y, z = p
    return math.sqrt(x ** 2 + y ** 2 + z ** 2)


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    player1 = get_player_pos()

    print(f"Got a first tuple: {player1}")
    print(f"It includes: X={player1[0]}, Y={player1[1]}, Z={player1[2]}")

    dis_from_origin = distance_from_origin(player1)
    print(f"Distance to center: {dis_from_origin:.4f}\n")

    print("Get a second set of coordinates")
    player2 = get_player_pos()

    print(
        "Distance between the 2 sets of coordinates: "
        f"{distance(player1, player2):.4f}"
    )


if __name__ == "__main__":
    main()
