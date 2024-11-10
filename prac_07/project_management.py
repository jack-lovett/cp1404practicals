"""
CP1404 Practical
Project Management Program

Start time: 10:30am
End time:
Estimated completion time: 1 hour
Actual completion time:
"""

TXT_FILE = "projects.txt"


def main():
    """Pythonic Project Manager main function."""
    print("Welcome to Pythonic Project Management")
    # load_projects()
    display_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            # load_projects
            pass
        elif choice == "S":
            # save_projects
            pass
        elif choice == "D":
            # display_projects
            pass
        elif choice == "F":
            # filter
            pass
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


if __name__ == "__main__":
    main()
