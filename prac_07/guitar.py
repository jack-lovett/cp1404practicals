"""
CP1404 Practical - Guitar

Start time: 9:51am
End time: 10:24am
Completion time: 33 minutes
"""
import csv

CURRENT_YEAR = 2024

IN_FILE = "guitars.csv"


def main():
    guitars = read_guitars()
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def read_guitars(in_file=IN_FILE):
    guitars = []
    with open(IN_FILE, encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            guitars.append(Guitar(row[0], int(row[1]), float(row[2])))
    return guitars


class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= 50


if __name__ == "__main__":
    main()
