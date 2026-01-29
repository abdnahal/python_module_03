import math
import sys


def calculate_distance(coord: tuple) -> float:
    base = (0, 0, 0)
    x, y, z = coord
    i, j, k = base
    distance = math.sqrt((x-i)**2 + (y-j)**2 + (z-k)**2)
    return (round(distance, 2))


def parse_coord(str: str) -> tuple:
    try:
        cord = tuple(str.split(","))
        cord = tuple(map(int, cord))
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - type: {type(e).__name__}, Args: {e}")
        return 0
    return (cord)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    tup = (10, 20, 5)
    print(f"Position created: {tup}")
    print(f"Distance between (0, 0, 0) and {tup}: {calculate_distance(tup)}\n")

    args = sys.argv[1:]
    ac = len(args)

    if ac < 1:
        args = ["3, 4, 0"]

    coord = parse_coord(args[0])
    if coord:
        print(f"Parsing coordinates: {args[0]} ")
        print(f"Parsed position: {coord}")
        distance = calculate_distance(coord)
        print(f"Distance between (0, 0, 0) and {coord}: {distance}\n")

    print("Unpacking demonstration:")
    if coord:
        x, y, z = coord
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
