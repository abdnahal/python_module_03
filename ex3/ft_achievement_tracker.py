def rare_achievement(players: dict):
    all = set()

    for ach in players.values:
        all = all.union(ach)

if __name__ == "__main__":
    players = {
    'alice': {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'},
    'bob': {'first_kill', 'level_10', 'boss_slayer', 'collector'},
    'charlie': {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}
    }

    print("=== Achievement Tracker System ===\n")
    print(f"Player alice achievements: {players['alice']}")
    print(f"Player bob achievements: {players['bob']}")
    print(f"Player charlie achievements: {players['charlie']}\n")
    
    print("=== Achievement Analytics ===")
    
    print(f"All unique achievemnets: {players['alice'].union(players['bob'], players['charlie'])}")
    print(f"Total unique achievements: {len(players['alice'].union(players['bob'], players['charlie']))}\n")
    print(f"Common to all players: {players['alice'].intersection(players['bob'], players['charlie'])}")
    print(f"Rare achievements (1 player): {}")
