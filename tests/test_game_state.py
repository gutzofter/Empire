import unittest
from game_state import GameState

class TestGameState(unittest.TestCase):
    def test_initialization(self):
        game_state = GameState(2)
        # Ensure the correct number of players and barbarians
        self.assertEqual(len(game_state.players), 6)
        self.assertEqual(game_state.barbarian_land, 6000)
        # Verify active/inactive players
        self.assertTrue(game_state.players[0]["active"])
        self.assertFalse(game_state.players[5]["active"])
        # Check player properties
        self.assertEqual(game_state.players[0]["land"], 10000)
        self.assertEqual(game_state.players[0]["grain_reserve"], 15000)
