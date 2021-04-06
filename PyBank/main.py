
# Import os and csv
import csv
import os


Months = 0
Profits = []
Dates = []


#Read the CSV
with open("Resources/budget_data.csv", newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)


#Count the number of non-header rows
    for row in csvreader:
        Months += 1
        Dates.append(row[0])
        Profits.append(float(row[1]))


#and then load all the values into two lists
TotalProfits = Profits[0]
TotaledChanges = 0
BigInc = 0
BigDec = 0


#Begin with 1 to calculate the change in profit
for n in range (1, Months):
    #Add current month's profit to total profits
    TotalProfits += Profits[n]
    
    
    #Calculate the change between this month and the month before. Add to the totaled changes.
    CurrentChange = Profits[n] - Profits[n-1]
    TotaledChanges += CurrentChange
    
    
    #Check if the current change was the biggest increase or decrease and if so, 
    #make it the one with the biggest change
    if CurrentChange > BigInc:
        BigInc = CurrentChange
        BigIncDate = Dates[n]
    elif CurrentChange < BigDec:
        BigDec = CurrentChange
        BigDecDate = Dates[n]


#Print the final results
print("Financial Analysis")
print("----------------------------")
print(f"Months: {Months}")
print(f"Total Profits: ${(TotalProfits):.2f}")
print(f"Average Change: ${(TotaledChanges/(Months - 1)):.2f}")
print(f"Greatest Increase in Profits: {BigIncDate} (${(BigInc):.2f})")
print(f"Greatest Decrease in Profits: {BigDecDate} (${(BigDec):.2f})")

#Output final results to txt file
with open("Financial_Analysis.txt","w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Months: {Months}\n")
    txtfile.write(f"Total Profits: ${(TotalProfits):.2f}\n")
    txtfile.write(f"Average Change: ${(TotaledChanges/(Months - 1)):.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {BigIncDate} (${(BigInc):.2f})\n")
    txtfile.write(f"Greatest Decrease in Profits: {BigDecDate} (${(BigDec):.2f})\n")
    txtfile.write("----------------------------\n")