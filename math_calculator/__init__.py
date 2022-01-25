from math import pi

def mathematics():
    Function_Type = input(
        "Do you want to calculate the square footage or circumference? (square/circle) ").lower()
    if Function_Type == 'square':
        Side = input("What is the side equal too? (int only) ")
        length = float(Side)
        if isinstance(float(length), float):
            return length ** 2
        else:
            return "Error. Did not follow instructions."
    elif Function_Type == 'circle':
        Side = input("What is the radius equal too? (int only) ")
        radius = float(Side)
        if isinstance(float(radius), float):
            return 2 * pi * radius
        else:
            return "Error. Did not follow instructions."
