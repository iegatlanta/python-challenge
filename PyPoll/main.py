import os
import csv

#-----------------------------------------------



#election_data = os.path.join('..', 'Resources', 'election_data.csv')

election_data = os.path.join('Resources', 'election_data.csv')

#-----------------------------------------------
candidates = []
total_candidates = []
candidate_percentage = []
total_votes = []
#-----------------------------------------------
#electiondata = os.path.join('..', 'Resources', 'election_data.csv')

with open(election_data, 'r', newline='') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
#-----------------------------------------------
    header = next(csvreader)

    totalvote = 0
#-----------------------------------------------
    for row in csvreader:
        total_candidates.append(row[2])
        totalvote += 1

sortcandidate = sorted(total_candidates)
#-----------------------------------------------
for x in range(totalvote):
    if sortcandidate[x-1] != sortcandidate[x]:
        candidates.append(sortcandidate[x])
for z in range (len(candidates)):
    candidatecount = 0 

    for y in range (len(sortcandidate)):
        if candidates[z] == sortcandidate[y]:
            candidatecount += 1
    candidate_percentage.append(round(candidatecount / totalvote * 100, 1))
    total_votes.append(candidatecount) 
#-----------------------------------------------
print("Election Results")
print("------------------------")
print("Total Votes: " + str(totalvote))
print("------------------------")
#-----------------------------------------------
zipcandidates = zip(candidates, candidate_percentage, total_votes)  
for row in zipcandidates:
    print(row[0] + ":", str(row[1]) + "%", "(" + str(row[2]) + ")")

for s in range(len(candidate_percentage)):
    if total_votes[s] > total_votes[s-1]:
        winning_candidate = candidates[s]

#-----------------------------------------------
print("------------------------")  
print("Winner: ", str(winning_candidate))
print("------------------------") 
#-----------------------------------------------
textoutput = os.path.join('..', 'PyPoll', 'electionresults.txt')
with open (textoutput, 'w', newline='') as Elections:
    write = csv.writer(Elections)
    write.writerows([
            ["Election Results"],
            ["Total Votes: " + str(totalvote)],
            ["-----------------------------------"],
            ["-----------------------------------"],
            ["Winner: " + str(winning_candidate)],
            ["-----------------------------------"]
])