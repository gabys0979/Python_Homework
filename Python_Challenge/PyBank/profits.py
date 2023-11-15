# Modules
import os
import csv

#set pathway
csvpath = os.path.join("Resources", "budget_data.csv")

#initialize variables
totalMonths = 0
netprofit = 0
monthlyChanges = []
prevmonth = 0
greatestIncrease = ['date', '0']
greatestDecrease = ['date', '0']
monthlyChanges = 0

#open the csv
with open(csvpath, encoding='utf') as csvfile:
    budgetData = csv.reader(csvfile, delimiter=",")
    #skip header
    next(budgetData)
    # calculating changes
    for row in budgetData:
        totalMonths = totalMonths + 1 
        netprofit += int(row[1]) 
        change = int(row[1])-prevmonth #difference
        #check if it set a new record
        if change > 0:
            if change > int(greatestIncrease[1]):
                greatestIncrease = [row[0], str(change)]
        #profit decreased check if it is a new record
        if change < 0: 
            if change < int(greatestDecrease[1]):
                greatestDecrease = [row[0], str(change)]
        monthlyChanges += change #cumulative changes
        prevmonth = int(row[1]) 

    #output results to terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total: {netprofit}")
    print(f"Average Change: ${monthlyChanges/(totalMonths-1)}")
    print(f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})")
    print(f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})")

#write to a text file
with open("analysis\profits.txt", 'w') as file:
    print("Financial Analysis", file = file)
    print("----------------------------", file = file)
    print(f"Total Months: {totalMonths}", file = file)
    print(f"Total: {netprofit}", file = file)
    print(f"Average Change: ${monthlyChanges/(totalMonths-1)}", file = file)
    print(f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})", file = file)
    print(f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})")
