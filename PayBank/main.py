
import os 
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')
Total_Months = 0
print("Financial Analysis")
print("------------------------------")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)



    for row in csvreader:
        Total_Months +=1
    print(f"Total Months: {Total_Months}")
        
   