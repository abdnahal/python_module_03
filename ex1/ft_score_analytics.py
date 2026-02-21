import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    try:
        args = list(map(int, sys.argv[1:]))
        ac = len(args)
        if ac > 0:
            print(f"Scores processed: {args}")
            print(f"Total players: {ac}")
            print(f"Total score: {sum(args)}")
            print(f"Average score: {round(sum(args) / ac, 1)}")
            print(f"High score: {max(args)}")
            print(f"Low score: {min(args)}")
            print(f"Score range: {max(args) - min(args)}")
        else:
            print("No scores provided. Usage: python3 ft_score_analytics.py "
                  "<score1> <score2> ...")
    except ValueError:
        print("non-numeric value detected, MAT3AWEDHACH")
