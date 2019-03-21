import datetime

# Default format for date is yyyy-mm-dd
gvr = datetime.date(1956, 1, 31)
print(gvr)
print(gvr.year)
print(gvr.month)
print(gvr.day)

# To add or subtract number of days from date use timedelta
mill = datetime.date(2000, 1, 1)
# This takes number of days as arg
dt = datetime.timedelta(100)
# Positive number will increase the date and negative number will decrease the date
print("mill + dt : ",mill + dt)

# Reformat the date
# Day-name, Month-name day #, Year
# Two ways to do this
print(gvr.strftime("%A, %B %d, %Y"))
message = "GVR was born on  {:%A, %B %d, %Y}."
print(message.format(gvr))

# Format similar to launch date
launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
print(launch_date)
print(launch_time)
print(launch_datetime)

# Access current date and time
# This can be achieved using method today
now = datetime.datetime.today()
print(now)

# Taking date as a string and converting that string as a date
# This can be done using method String parse Time a.k.a strptime 
moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)
print(type(moon_landing_datetime))