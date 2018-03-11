import re

print("I am calculator hear me roar!")
print("Type 'quit' to exit\n")

previous = 0
run = True


def performmath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))
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
