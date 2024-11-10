"""
CP1404 Practical
Project Management Program

Start time: 10:30am
End time:
Estimated completion time: 1 hour
Actual completion time:
"""
import datetime


class Project:
    """Project class."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct project class."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.completion_percentage == 100

    def get_start_date(self):
        return self.start_date
