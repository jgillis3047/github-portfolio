#!/usr/bin/env python
# coding: utf-8

# # Reward Points Calculation
# 
# The program reads the customer's spending data for three different columns(grocery, food, and other) from two seperate files. The program will display how many customer records are present for each file. The program then combines the data files into one set and calculates the reward points that should be granted to each customer based on the following rules: Every 10 dollars spent on groceries is 1 point, every 5 dollars spent on food is 1 point, every 20 dollars spent in other categories is 1 point. After the calculation is performed, the program then displays the mean, standard deviation, and median of the points earned by the customer. It will then also show many customers are in each tier based on the following rules: Platinum customers have atleast 650 points; Gold customers have atleast 550 points but less than 650 points; and Silver customers have atleast 400 points but less than 550 points.
# 
# * Input: There is no manual entry. The problem should be able to handle different files as long as the files are named as customer_spending_UT.csv. & customer_spending_NV.csv.
# 
# * Output: The total spending records for both Utah and Nevada, the mean points earned, the standard deviation of points earned, the median of the points earned, the amount of platinum customers, the amount of gold customers, and the amount of silver customers. 
# 
# * Author: Jordan Gillis
# * Date: 2023-11-07

# In[1]:


# import pandas and numpy
import pandas as pd
import numpy as np


# define the formatter to ensure the numeric output only has two digits after decimal
formatter = '{gg:,.2f}'


# read the csv files to gather the data 
nvGroceryData = pd.read_csv('customer_spending_NV.csv')['grocery'].values
nvFoodData = pd.read_csv('customer_spending_NV.csv')['food'].values
nvOtherData = pd.read_csv('customer_spending_NV.csv')['other'].values
utGroceryData = pd.read_csv('customer_spending_UT.csv')['grocery'].values
utFoodData = pd.read_csv('customer_spending_UT.csv')['food'].values
utOtherData = pd.read_csv('customer_spending_UT.csv')['other'].values


# concatenate the arrays for both files to combine grocery, food, and other data
combinedGrocery = np.concatenate((nvGroceryData,utGroceryData))
combinedFood = np.concatenate((nvFoodData,utFoodData))
combinedOther = np.concatenate((nvOtherData,utOtherData))


# create NumPy arrays to get the points from the CSV combined data
groceryPoints = combinedGrocery / 10
foodPoints = combinedFood / 5
otherPoints = combinedOther / 20

# The point arrays are then broadcasted into one array to get the total array
# in order to get the total points 
pointsArray = groceryPoints + foodPoints + otherPoints


# calculate and assign the number of customers in each reward tier 
platinumCustomers = np.sum(pointsArray >= 650)
goldCustomers = np.sum((pointsArray >= 550) & (pointsArray < 650))
silverCustomers = np.sum((pointsArray >= 400) & (pointsArray < 550))


# print the amount of customer records for Utah and Nevada 
print("There are "+str(utGroceryData.size)+" spending records for Utah customers.")
print("There are "+str(nvGroceryData.size)+" spending records for Nevada customers.\n")

# print the mean, standard deviation, and median for the total points 
print("The mean of the points earned is: ".ljust(50)+formatter.format(gg=pointsArray.mean()).rjust(10))
print("The standard deviation of the points earned is: ".ljust(50)+formatter.format(gg=pointsArray.std()).rjust(10))
print("The median of the points earned is: ".ljust(50)+formatter.format(gg=np.median(pointsArray)).rjust(10)+"\n")

# print the amount of customers that align for each tier 
print("Platinum Customers: ".ljust(20)+str(platinumCustomers).rjust(10))
print("Gold Customers: ".ljust(20)+str(goldCustomers).rjust(10))
print("Silver Customers: ".ljust(20)+str(silverCustomers).rjust(10))



# In[ ]:




