import random

# Constants and Data Structures
A = [[0] * 20 for _ in range(7)]  # Array for game stats
Z = [[None] * 7 for _ in range(7)]  # Array for names and roles
BA = 6000  # Initial barbarian land count
NY = 0  # Starting year
NP = 0  # Number of players
K = 1  # Current player index

def initialize_game():
    """
    Initialize the game, setting up players and initial stats.
    """
    print("E M P I R E".center(40))
    input("(Always hit <enter> to continue)")
    print("\033c", end="")  # Clear screen

    global A, Z, BA, NP

    # Initialize game data
    for i in range(1, 7):
        for j in range(7):
            Z[i][j] = None  # Placeholder for names and roles

    for i in range(1, 7):
        A[i][1] = 10000
        A[i][2] = 15000 + random.randint(0, 10000)
        A[i][3] = 2000
        A[i][4] = 1000
        A[i][7] = 25
        A[i][8] = 20
        A[i][9] = 5
        A[i][10] = 35
        A[i][15] = 20
        A[i][17] = 2
        A[i][18] = 1
        A[i][19] = 15

    # Player input
    while True:
        try:
            NP = int(input("How many people are playing? "))
            if NP > 6:
                print("Maximum players: 6")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Assign ruler names
    for i in range(1, NP + 1):
        Z[i][1] = input(f"Who is the ruler of Land {i}? ")
        Z[i][0] = input(f"What is the ruler's title (e.g., King, Queen) for Land {i}? ")

def process_weather_event():
    """
    Simulate and display the weather event for the year.
    """
    global NY
    NY += 1
    print("\033c", end="")  # Clear screen
    print(f"Year {NY}\n")

    NW = random.randint(1, 6)  # Weather event
    weather_events = {
        1: "Poor weather. No rain. Locusts migrate.",
        2: "Early frosts. Arid conditions.",
        3: "Flash floods. Too much rain.",
        4: "Average weather. Good year.",
        5: "Fine weather. Long summer.",
        6: "Fantastic weather! Great year!",
    }
    print(weather_events[NW])
    input("(Press Enter to continue)")

def display_summary():
    """
    Display a summary of the player's status at the end of the year.
    """
    print("\033c", end="")  # Clear screen
    print("Summary")
    print("Nobles   Soldiers   Merchants   Serfs   Land    Palace")
    print("-" * 50)

    for i in range(1, 7):
        if A[i][0] != 0:  # If the player is active
            print(f"{Z[i][A[i][17]]} {Z[i][0]} of {Z[i][1]}:")
            print(
                f"{A[i][18]:>4} {A[i][15]:>10} {A[i][7]:>10} "
                f"{A[i][3]:>10} {A[i][1]:>8} {A[i][16] * 10:>6}%"
            )

    input("(Press Enter to continue)")

def plague_event():
    """
    Simulate a plague event affecting the current player.
    """
    global A, K
    print("\033c", end="")  # Clear screen
    print(" " * 22 + "P L A G U E  ! ! !")
    print("\nBlack death has struck your nation.\n")

    deaths_serfs = int(random.randint(0, A[K][3] // 2))
    A[K][3] -= deaths_serfs
    print(f"{deaths_serfs} serfs died.")

    deaths_merchants = int(random.randint(0, A[K][7] // 3))
    A[K][7] -= deaths_merchants
    print(f"{deaths_merchants} merchants died.")

    deaths_soldiers = int(random.randint(0, A[K][15] // 3))
    A[K][15] -= deaths_soldiers
    print(f"{deaths_soldiers} soldiers died.")

    deaths_nobles = int(random.randint(0, A[K][18] // 3))
    A[K][18] -= deaths_nobles
    print(f"{deaths_nobles} nobles died.")

    input("(Press Enter to continue)")

def check_game_over():
    """
    Determine if all players are eliminated or one player has won.
    """
    active_players = [i for i in range(1, 7) if A[i][0] != 0]
    if len(active_players) == 0:
        print("\nAll nations have collapsed. The game is over.")
        return True
    if len(active_players) == 1:
        winner = active_players[0]
        print(f"\nGame over! {Z[winner][A[winner][17]]} {Z[winner][0]} of {Z[winner][1]} is victorious!")
        return True
    return False

def end_turn():
    """
    Handle end-of-turn events like plagues and starvation.
    """
    if random.random() < 0.02:  # 2% chance of plague
        plague_event()

    # Additional end-turn checks can be added here.
    return check_game_over()

# Main Game Loop
if __name__ == "__main__":
    initialize_game()
    game_over = False
    while not game_over:
        process_weather_event()
        display_summary()
        # Placeholder for additional actions, like attacking or trading.
        game_over = end_turn()
    print("\nThank you for playing E M P I R E!")
