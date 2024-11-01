"""Quick picks generator"""
import random

MINIMUM = 1
MAXIMUM = 45
NUMBER_OF_RANDOM_NUMBERS = 6


def main():
    """Quick picks generator"""
    number_of_quick_picks = int(input("How many quick picks? "))
    display_quick_picks(number_of_quick_picks)


def display_quick_picks(number_of_quick_picks):
    """Display quick picks depending on inputted number"""
    for i in range(number_of_quick_picks):
        print(generate_unique_number_line())


def generate_unique_number_line():
    """Return sorted, formatted list of unique string numbers"""
    possible_numbers = [number for number in range(MINIMUM, MAXIMUM + 1)]
    numbers = []
    for i in range(NUMBER_OF_RANDOM_NUMBERS):
        random_number = random.choice(possible_numbers)
        numbers.append(random_number)
        possible_numbers.remove(random_number)
    numbers.sort()
    number_line = " ".join(f"{number:2}" for number in numbers)
    return number_line


main()
