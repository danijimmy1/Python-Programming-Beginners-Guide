""" WARNING: The pseudo-random generators of this module should not be used for
	security purposes. Use os.urandom() or SystemRandom if you require a cryptographically
	secure pseudo-random generator.
"""
import random

# Display 10 random numbers from interval [0, 1)
for i in range(10):
	print(random.random())

print("-"*70)

# Generate random numbers from interval [3, 7)
"""
Several ways of doing this
call random(): 					# in [0,1)
scale number (multiply by 4): 	# in [0,4) (as difference between 7 and 3 is 4)
Shift number (add 3):			# in [3,7)

Reason for doing this to show random() function can be used to build
customized random number generator.
"""
def my_random():
	# Random, scale, shift, return ...
	return 4*random.random() + 3

for i in range(10):
	print(my_random())

print("-"*70)
"""
Easier way to generate random number within specific range is 
using uniform() available in random module
"""
for i in range(10):
	print(random.uniform(3,7))


# random() and uniform() are both uniform distributions.

print("*"*70)
# To generate number from bell curve along some mean and standard deviation
# use normalvariate()
for i in range(20):
	print(random.normalvariate(0, 1))

print("^"*70)
# Generate numbers within specific range with discrete probability distributions
# This can be achieved using randint()
for i in range(20):
	print(random.randint(1, 6))

print("+"*70)
"""
Random selection from list of values. playing rock, paper, scissors.
"""
outcomes = ['rock', 'paper', 'scissors']
# To pick a random values from this list use a choice funtion
for i in range(20):
	print(random.choice(outcomes))