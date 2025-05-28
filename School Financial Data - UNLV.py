#!/usr/bin/env python
# coding: utf-8

# # School Financial Data
# The objective of this program is to create a scatter plot to show multiple relationships. The scatter plot data should be found from the following files: SSF_2014_2016_00A01_with_ann.csv and STC_2016_00A2_with_ann.csv. With the data provided, the scatter plot should show the following relationships: the relationship between the tax income and expenditure of schools, the relationship of tax income and outstanding debt, and the relationship of tax income and total revenue, for each state in the United States in 2016. 
# 
# * Input: There is no physical input, data is retrieved and scatter plot is generated through the reading of the two files.
# 
# * Output: A scatterplot containing the relationship between the tax income and expenditure of schools, the relationship tax income and outstanding debt, and the relationship of the tax income and total revenue, for each state in the United States 2016. The scatter plot contains a title "Tax Income and School Finance 2016" and a legend highlighting the color associated with "Expenditure", "Outstanding Debt" and "Revenue".
# 
# * Author: Jordan Gillis
# * Date: 11/27/2023

# In[1]:


# import pandas, set the alias as pd
import pandas as pd 

# import numpy, set the alias as np
import numpy as np

# import the plyplot module, set the alias as plt
import matplotlib.pyplot as plt

# show the plot wih inline mode
get_ipython().run_line_magic('matplotlib', 'inline')

# read the csv files for the data
file2016Data = pd.read_csv('STC_2016_00A2_with_ann.csv')
fileData = pd.read_csv('SSF_2014-2016_00A01_with_ann.csv')

# filter the datasets to get the total taxes and 2016 
file2016TotalTaxes = file2016Data [file2016Data['Meaning of Tax Type'] == 'Total Taxes']
fileSSFData = fileData[fileData['Year'] == 2016]

# merge the STC data with the SSF data on 'Geographic area name'
merged2016 = pd.merge(file2016TotalTaxes, fileSSFData, on='Geographic area name')


# replace the missing data values with 0 from the csv files
merged2016 = merged2016.replace(np.nan, 0)


# select the relevant data for the scatter plot
taxIncome2016 = merged2016['Amount ($1,000)'] 
expenditure2016 = merged2016['Total expenditure ($1,000)']  
outstandingDebt2016 = merged2016['Debt outstanding at end of fiscal year ($1,000)'] 
totalRevenue2016 = merged2016['Total revenue ($1,000)'] 

# create the scatter plot
plt.figure(figsize=(10,6))

# plot revenue, outstanding debt, and expenditure with different colors for 2016
plt.scatter(taxIncome2016, totalRevenue2016, color= 'blue',label='Revenue', alpha= .3)
plt.scatter(taxIncome2016, outstandingDebt2016, color= 'orange', label='Outstanding Debt', alpha= .3)
plt.scatter(taxIncome2016, expenditure2016, color= 'green', label='Expenditure', alpha= .3)

# add title and axis labels
plt.title('Tax Income and School Finance 2016')
plt.xlabel('Tax Income ($1000)')
plt.ylabel('Total Revenue, Debt, and Expenditure ($1000)')

# display the legend in the lower right area of the scatter plot
plt.legend(loc='lower right')

# display the plot
plt.show()


# In[ ]:




