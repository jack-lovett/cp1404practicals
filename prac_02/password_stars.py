"""CP1404 Practical 2
Password length w/ error checking"""

PASSWORD_LENGTH = 4


def main():
    """Password length main function"""
    password = get_password(PASSWORD_LENGTH)
    print_stars(len(password))


def print_stars(number):
    """Print number of stars equal to parameter"""
    print("*" * number)


def get_password(length):
    """Get valid password"""
    password = input("Enter a password: ")
    while len(password) < length:
        print(f"Password needs to be at least {length} characters long.")
        password = input("Enter a password: ")
    return password


if __name__ == '__main__':
    main()
