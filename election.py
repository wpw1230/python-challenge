# Dependencies
import os
import csv

# Read in election_data.csv
election_csv = os.path.join('election_data.csv')

# Store total votes in variable
tot_votes = 0

# Store list of candidates and their vote percentages in dictionaries
candidates_dict = {}
candidates_pct_dict = {}

with open(election_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Remove headers
    header = next(csvreader)
    
    for row in csvreader:
        # Tally total votes
        tot_votes += 1

        # Tally total votes per candidate
        candidate = row[2]
        if candidate in candidates_dict :
            candidates_dict[candidate] += 1
        else:
                candidates_dict[candidate] = 1
        
        # Tally total vote percentage per candidate
        candidates_pct_dict[candidate] = f"{(candidates_dict[candidate] / tot_votes * 100): .2f}%"

# Store winner data in variable
winner = max(candidates_dict, key=lambda key: candidates_dict[key])

# Print election results
print(f"Total Votes: {tot_votes}")
print(f"Vote Count: {candidates_dict}")
print(f"Vote Percentage: {candidates_pct_dict}")
print("Winner: {}".format(winner))

# Print results to text file
with open('election_results.txt', 'w') as text:
    text.write("Election Results" + "\n"
                "--------------------------" + "\n"
                "    Total Votes: " + str(tot_votes) + "\n"
                "    Candidate Vote Count: " + str(candidates_dict) + "\n"
                "    Candidate Vote Percentage: " + str(candidates_pct_dict) + "\n" 
                "    Winner: {}".format(winner)
                )