"""
Read the data from the file task02.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches
"""
test = input("input the name of a stock: ")
test = test
numberT = 0
import csv
reader = csv.reader(open('task5.csv'))

result = {}
for row in reader:
    key = row[0]
    if key in result:
        # implement your duplicate row handling here
        pass
    result[key] = row[1:]

for x in result:
    if test in x:
        numberT = numberT + 1

if numberT == 1:
    for x in result:
        if test in x:
            print(f"{result[x]}")
elif numberT > 1:
    print(f"There are {numberT} stocks with that symbol")
else:
    print("Invalid search. try again")