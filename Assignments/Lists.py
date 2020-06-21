"""List Functions Practice

Practice using lists in functions
"""


__author__ = 'S Hossain'


def get_string_list(n):
    strings = []
    for i in range(n):
        strings.append(input("Enter string: "))
    return strings

def get_int_list(n):
    integers = []
    for i in range(n):
        try:

            integers.append(int(input("Enter integer: ")))
        except ValueError:
            print("Invalid input! Please try again.")
            continue
    return integers

def get_float_list(n):
    floats  = []
    for i in range(n):
        try:

            floats.append(float(input("Enter float: ")))
        except ValueError:
            print("Invalid input! Please try again.")
            continue
    return integers

def mean(num_list):
	sum = 0
	mean = 0
	for num in num_list:
		sum += num
	mean = sum / len(num_list)
	return mean

def lengths_of_strings(string_list):
	lengths = []
	for string in string_list:
		lengths.append(len(string))
	return lengths

def mean_length_of_strings(string_list):
	return mean(lengths_of_strings(string_list))

def count(list, item):
	count = 0
	for thing in list:
		if thing == item:
			count += 1
	return count

def median(num_list):
	length = len(num_list)
	median = 0
	if length % 2 == 0:
		median = (num_list[(int)(length / 2)] + num_list[(int)(length / 2 - 1)]) / 2
		return median
	else:
		median = num_list[(int)((length - 1) / 2)]
		return median

def student_list():
	students = ['a','b','c','d']
	ids = []
	for i in range(len(students)):
		ids.append(i + 1)
	student_list = [students, ids]
	return student_list

def print_student_list(student_list):
	# TBD

def main():
	print(student_list())

if __name__ == '__main__':
    main()

'''Exercises 2.3: Lists
Write the code in a Python module (.py file), not Colab. Do not rely on built-ins, but rather code the algorithms yourself. Document and comment.

Write a function get_string_list(n) which takes an integer n as parameter. The function should ask the user for n strings and add each of them to a list, which is returned. Test the code in the main program by getting a number from the user and calling the function. Usage:
>>> a = get_string_list(3)
spam
cheddar
parrot
>>> a
['spam', 'cheddar', 'parrot']
Write two more functions similar to the previous question: get_int_list(n) and get_float_list(n). Test in the main program. Even better, ensure inputs are validated so that there are no exceptions.
Write a function mean(num_list) which returns the mean, or average, of the values in num_list. 
Write a function lengths_of_strings(string_list) which takes as parameter a list of strings and returns a list which is the lengths of each string in the string_list.
Write a function mean_length_of_strings(string_list) which returns the mean length of all strings in string_list.
Write a function count(lst, item) which returns the number of occurrences of item in lst. Eg. 
>>> count(['b', 'a', 'n', 'a', 'n', 'a'], 'a')
3
>>> count(['b', 'a', 'n', 'a', 'n', 'a'], 'z')
0
Look up the following list methods: index(), pop(), insert(), sort(). Experiment with them. What are their parameters, if any? What causes exceptions?
Write a function median(num_list) which returns the median of a numerical list. Recall the median is the middle number of a sorted list. If there are an even number of items, the median is the mean of the middle two numbers.
Parallel Lists Create two lists of identical length: students and ids. Fill students with names of students (str). Fill ids with the student id numbers (int). (You can hardcode this.) Crucially, the name at index i is associated with the id at index i in the other list. Write a short program to list all students followed by their student number, formatted nicely, such as like this:
CLASS LIST
----------
Student      ID
Alan T       110101101
Ada L        271828182
Donald K     314159265
Albert E     299792458
'''