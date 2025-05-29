#!/usr/bin/env python
# coding: utf-8

# # Player Salary Data
# 
# The program reads data from a csv files, representing data of NBA players' salaries in different years. This program can show the salary for a certain year, and allows the user to update the salary.
# 
# Author: Jordan Gillis

# In[2]:


# import pandas, set the alias as pd
import pandas as pd
# import numpy, set the alias as np
import numpy as np

# use the read_csv() funcito to read the data from three file into three DataFrame
# Note: The files should be at the same directory as the program
salary = pd.read_csv('player-salary.csv')
# salary

# set index to player's name
salary = salary.set_index('PLAYER')

# prompt the user to enter a player's name
print("Please enter a player's name: ")
playerName = input().strip()


# if the name does not exist, show error
if playerName not in salary.index:
    print("Can't find the data for the player", playerName)
# if the name exists    
else:
    # ask the user which year of data to see
    print("Which year of salary? 2022/23,2023/24,2024/25, or 2025/26?")
    year = input()
    # input validation 
    while year not in('2022/23','2023/24','2024/25', '2025/26'):
        print('Please enter a valid year. 2022/23,2023/24,2024/25, or 2025/26? ')
        year = input()

    # show the value from the cell.
    print('the salary is $', salary.loc[playerName, year])
    
    # ask the user whether they would like to update the salary
    print('Please enter the udpated salary. Enter -1 if you do not wish to update the value.')
    newValue = int(input())
    # if the user did not enter -1
    if newValue != -1:
        # update the cell value
        salary.loc[playerName, year]= newValue

        # write back to the csv file
        salary.to_csv('player-salary.csv')
        
        #print confirmation
        print('value updated.')


# In[ ]:





# In[ ]:




