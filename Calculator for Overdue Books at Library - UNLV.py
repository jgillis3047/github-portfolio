#!/usr/bin/env python
# coding: utf-8

# # Fine Calculator for Overdue Books at Library
# 
# In this program, the user will enter the number of books checked out. The program then calculates the fine per book. The fine amount charged for the first 10 days is 8 cents per day and then 15 cents per day for each additional day. For each book entry, the program will display the amount due right after the entry. The total fine amount for all the books are then displayed after each book is accounted for. Lastly, the user is prompted to ask if they want to get the fine amount for another patron.
# 
# * Input: Number of books checked out and number of days overdue per book.
# * Output: Fine per book and total fine for all of the books.
# 
# * Author: Jordan Gillis 
# 
# * Date: 10/3/2023 

# In[13]:


# define the function to calculate the fine amount for days overdue.The function should return a value.
def calculate_fine(daysOverdue, fine):
    if daysOverdue <= 10: 
        fine = daysOverdue * .08
    else:
        fine = 10 * .08 + (daysOverdue-10)* .15
        
    return fine

# initial condition 
userAnswer = 'y' 

# when the input value is 'y' or 'Y', get new patron's fine amount
while userAnswer == 'y' or userAnswer == 'Y':
    
    # format the output to only reflect two digits after the decimal point 
    formatter = '{gg:,.2f}'
    
    # get user input for the number of books checked out
    print('Please enter the number of books checked out: ')
    numberOfBooks = int(input())

    # initial conditions within while loop 
    books = 1
    fine = 0
    daysOverdue = 0
    total = 0

    # when the input value is not a postive number, show error message and ask for input again 
    while numberOfBooks < 0: 
        # get the user input for days overdue 
        print('The number of books checked out should be a positive number. Please enter again:')
        numberOfBooks = int(input())
        
    # when the input value is greater than or equal to the current book checker amount, ask for the days overdue 
    while numberOfBooks >= books: 
        # get the user input value for days overdue  
        print('For book '+str(books)+', please enter the number of days overdue.')
        daysOverdue = int(input())

        # when the input value is not a positive number, show error message and ask for input again
        while daysOverdue < 0:
            # get the user input for days overdue 
            print('The number of days overdue should be a positive number. Please enter again:')
            daysOverdue = int(input())
                      
        # initialize the return function to equal the function created for days overdue amount
        fine = calculate_fine(daysOverdue, fine)
        
        # display the overdue amount for the current book
        print('Book '+str(books)+': ' +str(daysOverdue)+' day(s) overdue, the fine is $'+formatter.format(gg=fine))
                
        # add current fine amount to total 
        total += fine
        
        # increase the book currently accounting for by 1 
        books += 1

    # display the total fine for all books
    print('The total fine for the patron is $'+formatter.format(gg=total))
    
    # get the user input deciding if they would like to get the fine amount for another patron
    print('Calculate the fine for another patron? (Y/y continue)')
    userAnswer = str(input())
    
    
    
    

    

    







# In[ ]:




