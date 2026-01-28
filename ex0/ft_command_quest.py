import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    args = sys.argv[1:]
    ac = len(args)
    
    if ac < 2:
        print("No arguments provided!")
    
    print(f"Program name: {args[0]}")
    if ac > 1:
        print(f"Arguments received: {ac - 1}")
        i = 1
        for arg in args:
            print(f"Argument {i}: {arg}")
            i += 1
    print(f"Total arguments: {ac}")
