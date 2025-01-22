from game_state import GameState
from game_logic import player_turn, process_weather_event, check_game_over
from display import display_summary, display_land_holdings

def main():
    print("Welcome to E M P I R E!")
    num_players = int(input("How many people are playing? (1-6): "))
    game_state = GameState(num_players)
    game_over = False

    while not game_over:
        game_state.current_year += 1
        process_weather_event(game_state)
        display_summary(game_state.players)
        display_land_holdings(game_state.players, game_state.barbarian_land)
        for game_state.current_player_index in range(game_state.num_players):
            if game_state.players[game_state.current_player_index]["active"]:
                player_turn(game_state)
        game_over = check_game_over(game_state)
    print("Thank you for playing E M P I R E!")

if __name__ == "__main__":
    main()
