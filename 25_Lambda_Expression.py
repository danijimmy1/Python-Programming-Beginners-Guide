"""
There are functions which does not have names at all. 
These nameless functions or anonymous functions are called Lambda functions.
Anonymous functions = Lambda expressions.
Common applications for this type of functions is sorting and filtering.
"""
# Using normal functions
# Function to compute 3*x + 1
def f(x):
    return 3*x + 1

print(f(2))

print("π"*80)
# Using anonymous function or Lambda expression
lambda x: 3*x + 1
g = lambda x: 3*x + 1
print(g(2))

print("√"*80)

# Combine first name and last name into single "Full Name"
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("     Jimmy", "Dani"))

print("*"*80)
scifi_authors = ["Issac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthus C. Clarke", "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett"]

scifi_authors.sort(key = lambda name: name.split()[-1].lower())
print(scifi_authors)

print("&"*80)

# Function that builds functions
def build_quadratic_functions(a, b, c):
    """Returns the function f(x) = ax^2 + b*x + c"""
    return lambda x: a*x**2 + b*x + c

f = build_quadratic_functions(2, 3, -5)
print(f(0))
print(f(1))
print(f(2))

# Creating different functions and then pass the value
a = build_quadratic_functions(3, 0, 1)(2) # 3*x + 1 exaluates for x = 2
print(a)