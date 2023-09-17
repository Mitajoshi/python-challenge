#PyPoll
# Modules
import os
import csv

print("Election Results")
print("--------------------------")

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read the header row first
    csv_header = next(csvreader)

    row_ctr = 0
    total_ballots = 0
    cand_votes = {}
    candidates = []
    for row in csvreader:
        #Initialize a list to hold the first name from top row. 
        #This list is for storing candidate names as they get discovered.
        candidate = row[2] 
        
        #Create a running sum of number of rows in the file
        row_ctr = row_ctr + 1
        total_ballots += int(row[0])

        #Identifying unique candidates
        if candidate not in candidates:
            candidates.append(candidate)
            #Initialize current candidate's vote count
            cand_votes[candidate] = 0 
        #Since current candidate matches the current row, 
        #continue adding that candidate's vote count
        cand_votes[candidate] += 1
        
    #Print the total number of rows in the file, 
    #which is same as the number of ballots cast in the polls
    print(f"Total Votes: {row_ctr}")    
    print("--------------------------")

    #Initializing the highest vote percentage variable
    winner = {}
    highest_votes = cand_votes[candidates[0]]
    for candidate in cand_votes:
        votes = cand_votes[candidate]
        percent_vote = round((votes*100/row_ctr),3)
        print(f"{candidate}: {percent_vote}% ({cand_votes[candidate]})")
    
        if highest_votes < votes:
            highest_votes = votes
            winner[highest_votes] = candidate
    print("--------------------------")
    print(f"Winner: {winner[highest_votes]}")
    print("--------------------------")

#Specifying the file to write to
output_path = os.path.join("analysis", "Poll_Results.txt")
#Opening file with write mode, specifying the variable to hold the contents
with open(output_path, 'w') as csvfile:
    #Initialize csv writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    #Writing the first row column headers
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["--------------------------"])
    csvwriter.writerow(['Total Votes: ' + str(row_ctr)])
    csvwriter.writerow(["--------------------------"])
    for candidate in cand_votes:
        votes = cand_votes[candidate]
        percent_vote = round((votes*100/row_ctr),3)
        csvwriter.writerow([candidate + ': '  + str(percent_vote) + '% ' + '(' + (str(cand_votes[candidate]) + ')')])
    #Post the winner in the file
    csvwriter.writerow(["--------------------------"])
    csvwriter.writerow(['Winner: ' + winner[highest_votes]])
    csvwriter.writerow(["--------------------------"])

    
