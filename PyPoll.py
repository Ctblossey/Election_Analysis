# Add our dependencies

import csv

import os

# Assign a variable to load a file from a path

file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter

total_votes = 0

# Candidate Options

candidate_options = []

# Declare empty dictionary

candidate_votes = {}

# Winning Candidate & Count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file

with open(file_to_load) as election_data:

# Read the file object with the reader function

    file_reader = csv.reader(election_data)

    # Read the header row

    headers = next(file_reader)

    # Print each row in the CSV file

    for row in file_reader:

     # Add the total vote count
     total_votes += 1

     # Print the candidate name from each row

     candidate_name = row[2]

     #Add the unique candidate name to the candidate list
     if candidate_name not in candidate_options: 

        # Add candidate

        candidate_options.append(candidate_name)

        # Begin tracking vote count

        candidate_votes[candidate_name] = 0

     #Add initial vote

     candidate_votes[candidate_name] += 1


#Save results to text file
with open(file_to_save, "w") as txt_file:

                # Print the final vote count to the terminal.
                election_results = (
                    f"\nElection Results\n"
                    f"-------------------------\n"
                    f"Total Votes: {total_votes:,}\n"
                    f"-------------------------\n")
                print(election_results, end="")
                # Save the final vote count to the text file.
                txt_file.write(election_results)

                for candidate_name in candidate_votes:
                        
                    #Retrieve vote count of a candidate
                    votes = candidate_votes[candidate_name]

                    #Calculate % of votes for candidate
                    vote_percentage = float(votes) / float(total_votes) * 100
                    candidate_results = (
                        f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

                    #Print candidate results to terminal
                    print(candidate_results)

                    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

                    if (votes > winning_count) and (vote_percentage > winning_percentage):
                        # If true then set new values
                        winning_count = votes
                        winning_percentage = vote_percentage
                        winning_candidate = candidate_name

                  # Print the winning candidate's results to the terminal.
                winning_candidate_summary = (
                 f"-------------------------\n"
                 f"Winner: {winning_candidate}\n"
                 f"Winning Vote Count: {winning_count:,}\n"
                 f"Winning Percentage: {winning_percentage:.1f}%\n"
                 f"-------------------------\n")
                print(winning_candidate_summary)
                  # Save the winning candidate's results to the text file.
                txt_file.write(winning_candidate_summary)
                
                