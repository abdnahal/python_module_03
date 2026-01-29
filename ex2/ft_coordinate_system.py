import math
import sys


def calculate_distance(cord: tuple) -> float:
    base = (0, 0, 0)
    distance = math.sqrt((cord[0]-base[0])**2 + (cord[1]-base[1])**2
                         + (cord[2]-base[2])**2)
    return (round(distance, 1))


def parse_coord(str: str) -> tuple:
    try:
        cord = tuple(str.split(","))
        cord = tuple(map(int, cord))
    except ValueError:
        print(f"Error parsing coordinates: invalid literal for int() with base 10: {cord}")
        return 0
    return (cord)


if __name__ == "__main__":
    args = sys.argv[1:]
    ac = len(args)

    if ac < 1:
        args = ["3, 4, 0"]
    
    coord = parse_coord(args[0])
    if coord:
        print(f"Parsed position: {coord}")
        print(f"Distance between (0, 0, 0) and {coord}: {calculate_distance(coord)}")
