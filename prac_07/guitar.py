"""
CP1404 Practical - More Guitars
"""
import csv

CURRENT_YEAR = 2024

CSV_FILE = "guitars.csv"


def main():
    """Guitar """
    guitars = read_guitars()
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name=name, year=year, cost=cost))
        print(f"{name} ({year}) : ${cost:.2f} added.\n")
        name = input("Name: ")
    guitars.sort()

    save_guitars(guitars)
    for guitar in guitars:
        print(guitar)


def read_guitars(in_file=CSV_FILE):
    """Read guitars from csv file and return a list of objects."""
    guitars = []
    with open(CSV_FILE, encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            guitars.append(Guitar(row[0], int(row[1]), float(row[2])))
    return guitars


def save_guitars(guitars, out_file=CSV_FILE):
    """Save guitars to csv file."""
    with open(out_file, mode='w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


class Guitar:
    """Guitar class."""

    def __init__(self, name="", year=0, cost=0.0):
        """Construct Guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        """Get age of guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a guitar is vintage."""
        return self.get_age() >= 50


if __name__ == "__main__":
    main()
