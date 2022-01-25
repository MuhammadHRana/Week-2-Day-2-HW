# PROBLEM #1
# 1) Build a Shopping Cart
# Should have the following capabilities:

    # 1) Takes in input
    # 2) Stores user input into a list
    # 3) User can add or delete items
    # 4) User can see current shopping list
    # 5) Loops until user 'quits'
    # 6) Upon quiting the program, print out all items in the user's list

# List = []
# def shopping(item):
#     if item == str("Yes"):
#         Addition = input("What would you like to add? ")
#         List = List.append(Addition)
#         Again = input("What would you like to add? ")
#         if Again == str("Yes"):
#             Addition = input("What would you like to add? ")
#     elif item == str("No"):
#         return List
#     else:
#         print("Incorrect input. ")
#         return shopping(item)

# shopping(input('Would you like to add an item to your cart? (Yes/No) '))


def shopping(item):
    List = {}
    x = 0
    if item == str("Yes"):
        x += 1
        Addition = input("What would you like to add? ")
        List[f'Item {x}'] = Addition
        print(List)
        Again = input("Would you like to continue adding? ")
        if Again == str("Yes"):
            x += 1
            Addition = input("What would you like to add? ")
            List[f'Item {x}'] = Addition
            print(List)
            return shopping(input('Would you like to add an item to your cart? (Yes/No) '))
        elif item == str("No"):
            return List
        else:
            print("Incorrect input. ")
            return shopping(item)
    elif item == str("No"):
        return List
    else:
        print("Incorrect input. ")
        return shopping(item)

shopping(input('Would you like to add an item to your cart? (Yes/No) '))


# END PROBLEM #1


# PROBLEM #2

# 2) Create a Module in Visual Studio Code and Import It
# Module should have the following capabilities:

# 1) Has a function to calculate the square footage of a room
# 2) Has a function to calculate the circumference of a circle

# Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage

# **Note: When using functions in Python, arguments are passed in by reference, NOT value.


# from math import pi


# def mathematics():
#     Function_Type = input("Do you want to calculate the square footage or circumference? (square/circle) ").lower()
#     if Function_Type == 'square':
#         Side = input("What is the side equal too? (int only) ")
#         length = float(Side)
#         if isinstance(float(length), float):
#             return length ** 2
#         else:
#             return "Error. Did not follow instructions."
#     elif Function_Type == 'circle':
#         Side = input("What is the radius equal too? (int only) ")
#         radius = float(Side)
#         if isinstance(float(radius), float):
#             return 2 * pi * radius
#         else:
#             return "Error. Did not follow instructions."
# mathematics()

# %run 'FILENAME.EXTENSION'    ---> TO ACCESS MODULE IN JUPYTER
# from FILENAME import FUNCTION

from math_calculator import mathematics

print(f'This is my calculation {mathematics()}')


# END PROBLEM #2