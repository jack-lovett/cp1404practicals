"""
CP1404/CP5632 - Practical
Reading files
"""
from prac_03.string_formatting import number

# 1.
name = input("What is your name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", 'r')
name = in_file.read().strip()
print(f"Hi {name}!")
in_file.close()

# 3.
with open("numbers.txt", 'r') as file:
    number_sum = 0
    number_sum += int(file.readline())
    number_sum += int(file.readline())
print(number_sum)

# 4.
with open("numbers.txt", 'r') as file:
    number_sum = 0
    for line in file:
        number_sum += int(line)
print(number_sum)
