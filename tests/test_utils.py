import unittest
from unittest.mock import patch
from utils import get_selection, display_message, display_list


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
