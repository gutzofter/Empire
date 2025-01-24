from unittest.mock import patch

def get_user_input():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    return name, age

def test_get_user_input():
    inputs = iter(["Alice", "30"])
    with patch('builtins.input', side_effect=lambda: next(inputs)):
        name, age = get_user_input()
        assert name == "Alice"
        assert age == "30"

test_get_user_input()
