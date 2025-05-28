#!/usr/bin/env python
# coding: utf-8

# # State Tax Income 
# 
# The system will read the data files provided (FY2019.csv, FY2020.csv, FY2021.csv, FY2022-STC-Detailed-Table.csv and taxitemcodesanddescriptions.csv). This will in turn show the tax information for the specific state abbreviation entered and for the specific year entered. The tax numeric data for a specific year/ state will be reflected next to the specific tax description. 
# 
# * Input: The state abbreviation, the specific year of data they want to see
# * Output: The tax description along with the amount of state income tax for each tax description
# 
# * Author: Jordan Gillis
# * Date: 11/15/2023
# 
# 

# In[67]:


import pandas as pd
import numpy as np



# use the read_csv() funciton to read the data from five files into five DataFrames
yearTax19 = pd.read_csv('FY2019.csv')
yearTax20 = pd.read_csv('FY2020.csv')
yearTax21 = pd.read_csv('FY2021.csv')
yearTax22 = pd.read_csv('FY2022-STC-Detailed-Table.csv')
taxDescriptions = pd.read_csv('taxitemcodesanddescriptions.csv')

# add an additional column to each of the year data frames
yearTax19['Year'] = 2019
yearTax20['Year'] = 2020
yearTax21['Year'] = 2021
yearTax22['Year'] = 2022

# create a list of the years that tax data is available. 
fourYears = [2019, 2020, 2021, 2022]

# use concatenate to combine all of the year data frames 
combineYear = pd.concat([yearTax19, yearTax20, yearTax21, yearTax22])

# use replace function to remove any missing values where the tax is not present
combineYear = combineYear.replace(np.nan, 0)

# ask the user for the state abbreviation
print('Please enter the abbreviation of a state to see the tax information')
stateAbbrev = input().strip().upper()

# if the state abbreviation is not in combined data
while stateAbbrev not in combineYears:
    print('The state abbreviation is not valid, please enter again.')
    stateAbbrev = input().strip().upper()
    
# ask the user for the year
print('Please enter the year (2019, 2020, 2021, or 2022):')
yearSelected = int(input().strip())

# if the year is not 2019, 2020, 2021, or 2020
while yearSelected not in validYears:
    print('Currently, only the data for 2019, 2020, 2021, and 2022 are available, please enter again:')
    yearSelected = int(input().strip())


mask = combineYears['Year'] == yearSelected

stateData = combineYears.loc[mask, ['item', stateAbbrev]]


stateDataWithDescriptions = pd.merge(stateData, taxDescriptions, left_on='item', right_on='Item Code')
# stateDataWithDescriptions

# use fancy indexing to select the relevant columns for display and put it in the correct item order
finalData = stateDataWithDescriptions.set_index('Description').loc[:, [stateAbbrev]]
# finalData

# display the data 
print(finalData)




# In[ ]:





# In[ ]:





# In[ ]:




