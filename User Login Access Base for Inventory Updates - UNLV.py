#!/usr/bin/env python
# coding: utf-8

# # ITSMASH PROGRAM
# This program allows users (based upon their login access) to add inventory, add sales, or modify either
# 
# Input: various user options
# 
# Output: modified stock and salesHistory files and/or respective graphs
# 
# * Author: Jordan Gillis
# * Date: 12/5/23

# In[18]:


#funtion to help validate inputs
def validate_input(display,validInputs):
    while True:
        print(display)
        user= input().strip().upper()
        if user in validInputs:
            return user
        else:
            print(f'Input invalid. Please enter one of the following: {", ".join(validInputs)}')

def load_csv_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while loading the file: {e}")
        return None

def check_stock(stock, prod_id):
    #check if the product already exist in the stock CSV
    prod_id = int(prod_id)
    product = stock[stock['productID'] == prod_id]
    if product.empty:
        return False
    return True

def get_sell_price(stock, prod_id):
    #check if the product already exist in the stock CSV
    prod_id = int(prod_id)
    product = stock[stock['productID'] == prod_id]
    return(product['sellingPrice'].iloc[0])

def add_stock(stock, user_prod_id, selling_price, user_prod_quantity):
    #add the new product into the stock dataset csv
    new_stock = stock

    new_item = pd.DataFrame({
        'productID': [user_prod_id],
        'sellingPrice': [f"${(selling_price)}"],
        'quantity': [user_prod_quantity]
    })
    new_stock = pd.concat([new_stock, new_item], ignore_index=True)
    #write this new stock back out to the real csv file on the computer
    new_stock.to_csv('stock.csv', index = False)
    return new_stock

def update_stock_quantity(stock, user_prod_id, user_prod_new_quantity):
    #find prod by id & update quantity
    stock.loc[stock['productID'] == user_prod_id, 'quantity'] += user_prod_new_quantity

    #write this new stock back out to the real csv file on the computer
    stock.to_csv('stock.csv', index = False)

def plot_sales_trend(product_sales):
    
    #TO ADDRESS BUG THIS IS A FIX
    product_sales = product_sales.copy()
    product_sales.sort_values('salesDate', inplace=True)

    #PLOT THE HISTORICAL DATA SALES TREND BY DATE CONFIG
    plt.figure(figsize=(10, 6))
    plt.plot(product_sales['salesDate'], product_sales['sale'], marker='o')
    plt.title(f'Sales Trends')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    #DISPLAY THE GRAPH
    plt.show()   

def clean_currency(x):
    #REMOVE NON-NUMERIC CHARACTERS AND CONVERT TO FLOAT
    if isinstance(x, str):
        return float(x.replace('$', '').replace(',', ''))
    return x

def get_quantity_for_product(df, product_id):
    try:
        # Convert the input product_id to an integer
        product_id_int = int(product_id)

        # Filter the DataFrame for the specific product ID
        filtered_df = df[df['productID'] == product_id_int]

        # Check if the product ID is found
        if not filtered_df.empty:
            quantity = filtered_df['quantity'].iloc[0]
            return quantity
        else:
            return "Product ID not found"
    except ValueError:
        # Handle the case where the input cannot be converted to an integer
        return "Invalid product ID format. Please enter a valid number."
    
def update_sales_history(sales_history, order_id, date, prod_id, qty_sold, sale_amount):
    #add the new sale transaction into sales_history dataset csv
    new_sales = sales_history

    new_item = pd.DataFrame({
        'orderID': [order_id],
        'salesDate': [date],
        'productID': [prod_id],
        'quantity': [qty_sold],
        'sale': [f"${(sale_amount)}"]
    })

    new_sales = pd.concat([new_sales, new_item], ignore_index=True)

    #write this new sales transaction back out to the real csv file on the computer
    new_sales.to_csv('salesHistory.csv', index = False)
    return new_sales

