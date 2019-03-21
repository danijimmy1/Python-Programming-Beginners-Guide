# Sets do not contain duplicate elements

example = set()
example.add(42)
example.add(False)
example.add(3.14159)
print(example)
print("Length of set : ",len(example))
print("Removing element 42 from the set")
example.remove(42)
print(example)
# element can also be removed using discard method
print("Adding element 50 to the set")
example.add(50)
print(example)
print("After discarding the element 50 from the set")
example.discard(50)
print(example)

# Prepopulate set
example2 = set([28, True, 2.71828, "Helium"])
print(len(example2))
print(example2)
# To remove all the elements from the set use clear method
example2.clear()
print(len(example2))

# Union and intersection of set
# Intehers 1 - 10
odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])

print("union of odds and evens")
print(odds.union(evens))
print("Intersection of odds and primes")
print(odds.intersection(primes))
print("Intersection of evens and primes")
print(primes.intersection(evens))
print("Union of primes and composite")
print(primes.union(composites))
print(2 in primes)
print(9 in evens)