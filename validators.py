"""Validated console input helpers."""


def get_float(prompt, minimum=0):
    while True:
        try:
            value = float(input(prompt))
            if value < minimum:
                print(f"Please enter a number that is at least {minimum}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_int(prompt, minimum=0):
    while True:
        try:
            value = int(input(prompt))
            if value < minimum:
                print(f"Please enter a whole number that is at least {minimum}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_name(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")
