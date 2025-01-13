# -*- coding: UTF-8 -*-
#"""PyBank Homework Solution."""

# Dependencies
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data and calculate the summary
total_months = 0
total_net = 0
prev_profit_loss = 0
changes = [] # To Track the changes in profit/losses
months = [] # To Track the months for our changes
greatest_increase = ["", float('inf') * -1]
greatest_decrease = ["", float('inf')]

# Open and read the csv. with open (file_to_load, encoding='utf-8') as csvfile:
with open(file_to_load, encoding='UTF-8') as financial_data:
    reader = csv.reader(financial_data, delimiter=",")

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    # Track the total and net change
    total_months = 1
    total_net = int(first_row[1])
    prev_profit_loss = int(first_row[1])

    # Process each row of data
    for row in reader:

        # Track the total
        total_months = total_months + 1
        current_profit_loss = int(row[1])

        # Track the net change
        total_net = total_net + current_profit_loss
        # Changes in "profit/losses" over the entire period
        change = current_profit_loss - prev_profit_loss
        changes.append(change)
        months.append(row[0]) # Store the month for this change

        # Calculate the greatest increase in profits (month and amount)
        if(change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = change

        # Calculate the greatest decrease in losses (month and amount)
        if(change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change

        #Set up for next change calculation
        prev_profit_loss = current_profit_loss

# Calculate the average net change across the months
net_montly_avg = sum(changes) / len(changes)

# Generate the output summary and print the output
output = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${net_montly_avg:.2f}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"""
print(output)


# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
