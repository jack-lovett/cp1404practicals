for i in range(1, 21, 2):
    print(i, end=' ')
print()

# question a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# question b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# question c
number_of_stars = int(input("Number of stars: "))
print("*" * number_of_stars)

# question d
number_of_star_lines = int(input("Number of star lines: "))
for i in range(1, number_of_star_lines + 1):
    print("*" * i)
