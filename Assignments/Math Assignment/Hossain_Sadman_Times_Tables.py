'''
Program Name: Times Table Displayer
Purpose: displays a multiplication table for 2 inputted
         positive integers 
Author: Sadman Hossain
'''

# constant integer FW represents the number of field widths to use
# when printing out numbers of the multiplication tables
FW = 5

# while loop continues until a positive integer less than 16 &
# a positive integer less than 21 are inputted
while True:
    
    try:
        # get first integer from user;  represents number of columns
        # in multiplication table
        columns = int(input("Enter a positive integer (less than 16): "))
        # if inputted number is a positive integer but not between 1 &
        # 15,  the while loop will go back to the top & run again
        if columns < 1 or columns > 15:
            print("Input must be a positive integer less than 16!")
            continue

        # get second integer from user;  represents number of rows in
        # multiplication table
        rows = int(input("Enter another positive integer (less than 21): "))
        # if inputted number is a positive integer but not between 1 &
        # 20,  the while loop will go back to the top & run again
        if rows < 1 or rows > 20:
            print("Input must be a positive integer less than 21!")
            print("Try entering both numbers again.")
            continue
        # exit while loop if both inputs are valid
        break

    # if any inputs are not integers,  display message to user stating
    # they did not input an integer
    except ValueError:
        print("Not an integer! Try again.\n")

# displays 4 spaces on the same line for column headers
print(" " * 4, end = "")
# for loop iterates through the number of columns
for i in range(1, columns + 1):
    # prints column header displaying number of each column (with a field
    # width declared at beginning of program) on the same line
    print("{:{width}}".format(i, width = FW), end = "")
print("")

# displays 4 spaces on the same line
print(" " * 4, end = "")
# for loop iterates through the total number of spaces occupied by the
# column headers (number of spaces for each number is equal to the field width 
# declared at beginning of program) excluding the first 4 spaces
for i in range(1, columns * FW + 1):
    print("-", end = "")
print("")    

# parent for loop iterates up to second integer inputted;  goes through 
# each row of the multiplication table
for i in range(1, rows + 1):
    # prints row header displaying number of row (with a field width
    # of 2 place values) mutliplication table
    print("{:{width}} |".format(i, width = 2), end = "")
    # nested for loop iterates up to first integer inputted;  goes through
    # each column of the multiplication table
    
    for j in range(1, columns + 1):
        # display the product of the respective row number multiplied by the
        # respective column number (with a field width of 5 place values)
        print("{:{width}}".format(i*j, width = FW), end = "")
    # print statement goes to next row of the multiplication table
    print("")