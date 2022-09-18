# Simple Command Line Claculator

# Import 'math' 'sys' Libraries
import math , sys

# Define Variables
output = 0
num1 = ""
operator = ""
num2 = ""
memStore = "Empty"

# Define Function Listing Function
def abilitiesList():
    print("+ ... Addition")
    print("- ... Subtraction")
    print("* ... Multiplication")
    print("/ ... Division")
    print("Abs ... Absolute Value")
    print("pi ... Returns PI")
    print("sin ... Sine")
    print("cos ... Cosine")
    print("tan ... Tangent")
    print("exit ... Finish The Program")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def askForNumInput(textPrompt):
    # Devine local variable
    convertedNum = math.nan

    # Wait for valid numerical input 
    while True:
        num = input(textPrompt)
        try:
            # Try to typecast the input to a float
            float(num)
        except ValueError:
            # Catch the exception if it is not a number
            print("ERROR: Syn: Invalid Num")
        else:
            # Typecasting
            convertedNum = float(num)
            break
    return convertedNum

# While Loop
while True:
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Type 'help' for a list of abilities")
    # Loop for getting operation
    while True:
        operator = input("What operation do you want to perform? ")
        if operator == "help":
            abilitiesList()
        elif operator == "pi":
            print(math.pi)
        # Has the user entered in a valid operator?
        elif operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "Abs" or operator == "sin" or operator == "cos" or operator == "tan":
            break
        elif operator == "exit":
            sys.exit()
        else:
            print("ERROR: Invalid Operator")

    # Loop for 1st number input
    while True:
        num1 = askForNumInput("First Number? ")
        # Catch asin and acos out of bounds error case
        if (operator == "asin" or operator == "acos") and (num1 > 1 or num1 < -1):
            print("ERROR: Math: 'asin' and 'acos' commands only accept inputs in range -1 to +1")
        elif operator == "!" and num1 < 0:
            print("ERROR: Math: Factorials only accept inputs > 0")
        else:
            break

    # Does the operation require a 2nd input?
    if not (operator=="Abs" or operator=="sin" or operator=="cos" or operator=="tan"):
        # Loop for 2nd number input
        while True:
            num2 = askForNumInput("Second Number? ")
            # Catch x/0 error case
            if  operator == "/" and num2 == "0":
                print("ERROR: Math: Canot divide by 0!")
            else:
                break

    # Calculations
    if operator == "+":
        output = num1 + num2
        print("Your Answer: "+str(output))
    elif operator == "-":
        output = num1 - num2
        print("Your Answer: "+str(output))
    elif operator == "*":
        output = num1 * num2
        print("Your Answer: "+str(output))
    elif operator == "/":
        output = num1 / num2
        print("Your Answer: "+str(output))
    elif operator == "Abs":
        output = math.fabs(num1)
        print("Your Answer: "+str(output))
    elif operator == "sin":
        output = math.sin(num1)
        print("Your Answer: "+str(output))
    elif operator == "cos":
        output = math.cos(num1)
        print("Your Answer: "+str(output))
    elif operator == "tan":
        output = math.tan(num1)
        print("Your Answer: "+str(output))
