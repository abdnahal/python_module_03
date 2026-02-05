def game_events(n: int) -> None:
    for i in range(n):
        if data[i]['event_type'] == 'death':
            message = 'died'
        elif data[i]['event_type'] == 'level_up':
            message = 'reached level'
        elif data[i]['event_type'] == 'login':
            message = 'logged in'
        elif data[i]['event_type'] == 'logout':
            message = 'logged out'
        elif data[i]['event_type'] == 'kill':
            message = 'killed'
        elif data[i]['event_type'] == 'item_found':
            message = 'found an item'
        else:
            message = 'event occurred'
        
        event_data = data[i]
        output = f"{event_data['player']} {message} - {event_data['data']['level']} (Zone: {event_data['data']['zone']})"
        yield output


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")
    for event in game_events(3):
        print(event)
