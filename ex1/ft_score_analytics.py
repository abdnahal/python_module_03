import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    try:
        args = list(map(int, sys.argv[1:]))
        ac = len(args)
    except ValueError:
        print("non-numeric value detected, MAT3AWEDHACH")
    
    if ac > 0:
        print(f"Scores processed: {args}")
        print(f"Total players: {ac}")
        print(f"Total score: {sum(args)}")
        print(f"Average score: {round(sum(args) / ac, 1)}")
        print(f"High score: {max(args)}")
        print(f"Low score: {min(args)}")
        print(f"Score range: {max(args) - min(args)}")
    else:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")


















# === Player Score Analytics ===
# Scores processed: [1500, 2300, 1800, 2100, 1950]
# Total players: 5
# Total score: 9650
# Average score: 1930.0
# High score: 2300
# Low score: 1500
# Score range: 800
# $> python3 ft_score_analytics.py
# === Player Score Analytics ===
# No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...