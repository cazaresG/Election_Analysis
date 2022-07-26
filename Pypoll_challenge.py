# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_results.txt")

# 1. Initialize a total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}
# Initialize a county list ------------------------------------ 1 
county_list = []
# Initialize a county dictionary (county key & votes) --------- 1
county_votes = {}




# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Winning county empty string--------------------------------  2
county_largest_turnout = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
   # Read and print the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
#print(total_votes)


# Print the candidate name from each row.
        candidate_name = row[2]
#Print county name for each row-----------------------------------  3
        county_name = row[1]
# If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
    # Add it to the list of candidates.
           candidate_options.append(candidate_name)
            # 2. Begin tracking that candidate's vote count.
           candidate_votes[candidate_name] = 0
            # 2. Begin tracking that candidate's vote count.
        candidate_votes[candidate_name] += 1

#Decision Statement ----------------------------------------------
        if county_name not in county_list: #---------------------- 4a
           county_list.append(county_name) #---------------------- 4b
           county_votes[county_name] = 0 #------------------------ 4c
        county_votes[county_name] += 1 #-------------------------- 5




#Using the with statement open the file as a text file.
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



# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
        candidate_results = (
        f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)



    for county_name in county_votes: #--------------------------------------------------- 6a
        votes2 = county_votes[county_name] #----------------------------------------6b
        county_vote_percentage = float(votes2) / float(total_votes) * 100 #--------6c
        county_results = (
        f"{county_name}: {county_vote_percentage:.1f}% ({votes2:,})\n") #----------6d
        print(county_results)
        txt_file.write(county_results)


        if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_candidate = candidate_name
         # And, set the winning_candidate equal to the candidate's name.
         winning_percentage = vote_percentage


#  Decision statement/ county with largest vote count  #----------------------------------6f
         if (votes2 > winning_count) and (county_vote_percentage > winning_percentage):
          winning_count = votes2
          county_largest_turnout = county_name
          winning_percentage = county_vote_percentage

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

    winning_county_summary = (   #----------------------------------------------------7
        f"Largest County Turnout: {county_largest_turnout}\n"
        f"-------------------------\n")
    print(winning_county_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_county_summary)
    

# Print each candidate, their voter count, and percentage to the terminal.
#print(candidate_results)


#print(candidate_votes)