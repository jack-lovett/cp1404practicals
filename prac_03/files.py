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
    number_sum = 0
    for i, line in enumerate(file):
        if i == 2:
            break
        number_sum += int(line)
print(number_sum)

# 4.
with open("numbers.txt", 'r') as file:
    number_sum = 0
    numbers = file.read()
    number_list = numbers.split('\n')
    for number in number_list:
        number_sum += int(number)
print(number_sum)
