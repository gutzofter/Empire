def get_selection(prompt, min_value=None, max_value=None, choices=None):
    while True:
        try:
            if choices:
                print(prompt)
                for i, choice in enumerate(choices, start=1):
                    print(f"{i}) {choice}")
                min_value, max_value = 1, len(choices)
                prompt = "Select an option: "
            value = int(input(prompt))
            if min_value is not None and (value < min_value or value > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
            else:
                return value - 1 if choices else value
        except ValueError:
            print("Invalid input. Please enter a number.")
