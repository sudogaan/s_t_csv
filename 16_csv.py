path = "google_stock_data.csv"
file = open(path)

for line in file:
	print(line)

path = "google_stock_data.csv"
lines = [line for line in open(path)]
print(lines[0])
print(lines[1])

print(lines[0].strip()) # to remove whitespace
print(lines[0].strip().split(",")) # to divide the string into smaller pieces

dataset = [line.strip().split(',') for line in open(path)]

print(dataset[0])
print(dataset[1])

# what if data contains "," in it, split(",") will create a problem
# to eliminate this issue

import csv
from datetime import datetime

path = "google_stock_data.csv"
file = open(path, newline='') 
reader = csv.reader(file) # to parse the csv data from the file
header = next(reader) # since the first line is the header and don't contain any data we use the next function to extract the first line
data = [row for row in reader] # to read the remaining data

print(header)
#print(data[0])

# but the data is still treated as strings 
# to fix that:

data = []
for row in reader:
	# row = [Date, Open, High, Low, Close, Volume, Adj. Close]
	date = datetime.strptime(row[0], '%m/%d/%Y')
	open_price = float(row[1]) # 'open' is the builtin function
	high = float(row[2])
	low = float(row[3])
	close = float(row[4])
	volume = int(row[5])
	adj_close = float(row[6])
	data.append([date, open_price, high, low, close, volume, adj_close])

#print(data[0])

# compute and store daily stock returns

returns_path = ("F:\data\google_returns.csv")
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(["Date", "Return"])

for i in range(len(data) - 1):
	todays_row = data[i]
	todays_date = todays_row[0]
	todays_price = yesterdays_row[-1] 
	yesterdays_row = data[i+1] # because the dates are in decreasing order, we can get yesterday's data using the index i + 1
	yesterdays_price = yesterdays_row[-1] # we can get yesterday's price from the data array using -1

	daily_return = (todays_price - yesterdays_price) / yesterdays_price
	formatted_date = todays_date.strftime('%m/%d/%Y')
	writer.writerow([formatted_date,daily_return])





