import unittest
from unittest.mock import patch, MagicMock
from main import main
from game_state import GameState

class TestMain(unittest.TestCase):

    @patch('builtins.input', side_effect=['2'])
    @patch('main.clear_screen')
    @patch('main.process_weather_event')
    @patch('main.display_summary')
    @patch('main.display_land_holdings')
    @patch('main.player_turn')
    @patch('main.check_game_over', side_effect=[False, True])
    def test_main(self, mock_check_game_over, mock_player_turn, mock_display_land_holdings, mock_display_summary, mock_process_weather_event, mock_clear_screen, mock_input):
        with patch('main.GameState', return_value=MagicMock(num_players=2, current_year=0, players=[{"active": True}, {"active": True}], barbarian_land=0)) as mock_game_state:
            main()
            mock_clear_screen.assert_called_once()
            mock_input.assert_called_once_with("How many people are playing? (1-6): ")
            mock_process_weather_event.assert_called()
            mock_display_summary.assert_called()
            mock_display_land_holdings.assert_called()
            mock_player_turn.assert_called()
            mock_check_game_over.assert_called()

if __name__ == "__main__":
    unittest.main()
