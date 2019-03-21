# Path of the CSV file
path = "./19_stock.csv"
# Use open function to display the contents of the file
file = open(path)

# for line in file:
#	print(line)

# Parse the data without using CSV module
lines = [line for line in open(path)]

# Looking at the first two lines
print(lines[0])
print(lines[1])

# strip() method can be used to remove the white space
print(lines[0].strip())
# split() can be used to divide the string into smaller pieces
print(lines[0].strip().split(','))
# Reading the data again
dataset = [line.strip().split(',') for line in open(path)]
print(dataset[0])
print(dataset[1])

print("+"*70)
# Reading a csv file using csv module
import csv

file2 = open(path, newline = '')
# Reader function to parse the csv data from the file
reader = csv.reader(file2)

header = next(reader) # The first line is the header
data = [row for row in reader] # Read the remaining data

print(header)
print(data[0])

print("+"*70)

# from datetime import datetime
# import time

# file3 = open(path, newline = '')
# reader3 = csv.reader(file3)

# header = next(reader3) # The first line is header

# print("Converting the data to appropriate types")
# data2 = []
# for row in reader3:
# 	# row = [Date, open, High, Low, Close, Volume, Adj. Close]
# 	date = datetime.strptime(row[0], '%m/%d/%Y')
# 	open_price = float(row[1])
# 	high = float(row[2])
# 	low = float(row[3])
# 	close = float(row[4])
# 	volume = int(row[5])
# 	adj_close = float(row[6])

# 	data2.append([date, open_price, high, low, close, volume, adj_close])

# print(data2[0])

# # Compute and store daily stock return
# return_path = "./stock_returns.csv"
# # open a file in write mode
# file4 = open(return_path, 'w')
# writer = csv.writer(file4)
# writer.writerow(["Date", "Return"])

# for i in range(len(data2) - 1):
# 	todays_row = data2[i]
# 	todays_date = todays_row[0]
# 	todays_price = todays_row[-1]
# 	yesterday_row = data[i+1]
# 	yesterday_price = yesterday_row[-1]

# 	daily_return = (todays_price - yesterday_price) / yesterday_price
# 	writer.writerow([todays_date, daily_return])