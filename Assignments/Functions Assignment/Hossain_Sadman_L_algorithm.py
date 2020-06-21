""" Luhn Algorithm Checker and Check-Digit Calculator

Determines if inputted numbers are valid using the Luhn Algorithm and calculates the
appropriate check-digit if they are invalid
"""


__author__ = 'S Hossain'


from math import sqrt


def loop_program():
	'''Reruns main() function if user inputs y; exits program if user inputs any other value'''
	while True:
		rerun = input("\nCheck another number (enter \"y\" for Yes or \"n\" for No)? ")
		if rerun == "y" or rerun == "Y":
			main()
		else:
			break
		break


def strip(string):
	'''Returns a string where all non-numerical characters are eliminated'''
	text = ""
	for i in range(len(string)):
		if string[i] in "0123456789":
			text += string[i]
	return text



def w_sum(number):
	'''Returns the weighted sum of an inputted number using the Luhn Algorithm'''
	sum = 0
	number_reverse = (strip(number))[::-1]
	for i in range(len(number_reverse)):
		if i % 2 != 0:
			digit = int(number_reverse[i]) * 2
		else:
			digit = int(number_reverse[i])
		if digit > 9:
			digit = digit - 9
		sum += digit
	return sum


def check_validity(number):
	'''Returns boolean value of whether inputted number is valid using Luhn Algorithm'''
	validity = False
	if w_sum(number) % 10 == 0:
		validity = True
	return validity


def check_digit(number):
	"""Returns check digit of inputted number
	
	If number is valid, returns the valid check-digit of the number
	If number is invalid, returns a calculated check-digit to be concatenated to input
	"""
	if (check_validity(number)):
		return str(number)[-1:]
	check_digit = 10 - w_sum(number + "0") % 10
	if check_digit == 10:
		check_digit = 0
	return check_digit


def turn_valid(number):
	'''Returns a valid Luhn Algorithm number using an inputted number'''
	if check_validity(number) == True:
		return number
	valid_num = number + str(check_digit(number))
	return valid_num


def main():
	number = input("Enter a number: ")
	print("Number Validity:", check_validity(number))
	if (not check_validity(number)):
		print("New Valid Number:", turn_valid(number))
	print("Check-Digit:", check_digit(number))
	loop_program()


if __name__ == "__main__":
	main()