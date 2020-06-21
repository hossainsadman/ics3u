'''
Program Name: Quadratic Equation Solver
Purpose: solves for the number and values of real
         roots of inputted quadratic equatioms
Author: Sadman Hossain
'''

from math import sqrt

# constant represents the unicode value for the number 2 in superscript
SUPERSCRIPT_2 = "\u00B2"

print("QUADRATIC SOLVER")

# while loop continues to run until user does not input "y"
# when asked if they want to input another quadratic equation
while True:

    # ask user to input values for quadratic equation
    print("\nEnter the values of a, b, and c from a quadratic equation ax{} + bx + c = 0:".format(SUPERSCRIPT_2))

    # floats for storing a, b, and c values of ax² + bx + c = 0
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    # integers for storing values of each root
    root1 = 0
    root2 = 0

    # strings for storing portion of text message to display when
    # displaying number of roots & value of each root
    num_of_roots_text = ""
    root_values_text = ""

    # if the inputted a value of the quadratic equation is 0, display message
    # to user stating inputted values do not represent a quadratic equation
    # and go to beginning of while loop
    if a == 0:
        print("That's not a quadratic equation! Try again.")
        continue 

    # calculate discriminant of inputted quadratic equation
    discriminant = b**2 - 4 * a * c
    
    if discriminant < 0:
        # assign number of roots string to state that there are no solutions
        num_of_roots_text = "are no solutions"

    elif discriminant == 0:
        # assign number of roots string to state that there is 1 solution
        num_of_roots_text = "is one solution"

        # calculate the x-value for only 1 root
        root1 = (-1 * b + sqrt(discriminant)) / (2*a)
        # assign value of roots string to only contain the value of the 
        # calculated root
        root_values_text = "The root is {:.2f}.".format(root1)

    elif discriminant > 0:
        # assign number of roots string to state that there are 2 solutions
        num_of_roots_text = "are two solutions"
        
        # calculate x-values for each of the roots using the quadratic equation
        root1 = (-1 * b + sqrt(discriminant)) / (2*a) 
        root2 = (-1 * b - sqrt(discriminant)) / (2*a)
        # assign value of roots string to contain values of both roots
        root_values_text = "The roots are {:.2f} and {:.2f}.".format(root1, root2)
    
    # display the number of roots
    print("\nThere {}.".format(num_of_roots_text))
    # display the value of each root only if the discriminant is non-negative
    # (as in, if the quadratic equation does not have 0 roots)
    if discriminant >= 0:
        print(root_values_text)

    # default state of whether the user wants to input values of another
    # equation is false
    try_again = False

    # while loop continues to ask whether user will input another set of values
    # until a valid input of yes ("y" or "Y") or no ("n" or "N") is inputted
    while True:
        
        # get user input of whether to reiterate while loop & input more values
        request = input("\nAnother? (y)es or (n)o: ")
        
        # if user input is yes,  program breaks out of while loop and boolean
        # representing if user will input more values is assigned to True
        if request == "y" or request == "Y":
            try_again = True
            break
        # if user input is no,  program breaks out of while loop and boolean 
        # representing if user will input more values stays False
        elif request == "n" or request == "N":
            break
        # if user input is not an accepted input representing yes or no, 
        # display message asking to try inputting again and while loop
        # continues to iterate w/o break statement
        else:
            print("Invalid input. Try again.")

    # if user input in previous loop is yes, continue statement causes
    # program control flow to go to start of parent while loop
    if try_again == True:
        continue
    # if user input in previous loop is not yes,  break out of while loop
    # to display good-bye message
    else:
        break

print("\nThanks for using QUADRATIC SOLVER.")
print("Good-bye!")