import math

def area(r):
    """Area of the circle with radius 'r'."""
    return math.pi * (r**2)

# To compute area of multiple circle
radii = [2, 5, 7.1, 0.3, 10]

# Method 1: Direct Method

areas = []
for r in radii:
    a = area(r)
    areas.append(a)

print(areas)
print("*"*80)

# Method 2: Use 'map' function
# This function takes two arguments
# 1. function name
# 2. Tuple or list or 
print(list(map(area, radii)))

print("&"*80)
temps = [("Berlin", 29), ("Cairo",36), ("Buenos Aires", 19),
        ("Los Angeles", 26), ("Tokoyo", 27), ("New York", 28),
        ("London", 22), ("Beijing", 32)]

c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)
print(list(map(c_to_f, temps)))

print("^"*80)
# Filter Function is used to select specific data from list, tuple or other collection of data.
import statistics as st

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = st.mean(data)
print(avg)
# Filter function to select data greater than the average
ff = filter(lambda x: x > avg, data)
print(list(ff))
print("%"*80)
# Remove Missing data using filter
countries = ["", "Argentina", "", "Brazil", "Chile", "", "Columbia", "",
            "Ecuador", "", "", "Venezuela"]
# Filter out the strings that returns false
ff2 = filter(None, countries)
print(list(ff2))
print("+="*80)
# Reduce Function
"""
Data: [a1, a2, a3, ..., an]
Function: f(x, y)

reduce(f, data):
    Step 1: val1 = f(a1, a2)
    Step 2: val2 = f(val1, a3)
    Step 3: val3 = f(val2, a4)
    .
    .
    .
    Step n-1: val(n-1) = f(val(n-2), a(n))
    Return val(n-1)

Alternatively:
    Returns f(f(f(a1, a2), a3), a4), ..., a(n))
"""
from functools import reduce
# Multiply all the numbers in a list
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
multiplier = lambda x, y: x*y
print(reduce(multiplier, data))

# Without using reduce function
product = 1
for x in data:
    product = product * x

print("Without using reduce()",product) 