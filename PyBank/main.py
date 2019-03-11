#import dependencies
import pandas as pd
import subprocess

# Make a reference to the budget_data.csv file path
csv_name = "budget_data.csv"
# Import the budget_data.csv file as a DataFrame
budget_data_df = pd.read_csv(csv_name)
#budget_data_df
header_output = ("Financial Analysis\n----------------------------")
print (header_output)

months = budget_data_df['Date'].count()
months_output = ("Total Months:"+str(months))
print(months_output)
Total_profit_losses = budget_data_df['Profit/Losses'].sum()
Total_output = ("Total: $" +str(Total_profit_losses))
print(Total_output)
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
budget_data_df['Diff'] = budget_data_df['Profit/Losses'] - budget_data_df['Profit/Losses'].shift(1)
Avg_Change = round(budget_data_df['Diff'].mean(),2)
Avg_Change_output = ("Average Change: $" +str(Avg_Change))
print(Avg_Change_output)
greatest_profit = budget_data_df['Profit/Losses'].max()
increase_month = budget_data_df['Date'].loc[budget_data_df['Profit/Losses'].idxmax()]
increase_month_output = ("Greatest Increase in Profits:"+increase_month +"($"+str(greatest_profit)+")")
print(increase_month_output)
greatest_Decrease = budget_data_df['Profit/Losses'].min()
decrease_month = budget_data_df['Date'].loc[budget_data_df['Profit/Losses'].idxmin()]
decrease_month_output = ("Greatest Decrease in Profits:"+decrease_month +"($"+str(greatest_Decrease)+")")
print(decrease_month_output)
# Push the remade DataFrame to a new CSV file
with open("budget_data.txt", "w+") as output:
	output.write(f'{header_output}\n{months_output}\n{Total_output}\n{Avg_Change_output}\n{increase_month_output}\n{decrease_month_output} ')

