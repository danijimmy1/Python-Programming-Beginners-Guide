# Two ways to create lists in python
example = list()
example2 = []

primes = [2, 3, 5, 7, 11, 13]
primes.append(17)
primes.append(19)
print(primes)

print(primes[0])
print("Looking at the last item")
print(primes[-1])

# Slicing
s1 = primes[2:5]
print(s1)

s2 = primes[0:6]
print(s2)

example = [128, True, "Alpha", 1.732, [64, False]]
print(example)

# Combining lists
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
print("After Combining")
print(numbers + letters)
print(letters + numbers)

print("To reverse the list")
numbers.reverse()
print(numbers)