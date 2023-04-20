import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
output_path =  os.path.join('analysis', 'analysis.txt')
#Declaring empty lists 
Ballot_Id =[]
#opening an output file 
with open(output_path,'w') as f:
    f.write("Election Results\n")
    f.write("---------------------\n")
    #opening a csv file to read from 
    with open(csvpath) as csvfile:
        print("Election Results")
        print("---------------------")

