"""
Number sequence generator
"""

menu = """1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
4. Exit the program"""

print(menu)
choice = int(input(">>> "))
while choice != 4:
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    if choice == 1:
        if x % 2 == 1:
            x += 1
        for i in range(x, y + 1, 2):
            print(i, end=" ")
    elif choice == 2:
        if x % 2 == 0:
            x += 1
        for i in range(x, y + 1, 2):
            print(i, end=" ")
    elif choice == 3:
        for i in range(x, y + 1):
            print(i ** 2, end=" ")
    else:
        print("Invalid input")
    print()
    print(menu)
    choice = int(input(">>> "))
