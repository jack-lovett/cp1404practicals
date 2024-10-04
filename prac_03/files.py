"""
CP1404/CP5632 - Practical
Reading files
"""

# 1.
name = input("What is your name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()
