# Alkaline earth metals
earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]
# Sort the list alphabetically
earth_metals.sort()
print("List sorted alphabetically", earth_metals)
print("Sort the data in reverse order")
earth_metals.sort(reverse = True)
print(earth_metals)
print("#"*70)
"""
"in place" algorithm. 
python does not create a 2nd data structure, modifies the input/existing data structure
"""
"""
format := (name, radius, density, distance from sun)

Radius: Radius at the equator in kilometers
Density: Average density in g/cm^3
Distance from sun: Average distance to sun in AUs
"""
planets = [
    ("Mercury", 2440, 5.43, 0.395),
    ("Venus", 6052, 5.24, 0.723),
    ("Earth", 6378, 5.52, 1.000),
    ("Mars", 3396, 3.93, 1.530),
    ("Jupiter", 71492, 1.33, 5.210),
    ("Saturn", 60268, 0.69, 9.551),
    ("Uranus", 25559, 1.27, 19.213),
    ("Neptune", 24764, 1.64, 30.070)
]
# Sorting the planets by size
size = lambda planet: planet[1]
planets.sort(key = size, reverse = True)
print("Sorted according to size ", planets)
print("-"*70)
# Sorting the planets by density
density = lambda planet: planet[2]
planets.sort(key = density)
print("Sorted according to density ",planets)
print("*"*80)

"""
list.sort() changes the original list?
Q: Can you create a sorted copy?
Q: How do you sort a tuple?
A: Use sorted()
"""
print("earth_metals before sorting : ",earth_metals)
sorted_earth_metals = sorted(earth_metals)
print("earth_metals after sorting : ", sorted_earth_metals)
print("$"*80)

# sorting the tuple
data = (7, 2, 5, 6, 1, 3, 9, 10, 4, 8)
print(sorted(data))

# Sorting the strings
print(sorted("Alphabetical"))
