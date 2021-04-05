#! /usr/bin/env python3

import argparse

# define the functions

# function to accept command line arguments
def get_args():
	# create an ArgumentParser object
	parser = argparse.ArgumentParser(description='This script returns the Fibonacci number at \
		specified location in the Fibonacci sequence')

	# add positional arguments
	parser.add_argument("num", help="The Fibonacci number you wish to calculate", type=int)

	# add optional arguments
	# if 'store_true', this means assign 'True' if the argument is specified on the command line
	# the default for 'store_true' is false
	parser.add_argument("-v", "--verbose", help="Print verbose output or not", action='store_true')

	args = parser.parse_args()

	return args


# function to calculate the Fibonacci number/sequence
def fib(n):
	a,b = 0,1

	for i in range(n):
		a,b = b, a+b

	return a


# the 'main' function
def main():
	fib_number = fib(beyonce.num)
	
	# print the results
	if beyonce.verbose:
		print('The Fibonacci number for', beyonce.num, 'is:', fib_number)
	else:
		print(fib_number)


# get the command-line arguments
beyonce = get_args()

# set the environment for this script
# is this main, or is this a module being called by another script
if __name__ == '__main__':
	main()
















