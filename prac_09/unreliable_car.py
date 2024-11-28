import random
from car import Car


class UnreliableCar(Car):
    """A Car that does not always drive reliably."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but unreliably."""
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
