'''
    Program: Magical Calculator
    Author: Ben P
    Copyright: 2017

'''


import re

print("Je suis un calculator")
print("Welcome to hell")
print("Type 'quit' to exit\n")

previous = 0
run = True


def performmath():
    global run
    global previous
    equation = ""

    # If there has been a previous calculation
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

        # if user quits
    if equation == 'quit':
        print("Goodbye, human scum!")
        run = False
    else:
        equation = re.sub('[a-zA-z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    performmath()
