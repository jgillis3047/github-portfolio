#!/usr/bin/env python
# coding: utf-8

# # Average Height of US Presidents
# 
# This program reads the height data from a csv file and show the statistics.
# 
# Input: (read from a csv file)
# 
# Outout: Basic statistics of the height
# 
# Author: Jordan Gillis

# In[1]:


# import pandas, set the alias as pd
import pandas as pd
# import numpy, set the alias as np
import numpy as np

# read the csv file to read the data
data = pd.read_csv('president_heights.csv')
# use only the 'height(cm)' column to create a numpy array
heights = np.array(data['height(cm)'])

# Use the aggregations to show the statistics of the height
print("Mean height:       ",heights.mean())
print("Standard deviation:",heights.std())
print("Minimum height:    ",heights.min())
print("Maximum height:    ",heights.max())
print("25th percentile:   ",np.percentile(heights, 25))
print("Median:            ",np.median(heights))
print("75th percentile:   ",np.percentile(heights, 75))

# use tools in Matplotlib to visualize the data
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn; seaborn.set()  # set plot style
plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number');


# In[ ]:




