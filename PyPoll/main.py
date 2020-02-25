#First we will import the os module
import os 

#Module for reading CSV files
import csv

#Initialize variables
totalV = 0
kcount = 0
ccount = 0
lcount = 0
ocount = 0
max_votecount = 0

#% calculation function
def percentage (p, w):
    return 100 * float(p)/float(w)

#CSV reader specifies delimiter and variable that holds contents/opening
csvpath = os.path.join('..','pypoll','resources','election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        voterid = row[0]
        county = row[1]
        candidate = row[2]
        totalV = totalV + 1 

#votecount for each class of candidates
        if candidate =="Khan": 
            kcount = kcount + 1
        if candidate =="Correy":
            ccount = ccount + 1
        if candidate =="Li":
            lcount = lcount + 1
        if candidate =="O'Tooley":
            ocount = ocount + 1

#candidate and votes list 
candidatevote = {"Khan":kcount,"Correy":ccount, "Li":lcount,"O'Tooley":ocount}

# Find winner
for candidate, value in candidatevote.items():
    if value > max_votecount:
        max_votecount = value
        winner = candidate

#results
print(f"Election Results")
print(f"-----------------------------")
print(f"Total Votes: {totalV}")
print(f"-----------------------------")
print(f"Khan: {percentage(kcount,totalV):3f}% ({kcount})")
print(f"Correy: {percentage(ccount,totalV):3f}% ({ccount})")
print(f"Li: {percentage(lcount,totalV):3f}% ({lcount})")
print(f"O'Tooley: {percentage(ocount,totalV):3f}% ({ocount})")
print(f"-----------------------------")
print(f"Winner: {winner}")
print(f"-----------------------------")
