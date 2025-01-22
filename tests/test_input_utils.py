import unittest
from unittest.mock import patch
from input_utils import get_selection

class TestInputUtils(unittest.TestCase):
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