def get_conv_rate(foreign_currency, selected_foreign_currency):
    try:
        # Filter the DataFrame for the specific product ID
        filtered_df = foreign_currency[foreign_currency['currency'] == selected_foreign_currency]

        # Check if the product ID is found
        if not filtered_df.empty:
            conv_rate = filtered_df['conversionRate'].iloc[0]
            return conv_rate
        else:
            return "Currency type not found"
    except ValueError:
        # Handle the case where the input cannot be converted to an integer
        return "Invalid currency. Please enter a valid currency name."

def selling_agent(stock, sales_history, foreign_currency):
    print(f"\nThe following products are available\n")
    print(stock)

    user_prod_id = input("\nEnter Product ID being sold (blank to end): ")
    while user_prod_id != '':
        order_ID= salesHistory['orderID'].max()+1
        order_date= (date.today()).strftime("%m/%d/%Y")
        while not user_prod_id.isnumeric():
            print('productID should be a number, please re-enter the product ID:')
            user_prod_id= input().strip()
        while float(user_prod_id) not in stock['productID'].values:
            print('productID not found. Please re-enter an existing productID:')
            user_prod_id= input().strip()
        user_prod_id= float(user_prod_id)
        print('Quantity being sold:')
        sold_quantity= input().strip()
        while not sold_quantity.isnumeric():
            print('Quantity should be a number, please re-enter the quantity:')
            sold_quantity= input().strip()
        while float(sold_quantity) > stock.loc[stock['productID']==user_prod_id,'quantity'].values:
            print('Quantity sold exceeds quantity on hand, please use a lower amount:')
            sold_quantity= input().strip()
        responseList= ['Y','N']
        response= validate_input('Do you want to use suggested selling prices? (Y/N):',responseList)
        if response == 'Y':
            sell_price= stock.loc[stock['productID']==user_prod_id,'sellingPrice'].values
            final_sale= float(sold_quantity)*float(sell_price)
            salesHistory.loc[len(salesHistory.index)]=[order_ID,order_date,user_prod_id,sold_quantity,final_sale]
            stock.loc[stock['productID']==float(user_prod_id), 'quantity'] = stock['quantity'] - float(sold_quantity)
        elif response == 'N':
            user_selling_price = input("\nEnter custom selling price per unit: ")
            while not user_selling_price.isnumeric():
                print('Custome selling price should be a numeric value. Please enter again:')
                user_selling_price = input("\nEnter custom selling price per unit: ")
            sale = float(sold_quantity) * float(user_selling_price)
            foreignResponseList= ['Y','N']
            foreign_currency_response= validate_input('Is sale in foreign currency? (Y/N):',foreignResponseList)
            if foreign_currency_response == 'N':
                final_sale=float(sale)
                salesHistory.loc[len(salesHistory.index)]=[order_ID,order_date,user_prod_id,sold_quantity,final_sale]
                stock.loc[stock['productID']==float(user_prod_id), 'quantity'] = stock['quantity'] - float(sold_quantity)
            elif foreign_currency_response == 'Y':
                currencyList= foreignCurrency['currency'].values
                selected_foreign_currency= validate_input('Enter foreign currency:',currencyList)
                conv_rate = foreignCurrency.loc[foreignCurrency['currency']==selected_foreign_currency,'conversionRate'].values
                final_sale = ((float(sold_quantity) * float(user_selling_price))/float(conv_rate))
                salesHistory.loc[len(salesHistory.index)]=[order_ID,order_date,user_prod_id,sold_quantity,final_sale]
                stock.loc[stock['productID']==float(user_prod_id), 'quantity'] = stock['quantity'] - float(sold_quantity)
        user_prod_id = input("\nEnter Product ID being sold (blank to end): ")

    #CONVERT SALESDATE TO DATETIME FORMAT AND SALES TO NUMERIC AFTER CLEANING
    sales_history['salesDate'] = pd.to_datetime(sales_history['salesDate'])
    sales_history['sale'] = sales_history['sale'].apply(clean_currency)

    # Calculate the mean of the sales
    mean_sale = sales_history['sale'].mean()
    # Find the top sale
    top_sale = sales_history.loc[sales_history['sale'].idxmax()]
    # most popular product
    most_popular_product = sales_history['productID'].value_counts().idxmax()

    # Output the bullet points
    print(f"• Mean Sale: {mean_sale:.2f}")
    print(f"• Top Sale: {top_sale['sale']} on {top_sale['salesDate'].date()}")
    print(f"• Most Popular Product ID: {most_popular_product}")
    
    plot_sales_trend(sales_history)



