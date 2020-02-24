#First we will import the os module
import os
#Module for reading CSV files
import csv
#Initialize variables
mcount = 0 
total = 0
PreValue = 0 
Diff = 0 
Max = 0 
Min = 0
# CSV reader specifies delimiter and variable that holds contents/opening
csvpath = os.path.join('..', 'PyBank','resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for i in csvreader:
         month = i[0]
         Amount = i[1]
         iAmount = int(Amount)
         Diff =  iAmount - PreValue
         #Placeholder to track greatest increase in p for FA
         if Max < Diff:
            Max = Diff
            MaxDate = month
         #Placeholder to track greatest decrease in p for FA
         if Min > Diff:
            Min = Diff
            MinDate = month
         PreValue = iAmount
         #total months FA
         mcount = mcount + 1
         total += int(Amount)

#Results 
print(f"Financial Analysis")
print(f"----------------------------")
#The total # of months included in the dataset
print(f"Total Month : {mcount}")
#The total net amount of “P/L” over the entire period
print(f"Total: $ {total}")
# Greatest increase in p
print(f"Greatest Increase in Profits: {MaxDate} : ($ {Max}")
# Greatest increase in p
print(f"Greatest Decrease in Profits: {MinDate} : ($ {Min}")
