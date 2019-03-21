# Numbers: int, floats, complex
# Operations: + - / *

x = 28 # int
y = 28.0 # float

# ints are narrower than float 
# floats are wider than ints

# To convert number into complex number
a = 1.732 #float
a = 1.732 + 0j
print(a)
# Or pass number to complex constructor
print(complex(1.732))

# complex numbers cannot be converted to floats
# floats are narrower than complex numbers
# complex numbers are wider than float

# Arithmetic operations
a = 2 # int
b = 6.0 # float
c = 12 + 0j # complex number

# Rule: widen numbers so they are of same type
# Addition
s = a + b # int + float = float (a is widen to float)
print(s)

# Subtraction
ss = b - a # float - int = float (a is widen to float)
print(ss)

# Multiplication
m = a * 7 # int * int
print(m)

# Division
dd = c / b # complex / float (b is widen to complex)
print(dd)

rem = 16 % 5 # This gives remainder
print(rem)

rem = 16 % 5 # This gives remainder
print(rem)