def buying_agent(stock):
    response= 'null'
    print(stock)
    #PROMPT THE USER TO ENTER A NEW ITEM
    while response != '':
        responseList= ['Y','N','']
        response= validate_input('Add new item? (Y/N or blank to finish entry):',responseList)
        if response == "Y":
            print(f"You entered (Y)")
            prod_id_not_valid = True

            #Ask user for product id
            user_prod_id = input("\nEnter Product ID (Must be 4 digits):")
            while not user_prod_id.isnumeric():
                print('product ID should be a number, please re-enter the new product ID:')
                user_prod_id= input().strip()
            while float(user_prod_id) in stock['productID'].values:
                print('productID entered is taken, please enter a new productID:')
                user_prod_id= input().strip()
            while len(user_prod_id) != 4:
                print('productID must be 4 characters, please enter a new productID:')
                user_prod_id= input().strip().upper()
            user_prod_id=float(user_prod_id)
            user_buy_price = input("\nEnter Buying Price: ")
            while not user_buy_price.isnumeric():
                print('Buying price should be a number. Please enter again:')
                user_buy_price = input("\nEnter Buying Price: ")
            user_buy_price= float(user_buy_price)
            user_prod_quantity = input("\nEnter Product Quantity: ")
            while not user_prod_quantity.isnumeric():
                print('Quantity should be a number. Please enter again:')
                user_prod_quantity = input("\nEnter Product Quantity: ")
            user_prod_quantity= float(user_prod_quantity)
            # calculate sell price
            selling_price = round((user_buy_price * 1.7), 2)
            stock.loc[len(stock.index)]=[user_prod_id,selling_price,user_prod_quantity]

        elif response == 'N':
            print(f"\nYou are updating an existing product")
            user_prod_id = input("\nEnter Product ID to be updated: ")
            while not user_prod_id.isnumeric():
                print('product ID should be a number, please re-enter the new product ID:')
                user_prod_id= input().strip()
            while float(user_prod_id) not in stock['productID'].values:
                print('productID not found. Please re-enter an existing productID:')
                user_prod_id= input().strip()
 
            #Ask for the new product quantity
            user_prod_new_quantity = input("\nEnter Product Quantity: ")
            while not user_prod_new_quantity.isnumeric():
                print('Quantity should be a number. Please enter again:')
                user_prod_new_quantity = input("\nEnter Product Quantity: ")
            user_prod_new_quantity= int(user_prod_new_quantity)
            stock.loc[stock['productID']==float(user_prod_id), 'quantity'] = stock['quantity'] + int(user_prod_new_quantity)

    print('You entered blank to see graph')
    # Creating the bar chart that shows inventory levels by product
    plt.figure(figsize=(10, 6))
    plt.bar(stock['productID'], stock['quantity'], color='skyblue')
    plt.xlabel('Product ID')
    plt.ylabel('Quantity')
    plt.title('Quantity of Each Product')
    plt.show()

#Import Modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date

#Import Data
salesHistory= pd.read_csv('salesHistory.csv')
stock= pd.read_csv('stock.csv')
credentials= pd.read_csv('credentials.csv')
foreignCurrency= pd.read_csv('foreignCurrency.csv')

#ask user for their credentials
print('Enter username:')
username= input().strip()
print('Enter password:')
password= input().strip()

#create unique pair to ensure username and password match
combined= username+","+password
credentials['union']=credentials['username']+","+credentials['password']

#validate that the username and password exist
while combined not in credentials['union'].values:
    print('Username or password is incorrect.')
    print('Enter username:')
    username= input()
    print('Enter password:')
    password= input()

#extract only the user's row
userAccess= credentials.loc[credentials['union']==combined]

#initialize values
action= 'null'
modify= 'null'


