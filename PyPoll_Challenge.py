import csv
import os
# # Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources',"election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Declare the empty dictionary for candidate and votes.
candidate_votes = {}

# Declare empty County List
county_list = []

# Declare empty dictionary for county and votes.
county_votes = {}

# Largest county turnout
winning_county = ""
winning_county_count = 0

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# # Open the election results and read the file.
with open(file_to_load,newline="") as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data,delimiter=',')

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    # Iterate each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the total votes.
        print(total_votes)

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count..
            candidate_votes[candidate_name] = 0
                
        # Add a vote to that candidate's count. 
        candidate_votes[candidate_name] += 1


        # Print the county name for each row.
        county_name = row[1]
        # If the county name does not match any existing county name...
        if county_name not in county_list:
            # Add it to the list of counties.
            county_list.append(county_name)
            # And begin tracking that county's voter count..
            county_votes[county_name] = 0
        # Add a vote to that county's count. 
        county_votes[county_name] += 1


# Save the results to our text file.
with open(file_to_save,'w') as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each county by looping through the counts.
    # Iterate through the county list.
    
    # Print the county vote count to the terminal.
    county_vote_results = (f"County Votes:\n")
    print(county_vote_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(county_vote_results)

    for county in county_votes:
        # Retrieve vote count of a county.
        countyvotes = county_votes[county]
        # Calculate the percentage of votes.
        countyvote_percentage = float(countyvotes)/float(total_votes) * 100
 
        # Print the county name and percentage of votes.
        county_results = (f"{county}: {countyvote_percentage:.1f}% ({countyvotes:,})\n")
        # Print each county, its vote count, and percentage to the terminal.
        print(county_results)
        #  Save the candidate results to our text file.
        txt_file.write(county_results)

        
        # Determine winning county vote count
        if (countyvotes >= winning_county_count):
            # If true then set winning_county_count = county_votes.
            winning_county_count = countyvotes
            # Set the winning_county equal to the county's name.
            winning_county = county
        
    # Print the final county vote count to the terminal.
    county_election_results = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(county_election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(county_election_results)

        
    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes= candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = float(votes)/float(total_votes) * 100
        # Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
                        
        # Determine winning vote count and candidate
        if (votes >= winning_count) and (vote_percentage >= winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate
        
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
            
