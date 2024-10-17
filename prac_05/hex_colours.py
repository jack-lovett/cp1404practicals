"""
CP1404/CP5632 Practical
Hex colours
"""

COLOUR_TO_HEX = {"Amber": "#ffbf00", "Alizarin Crimson": "#e32636", "Asparagus": "#87a96b", "Bitter Lime": "#bfff00",
                 "BlueViolet": "#8a2be2", "Bright Lilac": "#d891ef", "Brilliant Rose": "#ff55a3", "Buff": "#f0dc82",
                 "Light Periwinkle": "#c5cbe1", "Medium Candy Apple Red": "#e2062c"}

colour = input("Enter the colour: ").strip().title()
while colour != "":
    if colour in COLOUR_TO_HEX:
        print(COLOUR_TO_HEX[colour])
    else:
        print("Unknown colour")
    colour = input("Enter the colour: ").strip().title()
