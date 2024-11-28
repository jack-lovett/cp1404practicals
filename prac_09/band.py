"""CP1404 Practical 9"""

class Band:
    """A collection of musicians."""

    def __init__(self, name):
        """Band constructor."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician."""
        self.musicians.append(musician)

    def play(self):
        """Play musicians."""
        for musician in self.musicians:
            print(musician.play())

    def __str__(self):
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"
