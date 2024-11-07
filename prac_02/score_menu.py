"""CP1404 Practical 2
Score program with menu"""

from score import get_valid_score, determine_result
from password_stars import print_stars

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Score menu main function"""
    score = get_valid_score()
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != 'Q':
        if menu_choice == 'G':
            score = get_valid_score()
        elif menu_choice == 'P':
            print(determine_result(score))
        elif menu_choice == 'S':
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        menu_choice = input(">>> ").upper()
    print("Farewell!")


main()
