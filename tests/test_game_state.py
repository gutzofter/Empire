import unittest
from unittest.mock import patch
from game_state import GameState


class TestGameState(unittest.TestCase):
    @patch("builtins.input", side_effect=["Alice", "Queen", "Bob", "King"])
    def test_initialization(self, mock_input):
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

    @patch("builtins.input", side_effect=["Alice", "Queen", "Bob", "King"])
    def test_initialization_with_input(self, mock_input):
        game_state = GameState(2)
        # Ensure the correct number of players and barbarians
        self.assertEqual(len(game_state.players), 6)
        self.assertEqual(game_state.barbarian_land, 6000)
        # Verify active/inactive players
        self.assertTrue(game_state.players[0]["active"])
        self.assertTrue(game_state.players[1]["active"])
        self.assertFalse(game_state.players[2]["active"])
        # Check player properties
        self.assertEqual(game_state.players[0]["ruler_name"], "Alice")
        self.assertEqual(game_state.players[0]["ruler_title"], "Queen")
        self.assertEqual(game_state.players[1]["ruler_name"], "Bob")
        self.assertEqual(game_state.players[1]["ruler_title"], "King")
        self.assertEqual(game_state.players[0]["land"], 10000)
        self.assertEqual(game_state.players[0]["grain_reserve"], 15000)
        self.assertEqual(game_state.players[0]["serfs"], 2000)
        self.assertEqual(game_state.players[0]["treasury"], 1000)
        self.assertEqual(game_state.players[0]["merchants"], 25)
        self.assertEqual(game_state.players[0]["soldiers"], 20)
        self.assertEqual(game_state.players[0]["palace_completion"], 0)
        self.assertEqual(game_state.players[0]["nobles"], 25)
        self.assertEqual(game_state.players[0]["army_efficiency"], 1.0)
        self.assertEqual(game_state.players[0]["sales_tax"], 1.0)

        # Check inactive player properties
        self.assertEqual(game_state.players[2]["land"], 0)
        self.assertEqual(game_state.players[2]["grain_reserve"], 0)
        self.assertEqual(game_state.players[2]["serfs"], 0)
        self.assertEqual(game_state.players[2]["treasury"], 0)
        self.assertEqual(game_state.players[2]["merchants"], 0)
        self.assertEqual(game_state.players[2]["soldiers"], 0)
        self.assertEqual(game_state.players[2]["palace_completion"], 0)
        self.assertEqual(game_state.players[2]["nobles"], 0)
        self.assertEqual(game_state.players[2]["army_efficiency"], 0.0)
        self.assertEqual(game_state.players[2]["sales_tax"], 0.0)
        self.assertIsNone(game_state.players[2]["ruler_name"])
        self.assertIsNone(game_state.players[2]["ruler_title"])

if __name__ == "__main__":
    unittest.main()
