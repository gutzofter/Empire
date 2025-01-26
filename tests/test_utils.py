import unittest
from unittest.mock import patch
from utils import get_selection, display_message, display_list, display_battle_results, display_land_holdings, display_summary, display_weather_event, display_plague_event, clear_screen


class TestDisplay(unittest.TestCase):
    @patch("builtins.print")
    def test_display_message(self, mock_print):
        display_message("Hello, world!")
        mock_print.assert_called_once_with("Hello, world!")

    @patch("builtins.print")
    def test_display_list(self, mock_print):
        display_list("Options:", ["Option 1", "Option 2"])
        mock_print.assert_any_call("Options:")
        mock_print.assert_any_call("1) Option 1")
        mock_print.assert_any_call("2) Option 2")

    @patch("builtins.print")
    def test_display_battle_results(self, mock_print):
        attacker = {"ruler_name": "Attacker", "ruler_title": "King"}
        defender = {"ruler_name": "Defender", "ruler_title": "Queen"}
        display_battle_results(attacker, defender, 50, 100)
        mock_print.assert_any_call("Battle Results:\n")
        mock_print.assert_any_call("Attacker King attacked Defender Queen.")
        mock_print.assert_any_call("Attacker losses: 50 soldiers.")
        mock_print.assert_any_call("Defender losses: 100 soldiers.")
        mock_print.assert_any_call("Attacker King is victorious!")

    @patch("builtins.print")
    def test_display_land_holdings(self, mock_print):
        players = [{"ruler_title": "King", "ruler_name": "Arthur", "land": 100, "active":True}]
        display_land_holdings(players, 50)
        mock_print.assert_any_call("Land Holdings:")
        mock_print.assert_any_call("1) Barbarians: 50 acres")
        mock_print.assert_any_call("2) King Arthur controls 100 acres")

    @patch("builtins.print")
    def test_display_summary(self, mock_print):
        players = [{"ruler_name": "Arthur", "ruler_title": "King", "nobles": 10, "soldiers": 20, "merchants": 30, "serfs": 40, "land": 50, "palace_completion": 0.5, "active": True}]
        display_summary(players)
        mock_print.assert_any_call("Summary")
        mock_print.assert_any_call("Nobles   Soldiers   Merchants   Serfs   Land    Palace")
        mock_print.assert_any_call("Arthur    King    10      20      30      40      50        50.0%")

    @patch("builtins.print")
    def test_display_weather_event(self, mock_print):
        display_weather_event(2023, "A great storm has passed.")
        mock_print.assert_any_call("Year 2023\n")
        mock_print.assert_any_call("A great storm has passed.")

    @patch("builtins.print")
    def test_display_plague_event(self, mock_print):
        display_plague_event("Arthur", 100, 50, 25, 10)
        mock_print.assert_any_call(" " * 22 + "P L A G U E  ! ! !")
        mock_print.assert_any_call("\nBlack death has struck Arthur's nation.\n")
        mock_print.assert_any_call("100 serfs died.")
        mock_print.assert_any_call("50 merchants died.")
        mock_print.assert_any_call("25 soldiers died.")
        mock_print.assert_any_call("10 nobles died.")

    @patch("builtins.print")
    def test_clear_screen(self, mock_print):
        clear_screen()
        mock_print.assert_called_once_with("\033c", end="")


class TestUtils(unittest.TestCase):
    @patch("builtins.input", side_effect=["2"])
    def test_get_selection_choice(self, mock_input):
        choices = ["Option 1", "Option 2"]
        result = get_selection("Choose an option:", choices=choices)
        self.assertEqual(result, 1)

    @patch("builtins.input", side_effect=["3", "1"])
    def test_get_selection_invalid_choice(self, mock_input):
        choices = ["Option 1", "Option 2"]
        result = get_selection("Choose an option:", choices=choices)
        self.assertEqual(result, 0)  # Second valid input is "1"

    @patch("builtins.input", side_effect=["5"])
    def test_get_selection_numeric_input(self, mock_input):
        result = get_selection("Enter a number:", min_value=1, max_value=10)
        self.assertEqual(result, 5)
