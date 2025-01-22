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
            print(
                f"{player['ruler_name']} {player['ruler_title']} "
                f"{player['nobles']:>5} {player['soldiers']:>10} {player['merchants']:>10} "
                f"{player['serfs']:>10} {player['land']:>8} {player['palace_completion'] * 10:>6}%"
            )

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
