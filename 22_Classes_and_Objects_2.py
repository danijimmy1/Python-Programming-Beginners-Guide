import datetime
""" 
Class Features
1. Methods
2. Initialization Methods (a.k.a Constructors)
3. Help text
"""
class User():
    """A member of FriendFace. For now we are only storing their name and birthday.
       But soon we will store an uncomfortable amount of user information."""

    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday #yyyymmdd

        # Extract first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]
    
    def age(self):
        """Returns age of the user in years."""
        today = datetime.date(2018, 6, 29)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)

user = User("Jimmy Dani", "19950616")
print(user.name)
print(user.first_name)
print(user.last_name)
print(user.birthday)
print(user.age())