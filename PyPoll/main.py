import csv
import os

# Location of input file
inputfile = os.path.join( '.', 'Resources', 'election_data.csv')
# Location of output file
outputdir = os.path.join( '.', 'output')
outputfile = os.path.join( outputdir, 'pypoll_output.txt')

# Initialize variables to be used in program
voteCount = 0
candidatesVotes = {}
winner = ('',0)

# Read file as CSV and parse for values as directed
with open(inputfile, newline='') as csvfile:
    inputfile = csv.reader(csvfile)
    next(inputfile)

    # Loop through CSV file and parse data
    for line in inputfile:
        if len(line) > 0:

            # Increase voteCount and increase number of votes for candidate 
            voteCount += 1
            if line[2] in candidatesVotes:
                candidatesVotes[ line[2] ] += 1
            else:
                candidatesVotes[ line[2] ] = 1

# Find candidate who received the most votes
for key, value in candidatesVotes.items():
    if  value > winner [1]:
        winner = (key, value)

# Print results to console
print( "Election Results" )
print( "__________________________" )
print( f"Total Votes: {voteCount}" )
print( "__________________________" )

# Print out all candidates, percentage of votes and vote count
for key, value in candidatesVotes.items():
    perc = (value / voteCount) * 100
    print( f"{key}: {perc:.3f}% ({value})" )

# Print winner of election
print( "__________________________" )
print( f"Winner: {winner[0]}" )
print( "__________________________" )

# Write output to text file
if not os.path.exists(outputdir):
    os.makedirs(outputdir)
with open(outputfile, 'w') as fout:
    print( "Election Results" , file=fout)
    print( "__________________________" , file=fout)
    print( f"Total Votes: {voteCount}" , file=fout)
    print( "__________________________" , file=fout)

    # Print out all candidates, percentage of votes and vote count
    for key, value in candidatesVotes.items():
        perc = (value / voteCount) * 100
        print( f"{key}: {perc:.3f}% ({value})", file=fout)

    # Print winner of election
    print( "__________________________" , file=fout)
    print( f"Winner: {winner[0]}" , file=fout)
    print( "__________________________" , file=fout)
