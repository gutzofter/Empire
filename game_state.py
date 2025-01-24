class GameState:
    def __init__(self, num_players):
        self.current_year = 0
        self.players = []
        self.barbarian_land = 6000
        self.num_players = num_players
        self.current_player_index = 0

        for i in range(num_players):
            ruler_name = input(f"Who is the ruler of Land {i + 1}? ")
            ruler_title = input(f"What is the ruler's title (e.g., King, Queen) for Land {i + 1}? ")
            self.players.append({
                "active": True,
                "land": 10000,
                "grain_reserve": 15000,
                "serfs": 2000,
                "treasury": 1000,
                "merchants": 25,
                "soldiers": 20,
                "palace_completion": 0,
                "ruler_name": ruler_name,
                "ruler_title": ruler_title
            })

        for _ in range(num_players, 6):
            self.players.append({
                "active": False,
                "land": 0,
                "grain_reserve": 0,
                "serfs": 0,
                "treasury": 0,
                "merchants": 0,
                "soldiers": 0,
                "palace_completion": 0,
                "ruler_name": None,
                "ruler_title": None
            })
