"""
CP1404 Practical
Project Management Program

Estimated completion time: 1 hour
Actual completion time: 1 hour 20 minutes
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
        """Return a string representation of the project."""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Define less-than comparison based on project priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Check if the project is complete."""
        return self.completion_percentage == 100

    def get_start_date(self):
        """Return the start date of the project."""
        return self.start_date

    def update_project(self, completion_percentage=None, priority=None):
        """Update the project's completion percentage and/or priority."""
        if completion_percentage is not None:
            self.completion_percentage = int(completion_percentage)
        if priority is not None:
            self.priority = int(priority)
