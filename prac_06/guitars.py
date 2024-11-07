"""
CP1404 Practical - Guitars

Estimated time: 20 minutes
Start time: 9:51am
End time: 10:14am
Completion time: 23 minutes
"""
from prac_06.guitar import Guitar

print("My guitars!")

guitars = []

name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name=name, year=year, cost=cost))
    print(f"{name} ({year}) : ${cost:.2f} added.\n")
    name = input("Name: ")

print("These are my guitars:")
for i, guitar in enumerate(guitars, start=1):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
