"""
CP1404 Practical
Project Management Program

Start time: 10:30am
End time:
Estimated completion time: 1 hour
Actual completion time:
"""


class Project:
    """Project class."""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct project class."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage
