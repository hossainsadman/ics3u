"""
Trigonometry Calculator: Sine and Cosine Law
Template by: Mr Cho

"""

__author__ = 'Hossain, Sadman'

# import statement
from math import sin, cos, asin, acos, degrees, radians, inf, sqrt


###--- define trig functions in degrees ---###
###--- don't change!                    ---###
def sin_(x):
    return sin(radians(x))


def cos_(x):
    return cos(radians(x))


def asin_(x):
    return degrees(asin(x))


def acos_(x):
    return degrees(acos(x))


###--- functions for menus: don't change!   ---###
###--- may change some text that is printed ---###
###--- add descriptions, etc.               ---###

def main_menu():
    """Execute main menu."""
    
    while True:
        print("""
  Trigonometry Calculator (uses degrees)
  -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

  Choose an option:

  1. Sine Law Calculator
  2. Cosine Law Calculator

  3. Exit Program

    """) 
        choice = input('> ') # can change this
        if choice == '1':
            sine_law_menu()
        elif choice == '2':
            cosine_law_menu()
        elif choice == '3':
            print('\nTrigonometry Calculator: TERMINATED') # change this
            break
        else:
            print('\nInvalid input.') # can change this


# runs sine law calculator
def sine_law_menu():
    """Execute cosine law menu."""
    
    while True:
        print("""
    Sine Law Calculator
    /\/\/\/\/\/\/\/\/\/

    Choose an option:

    1. (AAS) (solve for side b)
    2. (SSA) (solve for angle B)
    
    3. Exit to Main Menu

    """)
        choice = input('  > ') # can change this
        if choice == '1':
            sine_law_AAS()
        elif choice == '2':
            sine_law_SSA()
        elif choice == '3':
            break
        else:
            print('\nInvalid input.') # can change this

# runs cosine law calculator
def cosine_law_menu():
    """Execute cosine law menu."""

    while True:
        print("""
    Cosine Law Calculator
    \/\/\/\/\/\/\/\/\/\/\

    Choose an option:

    1. (SAS) (solve for side c)
    2. (SSS) (solve for angle C)

    3. Exit to Main Menu

    """)
        choice = input('  > ') # can change this
        if choice == '1':
            cosine_law_SAS()
        elif choice == '2':
            cosine_law_SSS()
        elif choice == '3':
            break
        else:
            print('\nInvalid input.') # can change this


#####################################
###--- complete the code below ---###
#####################################

def wait():
    """A simple function to pause the output."""
    
    input('\nPress enter to continue...\n') # can change the message

def separator():
    """Prints a line of 15 hyphens. Used to separate input and output values."""
    print("-"*15)
            
# fail-safe floating-point input function(s)

    # write your code here
def get_float(msg: str, lower: float, upper: float, error_msg: str) -> float:
    """General method for getting float input with upper and lower bounds."""
    while True:
        try:
            value = float(input(msg))
            if lower < value < upper:
                return value
            print(error_msg)
        except ValueError:
            print(error_msg)

def get_angle(msg: str) -> float:
    """Get angle between 0 & 180 degrees, exclusive."""
    return get_float(msg, 0, 180, "Invalid input.")

def get_side(msg: str) -> float:
    """Get side greater than 0."""
    return get_float(msg, 0, float('inf'), "Invalid input.")

## You MUST take inputs in the order as described
## in the Menu Structure drawing (see Assignment)

def sine_law_AAS():
    """Execute Sine Law (AAS) code."""
    angle_A = get_angle("Angle A: ")
    angle_B = get_float("Angle B (must be less than {}\xb0): ".format(180-angle_A), 0, 180-angle_A, "Invalid input.")

    side_a = get_side("Side a: ")
    separator()

    side_b = side_a * sin_(angle_B) / sin_(angle_A)
    print("Side b: {:.2f}".format(side_b))


def sine_law_SSA():
    """Execute Sine Law (SSA) code."""
    side_a = get_side("Side a: ")
    side_b = get_side("Side b: ")
    angle_A = get_angle("Angle A: ")
    separator()

    height = side_b*sin_(angle_A)

    if angle_A < 90 and side_a < height or angle_A >= 90 and side_a <= side_b:
        print("There is no valid solution for angle B with these input values.")
        return

    angle_B = asin_(height / side_a)

    if angle_A < 90 and height < side_a < side_b:
        print("Angle B: {:.1f}\xb0 or {:.1f}\xb0".format(angle_B, 180 - angle_B))
        return

    print("Angle B: {:.1f}\xb0".format(angle_B))


def cosine_law_SAS():
    """Execute Cosine Law (SAS) code."""
    side_a = get_side("Side a: ")
    side_b = get_side("Side b: ")
    angle_C = get_angle("Angle C: ")
    separator()

    side_c = sqrt(side_a**2 + side_b**2 - 2*side_a*side_b*cos_(angle_C))
    print("Side c: {:.2f}".format(side_c))


def cosine_law_SSS():
    """Execute Cosine Law (SSS) code."""
    side_a = get_side("Side a: ")
    side_b = get_side("Side b: ")
    side_c = get_side("Side c: ")
    separator()

    if side_a + side_b < side_c or side_a + side_c < side_b or side_b + side_c < side_a:
        print("Invalid input: sum of any 2 sides must be greater than 3rd side.")
        return

    angle_C = acos_((side_a**2 + side_b**2 - side_c**2) / (2*side_a*side_b))
    print("Angle C: {:.1f}\xb0".format(angle_C))


##########################
###--- main program ---###
##########################

if __name__ == '__main__':
    main_menu()