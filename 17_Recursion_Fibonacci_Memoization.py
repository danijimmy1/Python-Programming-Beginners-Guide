# import Least Recently used cache
from functools import lru_cache

# Fibonacci Sequence 1, 1, 2, 3, 5, 8, 13, 21 ...
# Write a function to return nth term of fibonacci sequence
# Modifying this function for computing more fibonacci series numbers

# Default value for this cache is 128

@lru_cache(maxsize = 1000)
def fibonacci(n):
	# Check if the input is an integer
	if type(n) != int:
		raise TypeError("n must be a positive integer")
	if n < 1:
		raise ValueError("n must be a positive integer")


	if n == 1:
		return 1
	elif n == 2:
		return 1
	elif n > 2:
		return fibonacci(n-1) + fibonacci(n-2)

# for i in range(1, 51):
# 	print(i, " : ", fibonacci(i))

# To see by what percentage numbers are growing simply by taking ratio
for n in range(1, 51):
	print(fibonacci(n+1) / fibonacci(n))

# The function is extremely slow if you want to print 100 number is the sequence
# Simple idea for this is memoization
# Store the values for the recent function call so future calls do not have to repeat the work
# Memoization can be implemented in several ways:
print("-"*80)
print("Creating another function for making computation faster for getting more numbers faster in fibonacci series")
# 1. implement Explicitly
# Create a dictionary called fibonacci cache
fibonacci_cache = {}
# Rewriting the function to make use of cache values
def fibonacci2(n):
	# If we have cached the value, then return it
	if n in fibonacci_cache:
		return fibonacci_cache[n]

	# Compute the Nth term
	if n == 1:
		value = 1
	elif n == 2:
		value = 2
	elif n > 2:
		value = fibonacci2(n - 1) + fibonacci2(n - 2)

	# Canhe the value and return it
	fibonacci_cache[n] = value
	return value

for n in range(1, 101):
	print(n , " : ", fibonacci2(n))