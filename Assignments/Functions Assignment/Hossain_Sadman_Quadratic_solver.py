"""Quadratic Solver Program

Calculates discriminant, number of solutions, and roots of quadratic equations.
"""


__author__ = 'S Hossain'


from math import sqrt


#	constant string holds the unicode representation of the character 2 superscript
SUPERSCRIPT_2 = "\u00B2"


def loop_program():
	'''Reruns main() function if user inputs y; exits program if user inputs any other value'''
	while True:
		rerun = input("\nCheck another number (enter \"y\" for Yes or \"n\" for No)? ")
		if rerun == "y" or rerun == "Y":
			main()
		break


def get_float(msg):
	"""Gets user input after displaying a message (parameter)
	
	Displays error messages and reruns getting an input if user input is not a float
	"""
	while True:
		try:
			num = float(input(msg))
			return num
		except ValueError:
			print("Invalid input. Try again!\n")

def discriminant(a, b, c):
	'''Returns discriminant of a quadratic equation'''
	discr = b**2 - 4*a*c
	return discr


def num_solutions(a, b, c):
	'''Returns the number of solutions to a quadratic equation'''
	discr = discriminant(a, b, c)
	num_sol = 0
	if discr == 0:
		num_sol = 1
	elif discr > 0:
		num_sol = 2
	return num_sol


def solve(a, b, c):
	'''Returns the exact solutions of a quadratic equation'''
	discr = discriminant(a, b, c)
	num_sol = num_solutions(a, b, c)
	try:
		
		if num_sol == 0:
			msg = "There are no solutions."
		elif num_sol == 1:
			root1 = (-1*b) / (2*a)
			msg = "The root is {}.".format(root1)
		elif num_sol == 2:
			root1 = (-1*b + discr) / (2*a)
			root2 = (-1*b - discr) / (2*a)
			msg = "The roots are {} and {}.".format(root1, root2)
		print(msg)	

	#	if a == 0, inputted values do not make a quadratic equation
	except ZeroDivisionError:
		print("Not a quadratic equation!")


def main():
	print("\nEnter the values of a, b, and c from a quadratic equation ax{} + bx + c = 0:".format(SUPERSCRIPT_2))
	a = get_float("a = ")
	b = get_float("b = ")
	c = get_float("c = ")
	#	only prints discriminant and number of solutions if inputs make a valid quadratic equation
	if a != 0:
		print("Discriminant:", discriminant(a, b, c))
		print("# of Solutions:", num_solutions(a, b, c))
	solve(a, b, c)
	loop_program()


if __name__ == '__main__':
    main()
