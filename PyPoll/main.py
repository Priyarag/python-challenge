#import dependencies
import pandas as pd

# Make a reference to the election_data.csv file path
csv_name = "election_data.csv"
# Import the election_data.csv file as a DataFrame
with open("election_data.txt", "w+") as output:
	# Import the CSV into a pandas DataFrame
	election_data_df = pd.read_csv(csv_name)
	#print Election Results header 
	header_output = ("Election Results\n----------------------------")
	print (header_output)
	#store the total votes count to Total_votes
	Total_votes = len(election_data_df['Voter ID'])
	Total_votes_output = (f"Total Votes: {Total_votes}\n----------------------------")
	#print the The total votes cast
	print(Total_votes_output)
	#write the above print results to the txt file
	output.write(f'{header_output}\n{Total_votes_output}\n')
	# Finding the percentage of votes each candidate won 
	Candidate_perc = election_data_df["Candidate"].value_counts(normalize=True)
	Candidate_perc.index = Candidate_perc.index.astype(str)
	#convert Candidate_perc to dict 
	Candidate_perc_dict =  (Candidate_perc.to_dict())
	#get the percentage of votes with 3 decimal format
	Candidate_perc = Candidate_perc.map(lambda n: '{:,.3%}'.format(n))
	#Find the total number of votes each candidate won 
	election_data_total = election_data_df["Candidate"].value_counts()
	#Loop through the no of items in the dict and print & write to output txt file, in 
	#format - Candidate: total vote won% (total vote)
	for i in range(0,len(Candidate_perc_dict)):
		cand_perc= (f"{list(Candidate_perc_dict)[i]}: {Candidate_perc[i]} ({election_data_total[i]})")
		print(cand_perc)
		output.write(f'{cand_perc}\n')
	#get the winner name of the election based on popular vote using max function
	#idxmax() function returns index of first occurrence of maximum over requested axis.
	winner = election_data_total.idxmax()
	winner_output = (f"----------------------------\nWinner: {winner}\n----------------------------")
	#print & write the winner name to output txt file
	print(winner_output)
	output.write(f'{winner_output}')

