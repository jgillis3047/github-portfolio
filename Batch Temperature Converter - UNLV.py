#!/usr/bin/env python
# coding: utf-8

# # Batch Temperature Converter 
# 
# Program Reads a file with some Fahrenheit temperatures. It converts the temperature Fahrenheit into Celcius. The result contains the day the temperature occured on along with celcius temperature, within the new output file created. 
# 
# * Input: Name of the file that contains the Fahrenheit temperature.
# * Output: Conversion result written in a file that contains the day and the celcius temperature.
# 
# * Author: Jordan Gillis
# 
# * Date: 2023-10-31

# In[2]:


# import numpy, set the alias as np
import numpy as np
import os

# define the formatter, making the data and total have two digits after the decimal 
formatter = '{gg:,.2f}'
# initial condition for days
days = 1

# get the name of the file with the original height
print('Please enter the name of the input file:')
inputFileName = input()

# if statement check to ensure the file name is present 
# if the file name is not present 
if not os.path.exists(inputFileName):
    print('The file does not exist')
# if the file name is present 
else: 
    print('Please enter the name of the output file:')
    outputFileName = input()
    
    # open the file and assign the file object 
    tempFile = open(inputFileName)
    # read the content as a whole to a string variable 
    content = tempFile.read()
    # close the file 
    tempFile.close()
    
    # split the string with \n as the separator, into a list 
    # use the list to create a NumPy array, convert the datatype to float16
    tempArray = np.array(content.split('\n'), dtype = 'float16')
    
    # FOR DEBUGGING: print all the temperature scores to see whether it is correct
    # print(tempArray)
    
    # apply the arithmetic ufunc to convert the temp 
    celcArray = np.round(tempArray-32)/1.8 # np.round() is used to round the number 
    
    # FOR DEBUGGING: print all the tempature scores to see what the celcius is 
    # print(celcArray)
    
    # open the output file in write mode
    convertedFile = open(outputFileName, 'w')
    
    
    # a loop to traverse the items in the array
    # use the size attribute of the array to determine the range
    for i in range(tempArray.size):
        # write to the file, use i to index the item in the array
        # write a new line character after for each temperature
        # increment the day count by 1 each loop 
        convertedFile.write('Day '+str(days)+':  '+formatter.format(gg=celcArray[i])+'\n')
        days += 1
        
        
    # close the output file 
    convertedFile.close()
    # show a confirm message to the user, indicating the file name. 
    print('Temperature converted. Please see '+outputFileName+' for the result.')
    
    


# In[ ]:




