
import os 
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')
Total_Months = 0
net_total = 0
Profit_loses_list = []
print("Financial Analysis")
print("------------------------------")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    P_l= csv_header.index("Profit/Losses")
    Date = csv_header.index("Date")
    for row in csvreader:
        Total_Months +=1
        net_total += int(row[P_l])
        Profit_loses_list.append(row[P_l])
    print(f"Total Months: {Total_Months}")
    print (f"Total: ${net_total}") 
    print (f"Greatest Increase in Profits: {net_total}")  
   