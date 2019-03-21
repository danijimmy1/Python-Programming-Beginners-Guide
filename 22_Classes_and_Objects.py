class User:
    pass

# Creating object of a class
user1 = User()
user1.first_name = "Jimmy"
user1.last_name = "Dani"
# Here first name and last name are called fields of the class User()
print(user1.first_name)
print(user1.last_name)

# Standalone variables
first_name = "Jimmy"
last_name = "Dani"
print(first_name, last_name)

# Creating second user
user2 = User()
user2.first_name = "Frank"
user2.last_name = "poole"
print(user2.first_name, user2.last_name)
# Attaching different fields to different users
user1.age = 37
user2.favourite_book = "2001 : A Space Odyssey"
print(user1.age)
print(user2.favourite_book)
