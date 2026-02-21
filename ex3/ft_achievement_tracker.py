def rare_achievements(players: dict) -> set:
    all_achievements = set()

    for achievements in players.values():
        all_achievements = all_achievements.union(achievements)

    rare = set()

    for achievement in all_achievements:
        count = 0
        for achievements in players.values():
            if achievement in achievements:
                count += 1

        if count == 1:
            rare.add(achievement)

    return rare


if __name__ == "__main__":
    players = {
        'alice': {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'},
        'bob': {'first_kill', 'level_10', 'boss_slayer', 'collector'},
        'charlie': {'level_10', 'treasure_hunter', 'boss_slayer',
                    'speed_demon', 'perfectionist'}
    }
    unique = players['alice'].union(players['bob'], players['charlie'])
    total = len(players['alice'].union(players['bob'], players['charlie']))
    common = players['alice'].intersection(players['bob'], players['charlie'])
    rare = rare_achievements(players)

    print("=== Achievement Tracker System ===\n")
    print(f"Player alice achievements: {players['alice']}")
    print(f"Player bob achievements: {players['bob']}")
    print(f"Player charlie achievements: {players['charlie']}\n")
    print("=== Achievement Analytics ===")
    print(f"All unique achievemnets: {unique}")
    print(f"Total unique achievements: {total}\n")
    print(f"Common to all players: {common}")
    print(f"Rare achievements (1 player): {rare}\n")

    common = players['alice'].intersection(players['bob'])
    print(f"Alice vs Bob common: {common}")
    print(f"Alice unique: {players['alice'].difference(players['bob'])}")
    print(f"Bob unique: {players['bob'].difference(players['alice'])}\n")
