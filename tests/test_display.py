import unittest
from unittest.mock import patch
from display import display_message, display_list

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
