import csv
import os

max_change = "none"
min_change = "none"
min_month = "none"
max_month = "none"

total_months = 0
total_amount = 0
counter = 0
Sum_of_Monthly_Change = 0

Profit_Loss_List = []
Monthly_Change_List =[]
Months_List = []

budget_data_path = os.path.join("Resources","budget_data.csv")

with open(budget_data_path,"r",newline = "",encoding="utf-8") as budget_data_file:
    budget_data_reader = csv.reader(budget_data_file,delimiter=",")
    budget_data_header = next(budget_data_reader)

    for rows in budget_data_reader:
        total_months = total_months + 1
        Profit_Loss_List.append(rows[1])
        Months_List.append(rows[0])
        total_amount = int(total_amount) + int(rows[1])

number_of_stored_pl_values = len(Profit_Loss_List)

while counter < number_of_stored_pl_values-1:
    balance = int(Profit_Loss_List[int(counter)+1])-int(Profit_Loss_List[int(counter)])

    if max_change == "none":
        max_change = balance
        max_month = Months_List[int(counter+1)]
    elif balance > max_change:
        max_change = balance
        max_month = Months_List[int(counter+1)]

    if min_change == "none":
        min_change = balance
        min_month = Months_List[int(counter+1)]
    elif balance < min_change:
        min_change = balance
        min_month = Months_List[int(counter+1)]

    Monthly_Change_List.append(balance)
    counter = counter + 1

for value in Monthly_Change_List:
    Sum_of_Monthly_Change = Sum_of_Monthly_Change + value

Average_Change = (Sum_of_Monthly_Change/len(Monthly_Change_List))
Floated_Average_Change = "{:.2f}".format(Average_Change)
print(f"Total Months: {len(Profit_Loss_List)}")
print(f"Total: ${total_amount} ")
print(f"Average Change: ${Floated_Average_Change}")
print(f"Greatest Increase in Profits: {max_month}  (${max_change})")
print(f"Greatest Decrease in Profits: {min_month}  (${min_change})")

results_path = os.path.join("Analysis","Results.txt")

with open(results_path,"w", newline = "", encoding="utf-8") as my_txt_file:
    my_txt_file.write("Financial Analysis\n")
    my_txt_file.write("----------------------------------------------------------\n")
    my_txt_file.write(f"Total Months: {len(Profit_Loss_List)}\n")
    my_txt_file.write(f"Total: ${total_amount}\n")
    my_txt_file.write(f"Average Change: ${Floated_Average_Change}\n")
    my_txt_file.write(f"Greatest Increase in Profits: {max_month}  (${max_change})\n")
    my_txt_file.write(f"Greatest Decrease in Profits: {min_month}  (${min_change})\n")
    my_txt_file.write("----------------------------------------------------------\n")
