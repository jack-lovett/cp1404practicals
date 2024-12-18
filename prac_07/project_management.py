"""
CP1404 Practical
Project Management Program

Estimated completion time: 1 hour
Actual completion time: 1 hour 20 minutes
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
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")
        display_menu()
        choice = input(">>> ").upper()
    save_choice = input(f"Would you like to save to {TXT_FILE}? (Y/N): ").upper()
    if save_choice == "Y":
        save_projects(projects)
    print("Thank you for using Pythonic Project Management.")


def display_menu():
    """Display the main menu options."""
    print("""- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit""")


def load_projects(in_file=TXT_FILE):
    """Load projects from a file."""
    projects = []
    with open(in_file, "r") as file:
        file.readline()  # Skip header row
        for line in file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    print(f"Loaded {len(projects)} projects from {in_file}")
    return projects


def save_projects(projects, out_file=TXT_FILE):
    """Save projects to a file."""
    with open(out_file, "w", encoding="utf-8") as file:
        # Write header row
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.get_start_date().strftime('%d/%m/%Y')}\t"
                f"{project.priority}\t{project.cost_estimate}\t"
                f"{project.completion_percentage}\n"
            )


def display_projects(projects):
    """Display incomplete and complete projects."""
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
    """Check if a project is newer than a given date."""
    return project.start_date > date


def filter_projects_by_date(projects):
    """Filter and display projects starting after a given date."""
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


def add_new_project(projects):
    """Add a new project to the list."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    percent_complete = input("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))


def update_project(projects):
    """Update an existing project's details."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_index = int(input("Project choice: "))
    project = projects[project_index]

    percent_complete = input("New Percentage: ").strip()
    priority = input("New Priority: ").strip()

    project.update_project(percent_complete or None, priority or None)


if __name__ == "__main__":
    main()
