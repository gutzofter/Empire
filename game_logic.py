import random
from display import display_message, display_list, display_weather_event
from input_utils import get_selection

def process_weather_event(game_state):
    """
    Determine and display the weather event for the year.
    """
    weather_events = {
        1: "Poor weather. No rain. Locusts migrate.",
        2: "Early frosts. Arid conditions.",
        3: "Flash floods. Too much rain.",
        4: "Average weather. Good year.",
        5: "Fine weather. Long summer.",
        6: "Fantastic weather! Great year!",
    }
    weather_roll = random.randint(1, 6)
    description = weather_events[weather_roll]
    display_weather_event(game_state.current_year, description)

def player_turn(game_state):
    """
    Handle a single player's turn.
    """
    player = game_state.players[game_state.current_player_index]
    display_message(f"{player['ruler_title']} {player['ruler_name']}'s turn:")
    actions = ["Buy Grain", "Sell Grain", "Attack", "End Turn"]
    choice_index = get_selection("Choose an action:", choices=actions)

    if choice_index == 0:  # Buy Grain
        buy_grain(game_state, player)
    elif choice_index == 1:  # Sell Grain
        sell_grain(game_state, player)
    elif choice_index == 2:  # Attack
        attack(game_state, player)
    elif choice_index == 3:  # End Turn
        return

def buy_grain(game_state, buyer):
    """
    Allow a player to buy grain from another player or the market.
    """
    sellers = [
        p for p in game_state.players
        if p["active"] and p["grain_reserve"] > 0 and p != buyer
    ]
    if not sellers:
        display_message("No grain available for purchase.")
        return

    seller_choices = [
        f"{seller['ruler_title']} {seller['ruler_name']} ({seller['grain_reserve']} bushels)"
        for seller in sellers
    ]
    seller_index = get_selection("Select a seller:", choices=seller_choices)
    seller = sellers[seller_index]

    max_purchase = seller["grain_reserve"]
    amount = get_selection(
        f"How many bushels do you want to buy? (Max: {max_purchase})", min_value=1, max_value=max_purchase
    )
    cost = amount * seller["sales_tax"]
    if buyer["treasury"] >= cost:
        buyer["grain_reserve"] += amount
        buyer["treasury"] -= cost
        seller["grain_reserve"] -= amount
        seller["treasury"] += cost
        display_message(f"Transaction complete: Bought {amount} bushels for {cost} gold.")
    else:
        display_message("You can't afford that!")

def sell_grain(game_state, seller):
    """
    Allow a player to sell grain to the market.
    """
    if seller["grain_reserve"] <= 0:
        display_message("You have no grain to sell.")
        return

    max_sell = seller["grain_reserve"]
    amount = get_selection(
        f"How many bushels do you want to sell? (Max: {max_sell})", min_value=1, max_value=max_sell
    )
    price_per_bushel = random.randint(10, 20)
    earnings = amount * price_per_bushel
    seller["grain_reserve"] -= amount
    seller["treasury"] += earnings
    display_message(f"Sold {amount} bushels for {earnings} gold.")

def attack(game_state, attacker):
    """
    Handle an attack action by the current player.
    """
    targets = [
        p for p in game_state.players if p["active"] and p != attacker
    ]
    targets.append({"ruler_title": "Barbarians", "ruler_name": "", "land": game_state.barbarian_land})

    target_choices = [
        f"{target['ruler_title']} {target['ruler_name']} ({target['land']} acres)"
        for target in targets
    ]
    target_index = get_selection("Choose a target to attack:", choices=target_choices)
    target = targets[target_index]

    if target.get("ruler_title") == "Barbarians":
        defender_strength = random.randint(50, 150)
    else:
        defender_strength = target["soldiers"] * target["army_efficiency"]

    attacker_strength = attacker["soldiers"] * attacker["army_efficiency"]
    if attacker_strength > defender_strength:
        land_gained = random.randint(5, 50)
        display_message(f"Victory! You gained {land_gained} acres of land.")
        attacker["land"] += land_gained
        if target.get("ruler_title") == "Barbarians":
            game_state.barbarian_land -= land_gained
        else:
            target["land"] -= land_gained
            if target["land"] <= 0:
                target["active"] = False
                display_message(f"{target['ruler_title']} {target['ruler_name']} has been defeated!")
    else:
        display_message("Defeat! Your soldiers were overpowered.")

def check_game_over(game_state):
    """
    Determine if the game is over.
    """
    active_players = [p for p in game_state.players if p["active"]]
    if len(active_players) <= 1:
        winner = active_players[0] if active_players else None
        if winner:
            display_message(f"{winner['ruler_title']} {winner['ruler_name']} is the ruler of the world!")
        else:
            display_message("The world has been destroyed. No one rules.")
        return True
    return False
