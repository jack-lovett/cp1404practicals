"""CP1404 Practical - Guitar test"""
from prac_06.guitar import Guitar

geetar = Guitar("Geetar 3x3", 2000, 400)

print(f"{geetar.name} get_age(), Expected: 24. Got {geetar.get_age()} ")
print(f"{geetar.name} is_vintage(), Expected: False. Got {geetar.is_vintage()} ")
