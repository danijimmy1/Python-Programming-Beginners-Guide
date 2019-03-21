squares = []
for i in range(1, 101):
    squares.append(i**2)

print(squares)

# List Comprehension
squares2 = [i**2 for i in range(1, 101)]
print(squares2)
print("*"*80)
remainders = [x**2 % 5 for x in range(1, 101)]
print(remainders)
print("*"*80)
remainders11 = [x**2 % 11 for x in range(1, 101)]
print(remainders11)
print("*"*80)
movies = ["Star Wars", "Gandhi", "Casablancs", "Shawshank", "Good Will Hunting", "Raiders of the Lost Ark", "Groundhog Day"]
# Getting all the movies that starts from 'G'
print("Without List Comprehension")
gmovies = []
for title in movies:
    if title.startswith("G"):
        gmovies.append(title)

print(gmovies)

print("With list compression")
gmovies2 = [title for title in movies if title.startswith("G")]
print(gmovies2)
print("*"*80)
# List containing tuples
movies3 = [("Citizen Kane", 1941), ("Spirited Away", 2001), ("Gattaca", 1997), ("No Country for Old Men", 2007)]
# Find the movies released befre 2000
pre2k = [title for (title, year) in movies3 if year < 2000]
print(pre2k)
print("*"*80)
# Scalar multiplication using list comprehension
v = [2, -3, 1]
w = [4*x for x in v]
print(w)
print("*"*80)
# Computing Cartesian Coordinate
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
cartesian_product = [(a,b) for a in A for b in B]
print(cartesian_product)