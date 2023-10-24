#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Man Chi Chan (Fiona)
 
 fich@bu.edu
 
 FE459 - Prof. Aaron Stevens
 
 Assignment 3 Part 2: Descriptive Statistics for Stock Investors
 Stocks
 
 https://cs-people.bu.edu/azs/fe459/assignments/a3.html
 
 a3task2.py
"""

from a3task1 import *



def calc_returns(prices):
    """
    This function will process a list of stock prices and calculate the periodic returns. 
    The function should assume that the oldest price is in prices[0] 
    and latest price in prices[-1]. 
    The function should use a loop and accumulator pattern
    to accumulate a list of returns for periods 1 to n.
    There is no return for period 0.

    """
    
    # Empty list for returns
    lis = []
    
    # Definite loop for calculating prices
    for x in range(1, len(prices)):
            r = (prices[x]/prices[x-1]) -1 # Returns equation
            lis.append(r) # Update the list
            
    return lis

### Testing
#prices = [100,110,105,112,115]
#returns = calc_returns(prices)
#print(returns)



def process_stock_prices_csv(filename):
    """
    This function will process a data file containing stock price data, 
    and return a list of stock prices.
    
    """
    
    # Open file
    file = open(filename, 'r')
    
    # Empty list
    price_list = []
    
    # Loop for reading the CSV File
    for line in file:
        line = line[:-1]
        fields = line.split(',')
        adj_close = fields[-1] # Field for Adj Close
        
        # Removes header
        if (adj_close == "Volume" or adj_close == "Adj Close"):
            list1 = []
        
        # Everything else get added to the list
        else:
            list1 = float(adj_close)
            price_list.append(list1)
        
    # Returns the list
    return price_list

### Testing
#filename = 'AAPL.csv'
#prices = process_stock_prices_csv(filename)
#print(prices)



def stock_report(filenames):
    """
    A client program to process stock prices and display (print out)
    descriptive statistics about the stocks. The function takes a 
    parameter filenames which is a list of CSV filenames with stock price history, 
    in the format as above.
    
    Outputs:
    Symbol, Mean, StDev, Covar, Correl, R-SQ, Beta, Alpha

    """
    
    # Market Index
    mkt_index = process_stock_prices_csv(filenames[-1])
    
    # Empty list to contain the data
    file_list = []
    
    # For loop to process the files
    for file in filenames:
        stock1 = process_stock_prices_csv(file)
        sym1 = str(file.replace(".csv", ""))
        mean1 = mean(stock1)
        stdev1 = stdev(stock1)
        covar1 = covariance(mkt_index,stock1)
        correl1 = correlation(mkt_index,stock1)
        rsq1 = rsq(mkt_index,stock1)
        reg1 = simple_regression(mkt_index,stock1)
        beta1 = reg1[1]
        alpha1 = reg1[0]
        
        # To keep the data stored in one list
        list1 = [sym1, mean1, stdev1, covar1, correl1, rsq1, beta1, alpha1]
        
        # Append the list to a list of lists
        file_list.append(list1)
    
    
    # For loop to print the Symbol
    print(f'Symbol:  ', end="")
    for x in range(len(file_list)):
        sym1 = file_list[x][0]
        print(f'{sym1:<20}', end="")

    # For loop to print the Mean
    print("\n" + f'Mean:    ', end="")
    for x in range(len(file_list)):
        avg = file_list[x][1]
        print(f'{avg:<20.5f}', end="")
        
    # For loop to print the StDev
    print("\n" + f'StDev:   ', end="")
    for x in range(len(file_list)):
        std = file_list[x][2]
        print(f'{std:<20.5f}', end="")
    
    # For loop to print the Covar
    print("\n" + f'Covar:   ', end="")
    for x in range(len(file_list)):
        covar = file_list[x][3]
        print(f'{covar:<20.5f}', end="")
        
    # For loop to print the Correl
    print("\n" + f'Correl:  ', end="")
    for x in range(len(file_list)):
        cor = file_list[x][4] 
        print(f'{cor:<20.5f}', end="")
        
    # For loop to print the RSQ
    print("\n" + f'R-SQ:    ', end="")
    for x in range(len(file_list)):
        rs = file_list[x][5] 
        print(f'{rs:<20.5f}', end="")
        
    # For loop to print the Beta
    print("\n" + f'Beta:    ', end="")
    for x in range(len(file_list)):
        bet = file_list[x][6] 
        print(f'{bet:<20.5f}', end="")
        
    # For loop to print the Alpha
    print("\n" + f'Alpha:   ', end="")
    for x in range(len(file_list)):
        Alp = file_list[x][7] 
        print(f'{Alp:<20.5f}', end="")

    
    
    
    """
    # Call to process_stock_prices_csv()
    stock1 = process_stock_prices_csv(filenames[0])
    stock2 = process_stock_prices_csv(filenames[1]) 
    stock3 = process_stock_prices_csv(filenames[2])
    mkt_index = process_stock_prices_csv(filenames[3])
    
    
    # Symbol
    sym1 = str(filenames[0].replace(".csv", ""))
    sym2 = str(filenames[1].replace(".csv", ""))
    sym3 = str(filenames[2].replace(".csv", ""))
    sym_mkt = str(filenames[3].replace(".csv", ""))
    
    # Mean
    mean1 = mean(stock1)
    mean2 = mean(stock2)
    mean3 = mean(stock3)
    mean_mkt = mean(mkt_index)
    
    
    # StDev
    stdev1 = stdev(stock1)
    stdev2 = stdev(stock2)
    stdev3 = stdev(stock3)
    stdev_mkt = stdev(mkt_index)
    
    
    # Covar
    covar1 = covariance(mkt_index,stock1)
    covar2 = covariance(mkt_index,stock2)
    covar3 = covariance(mkt_index,stock3)
    covar_mkt = covariance(mkt_index,mkt_index)
    
    
    # Correl
    correl1 = correlation(mkt_index,stock1)
    correl2 = correlation(mkt_index,stock2)
    correl3 = correlation(mkt_index,stock3)
    correl_mkt = correlation(mkt_index,mkt_index)
    
    
    # R-SQ
    rsq1 = rsq(mkt_index,stock1)
    rsq2 = rsq(mkt_index,stock2)
    rsq3 = rsq(mkt_index,stock3)
    rsq_mkt = rsq(mkt_index,mkt_index)
    
    
    # Simple Regression
    reg1 = simple_regression(mkt_index,stock1)
    reg2 = simple_regression(mkt_index,stock2)
    reg3 = simple_regression(mkt_index,stock3)
    reg_mkt = simple_regression(mkt_index,mkt_index)
    
    
    # Beta
    beta1 = reg1[1]
    beta2 = reg2[1]
    beta3 = reg3[1]
    beta_mkt = reg_mkt[1]
    
    
    # Alpha
    alpha1 = reg1[0]
    alpha2 = reg2[0]
    alpha3 = reg3[0]
    alpha_mkt = reg_mkt[0]
    
    
    # Print Statements
    print(f'Symbol:  {sym1:<20}{sym2:<20}{sym3:<20}{sym_mkt:<20}')
    
    print(f'Mean:    {mean1:<20.5f}{mean2:<20.5f}{mean3:<20.5f}{mean_mkt:<20.5f}')
    
    print(f'StDev:   {stdev1:<20.5f}{stdev2:<20.5f}{stdev3:<20.5f}{stdev_mkt:<20.5f}')

    print(f'Covar:   {covar1:<20.5f}{covar2:<20.5f}{covar3:<20.5f}{covar_mkt:<20.5f}')
    
    print(f'Correl:  {correl1:<20.5f}{correl2:<20.5f}{correl3:<20.5f}{correl_mkt:<20.5f}')
    
    print(f'R-SQ:    {rsq1:<20.5f}{rsq2:<20.5f}{rsq3:<20.5f}{rsq_mkt:<20.5f}')

    print(f'Beta:    {beta1:<20.5f}{beta2:<20.5f}{beta3:<20.5f}{beta_mkt:<20.5f}')
    
    print(f'Alpha:   {alpha1:<20.5f}{alpha2:<20.5f}{alpha3:<20.5f}{alpha_mkt:<20.5f}')
    """

    

### Test Code     
#files = ['AAPL.csv', 'BAC.csv', 'GOOG.csv','SPY.csv']
#stock_report(files)

    

    
    

