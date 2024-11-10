"""
CP1404 Practical - More Guitars
"""
import csv

from guitar import Guitar

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


if __name__ == "__main__":
    main()
