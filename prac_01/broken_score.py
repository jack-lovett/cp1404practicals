"""
CP1404/CP5632 - Practical
Working program to determine score status
"""

score = float(input("Enter score: "))
if score > 100 or score < 0:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
