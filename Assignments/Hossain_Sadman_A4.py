"""Assignment04: Lists, Functions, and the Function Design Recipe

Complete the code below as required with proper formatting.

Instructions follow the format #n.

NOTE: Calculate a grade point average according to:
        90 to 100: 4.0;
        80 to <90: 3.8;
        70 to <80: 3.4;
        60 to <70: 2.8;
        50 to <60: 2.0;
        <50: 1.0


When completed correctly, the output should appear exactly as below.

DO NOT alter the main() function, but definitely read it to aid you in
completing the function code.

<BEGIN SAMPLE OUTPUT>

    Average and GPA Calculator Demonstration

    Enter 5 marks between 0 and 100:
    > 90,0
    Invalid input...
    > 90.0
    > 76.8
    > 88.8
    > 59
    > 78

    You entered:
    mark 1: 90.0%
    mark 2: 76.8%
    mark 3: 88.8%
    mark 4: 59.0%
    mark 5: 78.0%

    Marks below 60:
    59.0%

    Your average mark: 78.5%

    Your GPA: 3.4

<END SAMPLE OUTPUT>

"""


__author__ = "S Hossain"


#1 Complete the HEADER of this function including type contract.
def get_float(msg: str) -> float:
    """Return a float gotten from the user with input message msg.

    Validate input so that only floats are accepted."""

    while True:
        try:
            x = float(input(msg))
            return x
        except ValueError:
            print('Invalid input...')
            

#2 Complete the DESCRIPTION of this function (no EXAMPLES given or necessary).
def get_list_of_float(n: int) -> [float]:
    """Return a list of floats inputted from user."""
    
    floats = []
    for i in range(n):
        floats.append(get_float('> '))
    return floats


#3 Complete the BODY of this function.
def average(nums: list) -> float:
    """Return the average of the values in nums.

    >>> average([4, 5])
    4.5
    >>> average([3.14, 2.78, 1.61])
    2.51
    >>> average([])
    0
    """

    sum = 0
    for num in nums:
        sum += num
    try:
        return sum / len(nums)
    except ZeroDivisionError:
        return 0


#4 Complete the EXAMPLES of this function.
def print_marks(marks: [float]):
    """Print the marks in marks nicely labelled with ordinal numbers.

    >>> print_marks([10, 20, 30])
    mark 1: 10%
    mark 2: 20%
    mark 3: 30%
    >>> print_marks([])
    No marks!
    """

    size = len(marks)
    if size > 0:
        for i in range(size):
            print('mark {}: {}%'.format(i+1, marks[i]))
    else:
        print('No marks!')


#5 Complete the HEADER, EXAMPLES, and BODY of this function.
def print_marks_below(marks: [float], cutoff):
    """Print only the marks in marks that are strictly less than cutoff.

    >>> print_marks_below([50, 60, 70, 90], 65)
    Marks below 65:
    50%
    60%
    >>> print_marks_below([70, 80]), 80)
    Marks below 80:
    70%
    """

    print("Marks below {}:".format(cutoff))
    for mark in marks:
        if mark < cutoff:
            print("{}%".format(mark))

    
#6 Complete the DESCRIPTION, EXAMPLES, and BODY of this function.
def calculate_gpa(mark: float) -> float:
    """Return the gpa of mark.

    >>> calculate_gpa(90)
    4.0
    >>> calculate_gpa(30.5)
    1.0
    """

    if mark >= 90:
        return 4.0
    elif mark >= 80:
        return 3.8
    elif mark >= 70:
        return 3.4
    elif mark >= 60:
        return 2.8
    elif mark >= 50:
        return 2.0
    return 1.0

#7 DO NOT ALTER ANY CODE BELOW THIS LINE
def main():    
    NUM_MARKS = 5
    print('Average and GPA Calculator Demonstration\n')
    print('Enter', NUM_MARKS, 'marks between 0 and 100:')
    marks = get_list_of_float(NUM_MARKS)
    print('\nYou entered:')
    print_marks(marks)
    cut = 60
    print()
    print_marks_below(marks, cut)

    avg = average(marks)
    print('\nYour average mark: {:.1f}%'.format(avg))
    
    gpa = calculate_gpa(avg)
    print('\nYour GPA: {}'.format(gpa))
    

if __name__ == '__main__':
    main()
