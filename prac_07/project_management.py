"""
CP1404 Practical
Project Management Program

Start time: 10:30am
End time:
Estimated completion time: 1 hour
Actual completion time:
"""
import datetime
from operator import attrgetter

from project import Project

TXT_FILE = "projects.txt"


def main():
    """Pythonic Project Manager main function."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects()
    display_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_projects()
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            # add
            pass
        elif choice == "U":
            # update
            pass
        else:
            print("Invalid choice")
        choice = input(">>> ").upper()


def display_menu():
    """Display menu."""
    print("- (L)oad projects"
          "- (S)ave projects"
          "- (D)isplay projects"
          "- (F)ilter projects by date"
          "- (A)dd new project"
          "- (U)date project"
          "- (Q)uit")


def load_projects(in_file=TXT_FILE):
    """Load projects from a file."""
    projects = []
    with open(in_file, "r") as file:
        file.readline()  # Skip header row
        for line in file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def save_projects(projects, out_file=TXT_FILE):
    with open(out_file, "w", encoding="utf-8") as file:
        # Write header row
        file.write("Name\tStart Dsdate\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date}\t"
                f"{project.priority}\t{project.cost_estimate}\t"
                f"{project.completion_percentage}\n"
            )


def display_projects(projects):
    complete_projects = [project for project in projects if project.is_complete()]
    incomplete_projects = [project for project in projects if not project.is_complete()]

    complete_projects.sort()
    incomplete_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in complete_projects:
        print(f"  {project}")


def is_project_newer(project, date):
    return project.start_date > date


def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    try:
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")
        return

    filtered_projects = [p for p in projects if is_project_newer(p, date)]
    filtered_projects.sort(key=attrgetter('start_date'))
    if filtered_projects:
        for project in filtered_projects:
            print(project)
    else:
        print(f"No projects found after {date_string}.")


if __name__ == "__main__":
    main()
