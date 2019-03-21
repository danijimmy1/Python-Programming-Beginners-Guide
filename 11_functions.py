import math

def ping():
	return "Ping!"

def volume(r):
	"""Returns the volume of sphere with radius r."""
	v = (4.0/3.0) * math.pi * r**3
	return v

def traingle_area(b, h):
	"""This function returns the area of the traingle"""
	return 0.5 * b * h

x = ping()
print(x)

vol = volume(3)
print(vol)

area_tr = traingle_area(2, 4)
print(area_tr)


# function with keyword arguments
def cm(feet = 0, inches = 0):
	"""converts a length from feet and inches to centimeters"""
	inches_to_cm = inches * 2.54
	feet_to_cm = feet * 12 * 2.54
	return inches_to_cm + feet_to_cm

print(cm(feet = 5))
print(cm(inches = 70))
print(cm(feet = 5, inches = 8))
print(cm(inches = 8, feet = 5))

# Types of arguments
# 1. Keyword arguments which are with some initial value
# 2. Required arguments which are without any initial values
# While writing a function with combination of required and keyword arguments 
# Keyword arguments are last
# Keyword arguments are passed by names

def g(y, x = 0):
	return x + y

print(g(5))
print(g(5, x = 4))