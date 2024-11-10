"""
CP1404 Practical - More Guitars
"""
CURRENT_YEAR = 2024


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
