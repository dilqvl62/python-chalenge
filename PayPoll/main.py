import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
output_path =  os.path.join('analysis', 'analysis.txt')
#Declaring empty lists 
votes_list =[]
#initialize a list 
Candidate_list=[]
#opening an output file 
with open(output_path,'w') as f:
    f.write("Election Results\n")
    f.write("---------------------\n")
    #opening a csv file to read from 
    with open(csvpath) as csvfile:
        print("Election Results")
        print("---------------------")
        csvreader = csv.reader(csvfile,delimiter=',')
        csv_header = next(csvreader)
        #Declaring index of the header list 
        
        Cand = csv_header.index("Candidate")
        #creating a list of all votes by candidate 
        for row in csvreader:
            votes_list.append(row[Cand])

        print(f" Total Votes: {len(votes_list)}")
        print("----------------------------------")
        
        #create a list of every candidate in a given list      
        # by itterate through all elements in a given list
        for v in votes_list:
            if v not in Candidate_list:
                Candidate_list.append(v)
        
        # Calculating the percentage of votes each candidate won 
        for x in Candidate_list:
            print(f"{x} : {'{0:}%'.format(round((votes_list.count(x)/len(votes_list))*100,3))} ({votes_list.count(x)})")