#if the user has admin credentials, they will flow down this path
if 'Admin' in userAccess['access'].values:
    #print stock and salesHistory dataframes
    print(stock)
    print(salesHistory)
    #ask user which action they would like to take
    while modify != '':
        modify= 'null'
        action= 'null'
        #input validation
        modifyList= ['STOCK','SALES','']
        modify= validate_input('Modify stock or sales (blank to end):',modifyList)
        #if user chooses stock
        if modify== 'STOCK':
            #while loop to continue code until user says return
            while action != 'RETURN':
                #input validation
                actionList= ['ADD','UPDATE','DELETE','RETURN']
                action= validate_input('Select action (add,update,delete,return):',actionList)
                #if the user picks the "add" option
                if action== 'ADD':
                    print('Add productID (4 numbers):')
                    newID= input().strip()
                    while not newID.isnumeric():
                        print('product ID should be a number, please re-enter the new product ID:')
                        newID= input().strip()
                    while float(newID) in stock['productID'].values:
                        print('productID entered is taken, please enter a new productID:')
                        newID= input().strip()
                    while len(newID) != 4:
                        print('productID must be 4 characters, please enter a new productID:')
                        newID= input().strip().upper()
                    newID= float(newID)
                    print('Add buying price:')
                    buyingPrice= input().strip()
                    while not buyingPrice.isnumeric():
                        print('buying price should be a number, please re-enter the buying price:')
                        buyingPrice= input().strip()
                    newSellingPrice= float(buyingPrice)*1.7
                    print('Add item quantity:')
                    newQuantity= input().strip()
                    while not newQuantity.isnumeric():
                        print('Quantity should be a number, please re-enter the quantity:')
                        newQuantity= input().strip()
                    newQuantity= float(newQuantity)
                    stock.loc[len(stock.index)]=[newID,newSellingPrice,newQuantity]
                #if the user picks the "update" option
                elif action== 'UPDATE':
                    print('productID to be updated:')
                    updatedID= input().strip()
                    while float(updatedID) not in stock['productID'].values:
                        print('productID not found. Please re-enter an existing productID:')
                        updatedID= input().strip()
                    print('New buying price:')
                    updatedPrice= input().strip()
                    while not updatedPrice.isnumeric():
                        print('New price should be a number, please re-enter the new price:')
                        updatedPrice= input().strip()
                    updatedSellingPrice= float(updatedPrice)*1.7
                    print('Update item quantity:')
                    updatedQuantity= input().strip()
                    while not updatedQuantity.isnumeric():
                        print('Quantity should be a number, please re-enter the quantity:')
                        updatedQuantity= input().strip()
                    updatedID= float(updatedID)
                    stock.loc[stock['productID']==float(updatedID), ['productID','sellingPrice','quantity']]=[float(updatedID),float(updatedSellingPrice),float(updatedQuantity)]
                #if the user picks the "delete" option
                elif action== 'DELETE':
                    print('Enter productID you would like to delete:')
                    deleteID= input().strip()
                    while float(deleteID) not in stock['productID'].values:
                        print('productID not found. Please re-enter an existing productID:')
                        deleteID= input().strip()
                    deleteID= float(deleteID)
                    stock= stock.drop(stock[stock['productID']==deleteID].index)
        #if user chooses sales
        elif modify== 'SALES':
            #while loop to continue code until user says return
            while action != 'RETURN':
                actionList= ['ADD','UPDATE','DELETE','RETURN']
                action= validate_input('Select action (add,update,delete,return):',actionList)
                #if the user picks the "add" option
                if action== 'ADD':
                    addID= salesHistory['orderID'].max()+1
                    addDate= (date.today()).strftime("%m/%d/%Y")
                    print('Enter the productID of the product being sold:')
                    addProductID= float(input().strip())
                    while float(addProductID) not in stock['productID'].values:
                        print('productID not found. Please re-enter an existing productID:')
                        addProductID= float(input().strip())
                    print('Quantity being sold:')
                    addQuantity= input().strip()
                    while not addQuantity.isnumeric():
                        print('Quantity should be a number, please re-enter the quantity:')
                        addQuantity= input().strip()
                    while float(addQuantity) > stock.loc[stock['productID']==addProductID,'quantity'].values:
                        print('Quantity sold exceeds quantity on hand, please use a lower amount:')
                        addQuantity= input().strip()
                    itemSellPrice= stock.loc[stock['productID']==addProductID,'sellingPrice'].values
                    addSale= float(addQuantity)*float(itemSellPrice)
                    salesHistory.loc[len(salesHistory.index)]=[addID,addDate,addProductID,addQuantity,addSale]
                    stock.loc[stock['productID']==float(addProductID), 'quantity'] = stock['quantity'] - float(addQuantity)
                #if the user picks the "update" option
                elif action== 'UPDATE':
                    print('orderID to be updated:')
                    orderUpdateID= input().strip()
                    while float(orderUpdateID) not in salesHistory['orderID'].values:
                        print('orderID not found. Please re-enter an existing orderID:')
                        orderUpdateID= input().strip()
                    orderUpdateID= float(orderUpdateID)
                    print('productID being sold')
                    updateProductID= input().strip()
                    while float(updateProductID) not in stock['productID'].values:
                        print('productID not found. Please re-enter an existing productID:')
                        updateProductID= float(input().strip())
                    updateProductID= float(updateProductID)
                    print('Quantity being sold:')
                    updateOrderQuantity= input().strip()
                    while not updateOrderQuantity.isnumeric():
                        print('Quantity should be a number, please re-enter the quantity:')
                        updateOrderQuantity= input().strip()
                    pastProductID= salesHistory.loc[salesHistory['orderID']==float(orderUpdateID),'productID'].values
                    pastProductQuantity= salesHistory.loc[salesHistory['orderID']==float(orderUpdateID),'quantity'].values
                    stock.loc[stock['productID']==float(pastProductID), 'quantity'] = stock['quantity'] + float(pastProductQuantity)
                    while float(updateOrderQuantity) > stock.loc[stock['productID']==updateProductID,'quantity'].values:
                        print('Quantity sold exceeds quantity on hand, please use a lower amount:')
                        updateOrderQuantity= input().strip()
                    updateSellPrice= stock.loc[stock['productID']==updateProductID,'sellingPrice'].values
                    updateSale= float(updateOrderQuantity)*float(updateSellPrice)
                    salesHistory.loc[salesHistory['orderID']==orderUpdateID,['orderID','productID','quantity','sale']]=[float(orderUpdateID),float(updateProductID),float(updateOrderQuantity),float(updateSale)]                
                #if the user picks the "delete" option
                elif action== 'DELETE':
                    print('Enter orderID you would like to delete:')
                    deleteOrderID= input().strip()
                    while float(deleteOrderID) not in salesHistory['orderID'].values:
                        print('orderID not found. Please re-enter an existing orderID:')
                        deleteOrderID= input().strip()
                    deleteOrderID= float(deleteOrderID)
                    deleteProductID= salesHistory.loc[salesHistory['orderID']==float(deleteOrderID),'productID'].values
                    deleteProductQuantity= salesHistory.loc[salesHistory['orderID']==float(deleteOrderID),'quantity'].values
                    stock.loc[stock['productID']==float(deleteProductID), 'quantity'] = stock['quantity'] + float(deleteProductQuantity)
                    salesHistory= salesHistory.drop(salesHistory[salesHistory['orderID']==deleteOrderID].index)
elif 'Buying' in userAccess['access'].values:
    buying_agent(stock)
elif 'Selling' in userAccess['access'].values:
    selling_agent(stock,salesHistory,foreignCurrency)
stock.to_csv('stock.csv',index=False)
salesHistory.to_csv('salesHistory.csv',index=False)


# In[14]:


agarwoodo
mP6_'au(g|kV{T'|>?2H4jb@R!/
jkopelmank
yV8*B&Ts5XVtAd_z#stbBj0p2!
lcoyl
xH1=h`Xjsm,Iv|`/%~&({v"X


# In[ ]:




