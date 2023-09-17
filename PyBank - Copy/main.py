#PyBank
# Modules
import os
import csv

#Initialize variables
row_ctr = 0
net_total = 0
change_list = []
counter = 0
# Initialize variables to hold the maximum and minimum values
gr_inc_profit = 0
gr_dec_profit = 0
#Initialize month variables
GIP_date = ""
GDP_date = ""
average_change = 0 

print("Financial Analysis")
print("--------------------------")
#  Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read the header row first
    csv_header = next(csvreader)
    
    for row in csvreader:
        #Create a running sum of number of rows in the file
        row_ctr = row_ctr + 1
        # Convert the value in the "Profit/Losses" column to an integer and add it to the total
        net_total += int(row[1])
    
        #Finding Greatest Increase in Profits & corresponding date
        #Finding Greatest Decrease in Profits & corresponding date
        if counter > 0:
            change_list.append(int(row[1]) - previous_amount)
            current_amount = int(row[1]) - previous_amount
            # Update the maximum and minimum values
            if (gr_inc_profit < current_amount):
                gr_inc_profit = current_amount 
                GIP_date = row[0] #Store date for Greatest Increase in Profit amount
            if (gr_dec_profit > current_amount):
                gr_dec_profit = current_amount
                GDP_date = row[0] #Store date for Greatest Decrease in Profit amount
        previous_amount = int(row[1])
        counter += 1

    #Print the number of rows in the file, which is same as the number of months
    print(f"Total Months: {row_ctr}")

    # Print the Net Total amount of Profit/Losses over the entire period
    print(f"Total: ${net_total}")

    #Find the Average Change
    average_change = round(sum(change_list)/len(change_list),2)
    print(f"Average Change: $ {average_change}")
    
    # Print the maximum and minimum values
    print("Greatest Increase in Profits: " + str(GIP_date) + " ($" + str(gr_inc_profit) + ")")
    print(("Greatest Decrease in Profits: " + str(GDP_date) + " ($" + str(gr_dec_profit) + ")"))

#Specifying the file to write to
output_path = os.path.join("analysis", "Bank_Analysis.txt")
#Opening file with write mode, specifying the variable to hold the contents
with open(output_path, 'w') as csvfile:
    #Initialize csv writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    #Writing first row to be printed
    csvwriter.writerow(['Financial Analysis'])

    #Writing next row
    csvwriter.writerow(['--------------------------'])
    #Writing next row
    csvwriter.writerow(['Total Months: ' + str(row_ctr)])
    #Writing next row
    csvwriter.writerow(['Total: $' + str(net_total)])
    csvwriter.writerow(["Average Change: $" + str(average_change)])
   
    csvwriter.writerow(["Greatest Increase in Profits: " + str(GIP_date) + " ($" + str(gr_inc_profit) + ")"])
    csvwriter.writerow(["Greatest Decrease in Profits: " + str(GDP_date) + " ($" + str(gr_dec_profit) + ")"])