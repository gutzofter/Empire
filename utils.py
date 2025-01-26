def get_selection(prompt, min_value=None, max_value=None, choices=None):
    while True:
        try:
            if choices:
                print(prompt)
                for i, choice in enumerate(choices, start=1):
                    print(f"{i}) {choice}")
                min_value, max_value = 1, len(choices)
                prompt = "Select an option: "
            value = int(input(prompt))
            if min_value is not None and (value < min_value or value > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
            else:
                return value - 1 if choices else value
        except ValueError:
            print("Invalid input. Please enter a number.")

def clear_screen():
    """Clear the terminal screen."""
    print("\033c", end="")

def display_message(message):
    """Display a simple message."""
    print(message)

def display_list(title, items):
    """Display a numbered list."""
    print(title)
    for i, item in enumerate(items, start=1):
        print(f"{i}) {item}")

def display_land_holdings(players, barbarian_land):
    """Display the land holdings for all nations and barbarians."""
    clear_screen()
    print("Land Holdings:")
    print(f"1) Barbarians: {barbarian_land} acres")
    for i, player in enumerate(players, start=2):
        if player["active"]:
            print(f"{i}) {player['ruler_title']} {player['ruler_name']} controls {player['land']} acres")

def display_summary(players):
    """Display a summary of all players' stats."""
    clear_screen()
    print("Summary")
    print("Nobles   Soldiers   Merchants   Serfs   Land    Palace")
    print("-" * 50)
    for player in players:
        if player["active"]:
            ruler_info = f"{player['ruler_name']:<10}{player['ruler_title']:<8}"
            stats_info = (
                f"{player['nobles']:<8}{player['soldiers']:<8}{player['merchants']:<8}"
                f"{player['serfs']:<8}{player['land']:<8}{player['palace_completion'] * 100:>6.1f}%"
            )
            print(ruler_info + stats_info)

def display_weather_event(year, description):
    """Display the weather event for the year."""
    clear_screen()
    print(f"Year {year}\n")
    print(description)

def display_plague_event(player_name, serfs_lost, merchants_lost, soldiers_lost, nobles_lost):
    """Display the results of a plague event."""
    clear_screen()
    print(" " * 22 + "P L A G U E  ! ! !")
    print(f"\nBlack death has struck {player_name}'s nation.\n")
    print(f"{serfs_lost} serfs died.")
    print(f"{merchants_lost} merchants died.")
    print(f"{soldiers_lost} soldiers died.")
    print(f"{nobles_lost} nobles died.")

def display_battle_results(attacker, defender, attacker_losses, defender_losses):
    """Display the results of a battle."""
    clear_screen()
    print(f"Battle Results:\n")
    print(f"{attacker['ruler_name']} {attacker['ruler_title']} attacked {defender['ruler_name']} {defender['ruler_title']}.")
    print(f"Attacker losses: {attacker_losses} soldiers.")
    print(f"Defender losses: {defender_losses} soldiers.")
    if attacker_losses < defender_losses:
        print(f"{attacker['ruler_name']} {attacker['ruler_title']} is victorious!")
    else:
        print(f"{defender['ruler_name']} {defender['ruler_title']} successfully defended their land.")
