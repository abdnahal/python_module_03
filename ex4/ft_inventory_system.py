import sys


def get_max(inventory: dict) -> str:
    max = ""
    temp = 0
    for key in inventory.keys():
        if inventory[key] > temp:
            temp = inventory[key]
            max = key
    return (max)


def restock(inventory: dict) -> list:
    lst = []
    for key in inventory.keys():
        if inventory[key] <= 1:
            lst.append(key)
    return lst


def get_min(inventory: dict) -> str:
    min = ""
    temp = 1
    for key in inventory.keys():
        if inventory[key] <= temp:
            temp = inventory[key]
            min = key
    return (min)


def get_moderate(inventory: dict) -> dict:
    dic = {}
    for key in inventory.keys():
        if inventory[key] >= 5:
            dic[key] = inventory[key]
    return dic


def get_scarce(inventory: dict) -> dict:
    dic = {}
    for key in inventory.keys():
        if inventory[key] < 5:
            dic[key] = inventory[key]
    return dic


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    if len(sys.argv) < 2:
        print("No arguments passed, try (item:value)")
    else:
        inventory = {}
        for arg in sys.argv[1:]:
            parsed = list(arg.split(":"))
            if parsed[0] in inventory.keys():
                inventory[parsed[0]] += int(parsed[1])
            else:
                inventory[parsed[0]] = int(parsed[1])
        print(f"Total items in inventory: {sum(inventory.values())}")
        print(f"Unique item types: {len(inventory.keys())}\n")
        print("=== Current Inventory ===")
        for key in inventory.keys():
            percent = inventory[key] / sum(inventory.values()) * 100
            print(f"{key}: {inventory[key]} units ({round(percent, 1)}%)")
        print()
        print("=== Inventory Statistics ===")
        max = max(inventory.values())
        print(f"Most abundant: {get_max(inventory)} ({max} units)")
        min = min(inventory.values())
        print(f"Least abundant: {get_min(inventory)} ({min} units)")
        print("=== Item Categories ===")
        print(f"Moderate: {get_moderate(inventory)}")
        print(f"Scarce: {get_scarce(inventory)}\n")
        print("=== Management Suggestions ===")
        print(f"Restock needed: {restock(inventory)}\n")
        print("=== Dictionary Properties Demo ===")
        print(f"Dictionary keys: {list(inventory.keys())}")
        print(f"Dictionary values: {list(inventory.values())}")
        check = 'sword' in inventory.keys()
        print(f"Sample lookup - 'sword' in inventory: {check}")
