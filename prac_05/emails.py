"""
CP1404/CP5632 Practical
Estimated: 10 minutes
Actual: 12 minutes
"""


def main():
    """Main function for email name extractor."""
    email_to_name = {}

    email = input("Email: ").strip()
    while email != "":
        name = extract_name_from_email(email).title()
        correct = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if correct not in ["", "y"]:
            name = input("Name: ").strip().title()

        email_to_name[email] = name
        email = input("Email: ").strip()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """Extracts a name from an email."""
    username = email.split("@")[0]
    parts = username.split(".")
    name = " ".join(parts)
    return name


main()
