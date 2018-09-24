#A program to calculate and display projected profit based on entered
#projected sales
#09/23/2018
#CTI-110 P2T1 - Sales Prediction
#Stephen Romine
#
#Enter projected sales
total_sales = float (input ('Enter the projected sales: '))
#Calculate the profit as 23 percent of the total sales
profit = total_sales * 0.23
#Display the profit
print ('The profit is $', format (profit, ',.2f'))
