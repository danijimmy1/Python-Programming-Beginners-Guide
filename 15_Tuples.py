import sys
import timeit

# Difference between list and tuples
# List Example
prime_numbers = [2, 3, 5, 7, 11, 13, 17]

# Tuple Example
perfect_squares = (1, 4, 9, 16, 25, 36)

# Display Length
print("# Primes = ", len(prime_numbers))
print("# Squares = ", len(perfect_squares))

# Iterate over both sequences
for p in prime_numbers:
	print("Prime : ", p)

for n in perfect_squares:
	print("Square : ", n)

# Methods for list
print("List methods")
print(dir(prime_numbers))
print(80*"-")
print("Tuples methods")
print(dir(perfect_squares))

# Creating list and tuple of exactly same elemets
list_eg = [1, 2, 3, "a", "b", "c", True, 3.14159]
tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.14159)
print("Getting size of list and tuple")
print("List size = ", sys.getsizeof(list_eg))
print("Tuple size = ", sys.getsizeof(tuple_eg))

# To see which takes more time list or tuples
list_test = timeit.timeit(stmt = "[1, 2, 3, 4, 5]", number = 10000000)
tuple_test = timeit.timeit(stmt = "(1, 2, 3, 4, 5)", number = 10000000)
print("List time : ", list_test)
print("Tuple time : ", tuple_test)

"""
Differences between lists and tuples:
1. Lists takes more momory than tuples
2. You can add, remove or change data in lists, while tuples cannot be changed
3. Tuples can be made more quickly then lists
4. Tuples are immutable
"""

# Empty tuple
empty_tuple = ()
# Tuple containing only one element is considered string
test1 = ("a")
# To make a tuple with one element
test11 = ("a",)
test2 = ("a", "b")
test3 = ("a", "b", "c")
print(empty_tuple)
print(test1)
print(test11)
print(test2)
print(test3)

# Alternative for construction of tuples
tt1 = 1,
tt2 = 1, 2
tt3 = 1, 2, 3
print(tt1)
print(tt2)
print(tt3)
print(type(tt1))
print(type(tt2))
print(type(tt3))

# Tuple with one element
# (age, country, knows_python)
survey = (27, "Vietnam", True)
age = survey[0]
country = survey[1]
knows_python = survey[2]

print("Age = ", age)
print("Country = ", country)
print("Knows Python?", knows_python)

survey2 = (21, "Switzerland", False)
age, country, knows_python = survey2
print("Age = ", age)
print("Country = ", country)
print("Knows_Python?", knows_python)

country = ("Australia",)
print(country)

# Number of variable should be equal to number of values