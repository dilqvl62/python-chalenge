
import os 
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')
Profit_loses_list = []
Date_list=[]
Inc_Deac_list=[]
print("Financial Analysis")
print("------------------------------")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    P_l= csv_header.index("Profit/Losses")
    Date = csv_header.index("Date")
    for row in csvreader: 
        Profit_loses_list.append(int(row[P_l]))
        Date_list.append(row[Date])
    for x in range(len(Profit_loses_list) -1):
        Inc_Deac_list.append(Profit_loses_list[x+1]- Profit_loses_list[x])

    max_index = Inc_Deac_list.index(max())
    min_index = Inc_Deac_list.index(min(Inc_Deac_list))
    print(f"Total Months: {len(Date_list)}")
    print (f"Total: ${sum(Profit_loses_list)}") 
    print(f"Average Change: ${round(sum(Inc_Deac_list)/len(Inc_Deac_list),2)}")
    print (f"Greatest Increase in Profits:  {Date_list[max_index +1]} (${Inc_Deac_list[max_index]})")  
    print (f"Greatest Decrease in Profits:  {Date_list[min_index + 1]} (${Inc_Deac_list[min_index]})")  
   