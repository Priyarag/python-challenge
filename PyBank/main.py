#import dependencies
import pandas as pd

# Make a reference to the budget_data.csv file path
csv_name = "budget_data.csv"
# Import the budget_data.csv file as a DataFrame
budget_data_df = pd.read_csv(csv_name)
#print Financial Analysis header 
header_output = ("Financial Analysis\n----------------------------")
print (header_output)
#store the total months count to months variable
months = budget_data_df['Date'].count()
months_output = ("Total Months:"+str(months))
# print the count of total months
print(months_output)
#store the net total amount of "Profit/Losses" over the entire period to Total_profit_losses variable
Total_profit_losses = budget_data_df['Profit/Losses'].sum()
Total_output = ("Total: $" +str(Total_profit_losses))
#print the net total amount of "Profit/Losses" 
print(Total_output)
#store the changes between months in "Profit/Losses"  to a panda series using shift function
budget_data_df['Diff'] = budget_data_df['Profit/Losses'] - budget_data_df['Profit/Losses'].shift(1)
#store the average change in "Profit/Losses" to Avg_Change
Avg_Change = round(budget_data_df['Diff'].mean(),2)
Avg_Change_output = ("Average Change: $" +str(Avg_Change))
#print the Avg_Change
print(Avg_Change_output)
#store the Greatest Increase in Profits using max function
greatest_profit = int(budget_data_df['Diff'].max())
#get the month of the Greatest Increase in Profits 
##idxmax() function returns index of first occurrence of maximum over requested axis.
increase_month = budget_data_df['Date'].loc[budget_data_df['Diff'].idxmax()]
increase_month_output = ("Greatest Increase in Profits:"+increase_month +" ($"+str(greatest_profit)+")")
print(increase_month_output)
#store the Greatest Decrease in Profits using min function
greatest_Decrease = int(budget_data_df['Diff'].min())
#get the month of the Greatest Decrease in Profits 
decrease_month = budget_data_df['Date'].loc[budget_data_df['Diff'].idxmin()]
decrease_month_output = ("Greatest Decrease in Profits:"+decrease_month +" ($"+str(greatest_Decrease)+")")
print(decrease_month_output)
# Push the ouput results to a new CSV file
with open("budget_data.txt", "w+") as output:
	output.write(f'{header_output}\n{months_output}\n{Total_output}\n{Avg_Change_output}\n{increase_month_output}\n{decrease_month_output} ')

