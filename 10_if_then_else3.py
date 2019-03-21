# Scalance Triangle : All sides have different sides
# Isosceles Triangle : Two sides have same length
# Equilateral Triangle : All sides are equal.

a = int(input("Enter length of side a : "))
b = int(input("Enter length of side b : "))
c = int(input("Enter length of side c : "))

if a!=b and b!=c and a!=c:
	print("This is a scalanne triangle.")
elif a == b and b == c:
	print("This is equilateral triangle.")
else:
	print("It is Isosceles triangle.") 