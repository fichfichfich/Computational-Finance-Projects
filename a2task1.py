#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Man Chi Chan (Fiona)
 
 fich@bu.edu
 
 FE459 - Prof. Aaron Stevens
 
 Assignment 2 Part 1: Bonds and Bond Math
 Cashflow, Discount Factors, Bond Cashflows, Bond Price, YTM
 
 https://cs-people.bu.edu/azs/fe459/assignments/a2.html
 
 a2task1.py
"""


def cashflow_times(n, m):
    """
    Develops the list of the times at which a bond makes coupon payments, 
    with n years and m coupon payments per year.
    """
    mylist = list(range(1, n * m + 1))
    return mylist



def discount_factors(r, n, m):
    """ 
    Calculates and returns a list of discount factors for a given 
    annualized interest rate r, for n years, and m discounting periods per year.
    """
    dft = [1/ (1 + (r / m))**(x + 1) for x in range (n * m)]
    return dft
              


def bond_cashflows(fv, c, n, m):
    """
    calculates and return a list of cashflows for a bond specified by the parameters. 
    The parameters are: fv is the future (maturity) value of the bond;
    c is the annual coupon rate expressed as percentage per year;
    n is the number of years until maturity;
    m is the number of coupon payments per year.
    """
    coupon = [c / m * fv for x in range (n * m - 1)]
    coupon.append(fv + (c / m * fv))
    return coupon



def bond_price(fv, c, n, m, r):
    """
    To calculate and return the price of a bond. 
    The parameters are: fv is the future (maturity) value of the bond; 
    c is the annual coupon rate expressed as percentage per year; 
    n is the number of years until maturity; 
    m is the number of coupon payments per year; 
    and r, the annualized yield to maturity of the bond 
    """
    dft = discount_factors(r, n, m)
    bcf = bond_cashflows(fv, c, n, m)
    
    # List comprehension for bond price
    bplist = [dft[i] * bcf[i] for i in range (n * m)]
    
    bp = sum(bplist)
    return bp

### Test
#print(bond_price(100, 0.04, 3, 2, 0.04))



def bond_yield_to_maturity(fv, c, n, m, price):
    """
    To calculate the annualized yield_to_maturity on a bond. 
    The parameters are: fv is the future (maturity) value of the bond;
    c is the annual coupon rate expressed as percentage per year;
    n is the number of years until maturity;
    m is the number of coupon payments per year;
    and price is the current market price of the bond
    """
    
    # Prerequisites to the loop
    count = 0
    testrate = 0.5
    ptestrate = 0.5
    testbp = bond_price(fv, c, n, m, testrate)
    diff = testbp - price
    
    # Loop
    while True:
        
        # When test price is bigger than price
        if testbp > price:
            # Print
            #print("Iteration", count, 
            #  "test_rate =", testrate,
            #  "price =", testbp,
            #  "diff =", diff)
            
            # Update statement
            count = count + 1
            ptestrate = ptestrate * 0.5
            testrate = testrate + ptestrate
            testbp = bond_price(fv, c, n, m, testrate)
            diff = testbp - price
            
        # When test price si smaller than price
        elif testbp < price:
            # Print
            #print("Iteration", count, 
            #  "test_rate =", testrate,
            #  "price =", testbp,
            #  "diff =", diff)
            
            # Update statement
            count = count + 1
            ptestrate = ptestrate * 0.5
            testrate = testrate - ptestrate
            testbp = bond_price(fv, c, n, m, testrate)
            diff = testbp - price
            
        # Break when accuracy <= 0.0001
        if (abs(diff) <= 0.0001):
            break
    
    # Return statement
    return testrate
            
            
### Test          
# bond_yield_to_maturity(100, 0.04, 3, 2, 101.75)

        
        


    