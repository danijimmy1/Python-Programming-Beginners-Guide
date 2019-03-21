import csv
from datetime import datetime

path = "./19_stock.csv"
file = open(path, newline = '')
reader = csv.reader(file)

header = next(reader) # This is first line in CSV file

data = []
for row in reader:
	# row = [Date, Open, High, Low, Close, Adj. Close]
	date = datetime.strptime(row[0], '%m/%d/%Y')
	open_price = float(row[1])
	high = float(row[2])
	low = float(row[3])
	close = float(row[4])
	volume = int(row[5])
	adj_close = float(row[6])

	data.append([date, open_price, high, low, close, volume, adj_close])

# Compute and store daily stock returns
return_path = "./19_stock_returns.csv"
file = open(return_path, 'w')
writer = csv.writer(file)
writer.writerow(["Date", "Return"])

for i in range(len(data) - 1):
	todays_row = data[i]
	todays_date = todays_row[0]
	todays_price = todays_row[-1]
	yesterdays_row = data[i+1]
	yesterdays_price = yesterdays_row[-1]

	daily_return = (todays_price - yesterdays_price) / yesterdays_price
	#writer.writerow([todays_date, daily_return])
	# Format data in user readable format
	formatted_date = todays_date.strftime('%m/%d/%Y')
	writer.writerow([formatted_date, daily_return])