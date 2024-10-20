"""
CP1404/CP5632 Practical
Estimated: 20 minutes
Actual: 12 minutes
"""
import csv


def main():
    """Main function for Wimbledon data reader."""
    data = read_wimbledon_data("wimbledon.csv")

    # Process the champions
    champions = get_champions_to_wins(data)
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")

    # Process the countries
    countries = get_countries(data)
    sorted_countries = sorted(countries)
    print(f"These {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))


def read_wimbledon_data(in_file):
    """Read the Wimbledon data from the CSV file."""
    data = []
    with open(in_file) as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip the header row
        for row in reader:
            data.append(row)
    return data


def get_champions_to_wins(data):
    """Return a dictionary of champions and their win counts."""
    champion_to_wins = {}
    for row in data:
        champion = row[2]
        if champion not in champion_to_wins:
            champion_to_wins[champion] = 0
        champion_to_wins[champion] += 1
    return champion_to_wins


def get_countries(data):
    """Return a set of countries that have won Wimbledon."""
    countries = set()
    for row in data:
        countries.add(row[3])
    return countries


main()
