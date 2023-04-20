
import os 
import csv
#Constructing path to both reading file and writing to a file 
csvpath = os.path.join('Resources', 'budget_data.csv')
output_path =  os.path.join('analysis', 'analysis.txt')
#declaring empty lists to store our data that we get from the csv file
Profit_loses_list = []
Date_list=[]
Inc_Deac_list=[]
#opening an output file 
with open(output_path, 'w') as f:
    f.write("Financial Analysis\n")
    f.write("------------------------------\n")
    #opening the csv file to read from 
    with open(csvpath) as csvfile:
        print("Financial Analysis")
        print("------------------------------")
        csvreader = csv.reader(csvfile,delimiter=',')
        csv_header = next(csvreader)
        #declaring index for profit/loses and date to itterate through the csv file and adding to the lists
        P_l= csv_header.index("Profit/Losses")
        Date = csv_header.index("Date")
        for row in csvreader: 
            Profit_loses_list.append(int(row[P_l]))
            Date_list.append(row[Date])
        for x in range(len(Profit_loses_list) -1):
            Inc_Deac_list.append(Profit_loses_list[x+1]- Profit_loses_list[x])
        #finding the index of a maximum value and minimum value in the inc_Deac_list 
        max_index = Inc_Deac_list.index(max(Inc_Deac_list))
        min_index = Inc_Deac_list.index(min(Inc_Deac_list))
    #printing and writing the results 
    print(f"Total Months: {len(Date_list)}")
    print (f"Total: ${sum(Profit_loses_list)}") 
    print(f"Average Change: ${round(sum(Inc_Deac_list)/len(Inc_Deac_list),2)}")
    print (f"Greatest Increase in Profits:  {Date_list[max_index +1]} (${Inc_Deac_list[max_index]})")  
    print (f"Greatest Decrease in Profits:  {Date_list[min_index + 1]} (${Inc_Deac_list[min_index]})")  
    f.write(f"Total Months: {len(Date_list)}\n")
    f.write(f"Total: {'${:}'.format(sum(Profit_loses_list))}\n") 
    f.write(f"Average Change: {'${:}'.format(round(sum(Inc_Deac_list)/len(Inc_Deac_list),2))}\n")
    f.write(f"Greatest Increase in Profits: {Date_list[max_index +1]} ({'${:}'.format(Inc_Deac_list[max_index])})\n")  
    f.write(f"Greatest Deacrease in Profits: {Date_list[min_index +1]} ({'${:}'.format(Inc_Deac_list[min_index])})\n")
 
