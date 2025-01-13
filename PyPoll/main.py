# -*- coding: UTF-8 -*-
#"""PyPoll Homework Solution."""

# Import necessary modules
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = {}

# Winning Candidate and Winning Count Tracker
winner = ""
winner_count = 0

# Open and read the csv. with open (file_to_load, encoding='utf-8') as csvfile:
with open(file_to_load, encoding='UTF-8') as election_data:
    reader = csv.reader(election_data, delimiter=",")

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets). Did this but takes forever.
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes = total_votes +1


        # Get the candidate's name from the row
        candidate = row[2]


        # If the candidate is not already in the candidate list, add them
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1


        # Add a vote to the candidate's count
        if candidates[candidate] > winner_count:
            winner = candidate
            winner_count = candidates[candidate]


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Loop through the candidates to determine vote percentages and identify the winner
    percentage_format = "{:.3%}"
    candidate_results = []
    for candidate, votes in candidates.items():

        # Get the vote count and calculate the percentage
        percentage = votes / total_votes
        formatted_percentage = percentage_format.format(percentage)

        # Update the winning candidate if this one has more votes. Print and save each candidate's vote count and percentage
        candidate_results.append(f"{candidate}: {formatted_percentage} ({votes})")

    print() # Add a blank line for readability
    # Print the total vote count. Generate and print the winning candidate summary (to terminal). Write total vote count, generate and print winning candidate summary to the text file. 
    output =f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{chr(10).join(candidate_results)}
-------------------------
Winner: {winner}
-------------------------"""
    print(output)
    # Save the winning candidate summary to the text file
    txt_file.write(output)