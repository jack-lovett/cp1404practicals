"""Password length w/ error checking"""

PASSWORD_LENGTH = 4


def main():
    password = get_password()
    print_stars(len(password))


def print_stars(number):
    print("*" * number)


def get_password():
    password = input("Enter a password: ")
    while len(password) < PASSWORD_LENGTH:
        print(f"Password needs to be at least {PASSWORD_LENGTH} characters long.")
        password = input("Enter a password: ")
    return password


if __name__ == '__main__':
    main()
