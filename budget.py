# Dependencies
import os
import csv

# Read in budget_data.csv
budget_csv = os.path.join('budget_data.csv')

# Create variables, set initial values at 0
total_months = 0
total_profit = 0
initial_profit = 0
total_change_profits = 0

# Create monthly profit changes, profit lists
monthly_changes = []
profit = []

with open(budget_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Remove headers
    header = next(csvreader)
    
    for row in csvreader:
        # Tally total months, profit for each row
        total_months += 1
        
        # Append profit information & calculate total profit
        profit.append(row[1])
        total_profit = total_profit + int(row[1])
        
        # Calculate monthly change in profits
        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit
        
        # Store monthly changes in monthly_changes list
        monthly_changes.append(monthly_change_profits)
        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = final_profit
        
    # Calculate average change in profits, subtracting first value in dataset since there is
    # no previous value, and thus no change for that month
    avg_chg_profits = (total_change_profits - monthly_changes[0]) / (len(monthly_changes) - 1)

# Print results
print(f"Total Months: {total_months}")
print(f"Total Profit: ${total_profit : .0f}")
print(f"Average Change: ${avg_chg_profits: .2f}")
print("Greatest Increase in Profits: $", max(monthly_changes))
print("Greatest Decrease in Profits: $", min(monthly_changes))

# Print results to text file
with open('financial_analysis.txt', 'w') as text:
    text.write("Financial Analysis" + "\n"
                "--------------------------" + "\n"
                "    Total Months: " + str(total_months) + "\n"
                "    Total Profit: $" + str(total_profit) + "\n"
                f"    Average  Change: ${avg_chg_profits:.2f}\n"
                "    Greatest Increase in Profits: $" + str(max(monthly_changes)) + "\n" 
                "    Greatest Decrease in Profits: $" + str(min(monthly_changes))
                )