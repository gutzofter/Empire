import unittest
from unittest.mock import patch, MagicMock
from game_logic import process_weather_event, player_turn, buy_grain, sell_grain, attack, check_game_over

class TestGameLogic(unittest.TestCase):

    @patch('game_logic.display_weather_event')
    @patch('game_logic.random.randint', return_value=4)  
    def test_process_weather_event(self, mock_randint, mock_display_weather_event):
        game_state = MagicMock()
        game_state.current_year = 1
        process_weather_event(game_state)
        mock_display_weather_event.assert_called_once_with(1, "Average weather. Good year.")

    @patch('game_logic.display_message')
    @patch('game_logic.get_selection', return_value=3)
    def test_player_turn_end_turn(self, mock_get_selection, mock_display_message):
        game_state = MagicMock()
        game_state.players = [{'ruler_title': 'King', 'ruler_name': 'Arthur'}]
        game_state.current_player_index = 0
        player_turn(game_state)
        mock_display_message.assert_called_once_with("King Arthur's turn:")
        mock_get_selection.assert_called_once_with("Choose an action:", choices=["Buy Grain", "Sell Grain", "Attack", "End Turn"])

    @patch('game_logic.display_message')
    @patch('game_logic.get_selection', side_effect=[0, 1])
    def test_buy_grain(self, mock_get_selection, mock_display_message):
        game_state = MagicMock()
        buyer = {'active': True, 'ruler_title': 'King', 'ruler_name': 'Arthur', 'treasury': 100, 'grain_reserve': 0}
        seller = {'active': True, 'ruler_title': 'Queen', 'ruler_name': 'Guinevere', 'grain_reserve': 50, 'sales_tax': 2, 'treasury': 0}
        game_state.players = [buyer, seller]
        buy_grain(game_state, buyer)
        self.assertEqual(buyer['grain_reserve'], 1)
        self.assertEqual(buyer['treasury'], 98)
        self.assertEqual(seller['grain_reserve'], 49)
        self.assertEqual(seller['treasury'], 2)
        mock_display_message.assert_called_with("Transaction complete: Bought 1 bushels for 2 gold.")

    @patch('game_logic.display_message')
    @patch('game_logic.get_selection', return_value=1)
    def test_sell_grain(self, mock_get_selection, mock_display_message):
        game_state = MagicMock()
        seller = {'ruler_title': 'King', 'ruler_name': 'Arthur', 'grain_reserve': 10, 'treasury': 0}
        game_state.players = [seller]
        with patch('game_logic.random.randint', return_value=15):
            sell_grain(game_state, seller)
        self.assertEqual(seller['grain_reserve'], 9)
        self.assertEqual(seller['treasury'], 15)
        mock_display_message.assert_called_with("Sold 1 bushels for 15 gold.")

    @patch('game_logic.display_message')
    @patch('game_logic.get_selection', return_value=0)
    def test_attack_victory(self, mock_get_selection, mock_display_message):
        game_state = MagicMock()
        attacker = {'ruler_title': 'King', 'ruler_name': 'Arthur', 'soldiers': 100, 'army_efficiency': 1, 'land': 10, 'active': True}
        target = {'ruler_title': 'Queen', 'ruler_name': 'Guinevere', 'soldiers': 50, 'army_efficiency': 1, 'land': 20, 'active': True}
        game_state.players = [attacker, target]
        with patch('game_logic.random.randint', return_value=30):
            attack(game_state, attacker)
        self.assertEqual(attacker['land'], 40)
        self.assertEqual(target['land'], -10)
        self.assertFalse(target['active'])
        mock_display_message.assert_any_call("Victory! You gained 30 acres of land.")
        mock_display_message.assert_any_call("Queen Guinevere has been defeated!")

    @patch('game_logic.display_message')
    def test_check_game_over(self, mock_display_message):
        game_state = MagicMock()
        game_state.players = [{'ruler_title': 'King', 'ruler_name': 'Arthur', 'active': True}]
        self.assertTrue(check_game_over(game_state))
        mock_display_message.assert_called_once_with("King Arthur is the ruler of the world!")

if __name__ == '__main__':
    unittest.main()