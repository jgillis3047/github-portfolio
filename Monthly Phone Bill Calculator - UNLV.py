#!/usr/bin/env python
# coding: utf-8

# # Monthly Phone Bill Calculator 
# The user enters the Data Usage Last Month in Gigabytes and also enters the year the account opened. Calls and texts will always be 9.99 This program should show the monthly amount of calls and texts, data and total of calls and texts and data added together.
# 
# * Input: gigabyte Usage and Year Account Opened 
# 
# 
# 
# 
# 
# * Process: enter the Gigabyte and Year Account Opened
# 
# * if the year entered is between 2000 and 2023, proceed with Monthly Phone Bill Calculator 
# 
# * if the year entered is not between 2000 and 2023, print The Cell Phone Company Opened in 2023 and end the Monthly Phone Bill Calculator
# 
# * if the year entered is less than 2020 charge $9.50 dollars for every gigabyte data used
# 
# * if the year entered is between 2020 and 2022 charge $11.50 dollars for every gigabyte data used
# 
# * if the year entered is greater than 2022 charge $7.50 dollars for every gigabyte used
# 
# * get the data price by multiplying the yearly charge amount by the gigabyte usage amount 
# 
# * if the data price is greater than 40, then the data price will remain at 40
# 
# * if the data price is less than or equal to 40, the data price will remain multiplying the yearly charge amount by the gigabyte usage amount 
# 
# * get the total bill by adding $9.99 for calls and texts and the data price amount 
# 
# * print the monthly calls and texts, print the monthly data amount, and the monthly total bill and end the program.
# 
# 
# 
# 
# 
# * Output: the monthly amount of calls and texts, monthly amount of data and monthly total bill or incorrect year
# 
# 
# * Author: Jordan Gillis 
# 
# * Date: 09/26/2023

# In[3]:


# print program purpose 
print('The purpose of the program is to calculate the cell phone bill for customers of a cell phone company')

# get data usage from last month 
print('Please enter the data usage last month in Gigabyte(GB):')
gigabyteUsage = float(input())

# get year the account opened 
print('Please enter the year the account is opened: ')
yearOpened = float(input())

# verify the user input for year is between 2000 and 2023 
if yearOpened < 2024 and yearOpened > 1999: 
    
    # verify the user input for year is less than 2020 
    if yearOpened < 2020: 
        chargeAmount = 9.5 
        
    # if the user input for year is between 2020 and 2022 
    elif yearOpened >= 2020 and yearOpened <= 2022: 
        chargeAmount = 11.5 
        
    # else, the user input for year is greater than 2022
    else: 
        chargeAmount = 7.5 
        
    #calculate the data price 
    dataPrice = chargeAmount*gigabyteUsage 
        
    # check if the data price is greater than 40
    if dataPrice > 40:
        dataPrice = 40.00
        
    # else, the data price is less than or equal to 40 
    else: 
        dataPrice = chargeAmount * gigabyteUsage 
        
    # calculate the total monthly phone bill
    totalPhone = 9.99 + dataPrice 
    
    # define the formatter, making the data and total have two digits after the decimal 
    formatter = "{gg:,.2f}"
    
    # print the display result 
    print('Calls and Texts:     $9.99')
    print('Data:                $'+formatter.format(gg=dataPrice))
    print('Total:               $'+formatter.format(gg=totalPhone))
    
    
# else, print the display result 
else: 
    print('The Cell Phone company opened in year 2000.')


# In[ ]:





# In[ ]:




