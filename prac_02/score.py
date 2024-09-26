"""
CP1404/CP5632 - Practical
Working program to determine score status
"""
import random


def main():
    score = get_valid_score()
    print(determine_result(score))

    random_score = random.randrange(0, 100)
    print(determine_result(random_score))


def get_valid_score():
    score = float(input("Enter score: "))
    while score > 100 or score < 0:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def determine_result(score):
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
