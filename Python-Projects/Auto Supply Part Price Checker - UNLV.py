#!/usr/bin/env python
# coding: utf-8

# # Happy Auto Supply Part Price Checker 
# 
# In this program, the user will enter the part number. The part number follows certain rules. Those being it can only be five characters, the first character should be "P" or "T", the second through fourth character should be a number, the second character should be between 1 and 5.  Once entered correctly, the program will then calculate the price of the part number. The initial price is always 85 dollars. If the first character of the part number is "T", the part number will cost an additional 75 dollars. If the second character in the part number is 3 or above, the part number gets charged an additional 25 dollars. If the last character is an "O", the system will multiply the current part number price by 3. The part number and price then get added to a dictionary. After, the program will ask if the user wants to enter another part number. If the user enters "y" or "Y" the process will begin again by asking for the part number and calculating the price. Once the user enters anything other than "y" or "Y" for the question asking if they want to enter another part number, display each part number entered along with the cost of each item.
# 
# * Input: The part number, Y/y to enter more part numbers, any input other than Y/y to end 
# * Output: Each part number entered along with the cost of each item 
# 
# * Author: Jordan Gillis 
# 
# * Date: 10/24/2023 

# In[ ]:


# create list to track the available characters that can be used for the first character in the part number
vehicleType = ('P','p','T','t')
# create list to track the available characters that can be used for the last character in the part number  
lastCharacter = ('M','m','o','O')
# create list to track the avaialble characters that can be used for the second character in the part number
secondCharacter = ('1','2','3','4','5')
# initialize value to inidicate the exact amount of characters the part number should be  
characterLimit = 5
# initialize the dictionary happy list as empty list
happyList = {}        
# initialize value indicating part number available
userAnswer = 'y'


# define the function to validate whether the part is under the right criteria 
def validate_part(partNumber):
    # initialize the error message as an empty message
    validationFail = ''
    # validate whether the first character is P, p, T, or t
    if not partNumber[0] in vehicleType:
        validationFail += 'The first character should be either P or T.\n'
    # validate whether the 2nd to 4th characters are numeric 
    if not partNumber[1:4].isdigit():
        validationFail += 'The 2nd to 4th characters should be numbers.\n'
    # validate whether the last character is M, m, O, or o
    if not partNumber[4] in lastCharacter:
        validationFail += 'The last character should be either M or O.\n'        
    # validate whether the second character is between 1 to 5    
    if not partNumber[1] in secondCharacter:
        validationFail += 'The 2nd character should be between 1 to 5.'        
    # validate whether the part number falls under any of the validation checks
    if validationFail: 
        print(validationFail)
        return False
    return True


# define the function to calculate the price of the part number 
def calculate_price(partNumber):
    # initialize the initial price as 85
    initialPrice = 85
    # determine if the first character is T or t
    if partNumber[0] in 'Tt':
        initialPrice += 75
    # determine if the second character is greater than or equal to 3
    if int(partNumber[1]) >= 3:
        initialPrice += 25
    # determine if the last character is O or o
    if partNumber[4] in 'Oo':
        initialPrice *= 3         
    return initialPrice


# define the function to generate the user output for the part number per price 
def print_total(itemsDict, leftWidth, rightWidth):
    print("\nAll the parts and the prices you just checked:")
    # for all the key-value pairs in the dictionary
    for k, v in itemsDict.items():
        # key is the part number, align the left 
        print(k.upper().ljust(leftWidth, '.')+("$"+str(v)).rjust(rightWidth))
        

# when there is data to be entered
while userAnswer.lower() in ['y', 'Y']:
    # ask for valid part number
    print("Please enter the part number: ")
    partNumber = input().strip()
    # when the character length is not equal to necessary character amount
    while len(partNumber) != characterLimit:
        print('The part number should be 5 digits.')
        print("Please enter again:")
        partNumber = input().strip()
    # when the part number is not valid
    while not validate_part(partNumber):
        print("Please enter again: ")
        partNumber = input().strip()
    # initialize the return function to equal the function created for days overdue amount
    price = calculate_price(partNumber)
    # assign the value to pair with the key
    happyList[partNumber] = price
    # show the part number and the price for the part number
    print('The part '+str(partNumber.upper())+' is $'+str(price))
    # ask for whether there are more product data to be entered
    print("Do you have more parts to check? (y/n)")
    userAnswer = input()
# call the print_total() method to display the part numbers and prices in the dictionary
print_total(happyList, 12, 5)



# In[ ]:





# In[ ]:




