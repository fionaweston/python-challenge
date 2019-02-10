import csv
import os

# Location of input file
inputfile = os.path.join( '.', 'Resources', 'budget_data.csv')
# Location of output file
outputdir = os.path.join( '.', 'output')
outputfile = os.path.join( outputdir, 'pybank_output.txt')

# Initialize variables to be used in program
monthCount = 0
sumofPandL = 0
maxProfit = ('', 0)
maxLoss = ('', 0)

# Read file as CSV and parse for values as directed
with open(inputfile, newline='') as csvfile:
    inputfile = csv.reader(csvfile)
    next(inputfile)

    # Loop through CSV file and parse data
    for line in inputfile:
        if len(line) > 0:
            income = int(line[1])

            # Increase monthCount and add income to sum of profits/losses
            monthCount += 1
            sumofPandL += income

            # Replace maxProfit with current month/profit if profit is greater
            # than current maxProfit
            if income > maxProfit[1]:
                maxProfit = (line[0], income)

            # Replace maxLoss with current month/loss if loss is less
            # than current maxLoss
            elif income < maxLoss[1]:
                maxLoss = (line[0], income)

# Print results to console
print("Financial Analysis")
print("------------------")
print(f"Total Months: {monthCount}")
print(f"Total Profit/Loss: ${sumofPandL}")
print(f"Average Change: ${sumofPandL/monthCount:.2f}")
print(f"Greatest Increase in Profits: {maxProfit[0]} ($ { maxProfit[1]})")
print(f"Greatest Decrease in Profits: {maxLoss[0]} ($ {maxLoss[1]})")

# Write output to text file
if not os.path.exists(outputdir):
    os.makedirs(outputdir)
with open(outputfile, 'w') as fout:
    print("Financial Analysis" , file=fout)
    print("------------------" , file=fout)
    print(f"Total Months: {monthCount}" , file=fout)
    print(f"Total Profit/Loss: ${sumofPandL}" , file=fout)
    print(f"Average Change: ${sumofPandL/monthCount:.2f}" , file=fout)
    print(f"Greatest Increase in Profits: {maxProfit[0]} ($ {maxProfit[1]} )" , file=fout)
    print(f"Greatest Decrease in Profits: {maxLoss[0]} ($ {maxLoss[1]} )" , file=fout)
