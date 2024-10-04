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
name = in_file.readline().strip()
print(f"Hi {name}!")
in_file.close()

# 3.
with open("numbers.txt", 'r') as file:
    number_total = 0
    for i, line in enumerate(file):
        if i == 2:
            break
        number_total += int(line)
print(number_total)
