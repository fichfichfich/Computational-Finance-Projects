#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Man Chi Chan (Fiona)
 
 fich@bu.edu
 
 FE459 - Prof. Aaron Stevens
 
 Assignment 2 Part 2: Bonds and Bond Math
 Duration, Convexity, and Estimate Change in Price
 
 https://cs-people.bu.edu/azs/fe459/assignments/a2.html
 
 a2task2.py
"""

from a2task1 import *

def bond_duration(fv, c, n, m, r):
    """ 
    To calculate and return the duration metric for a bond. The parameters are:

    fv is the future (maturity) value of the bond;
    c is the annual coupon rate expressed as percentage per year;
    n is the number of years until maturity;
    m is the number of coupon payments per year;
    and r is the interest rate of the bond
    """

    # Set Statements
    period = cashflow_times(n, m)
    bcf = bond_cashflows(fv, c, n, m)
    pb = bond_price(fv, c, n, m, r)
    dft = discount_factors(r, n, m)
    twpv = []
    
    # PV per period
    bplist = [dft[i] * bcf[i] for i in range (n * m)]
    
    # For loop to append time weight pv
    for i in (period):
        twpv.append(bplist[i - 1] * i)

    duration = sum(twpv)/pb
    
    return duration/m

### Test
#print(bond_duration(1000, 0.08, 5, 2, 0.07))



def macaulay_duration(fv, c, n, m, price):
    """ 
    To calculate and return the Macaulay duration for a bond. The parameters are:

    fv is the future (maturity) value of the bond;
    c is the annual coupon rate expressed as percentage per year;
    n is the number of years until maturity;
    m is the number of coupon payments per year;
    and price is the current market price of the bond.
    """
    # Set statements
    period = cashflow_times(n, m)
    bcf = bond_cashflows(fv, c, n, m)
    ytm = bond_yield_to_maturity(fv, c, n, m, price)
    dft = discount_factors(ytm, n, m)
    mac = []
    
    # PV per period
    bplist = [dft[i] * bcf[i] for i in range (n * m)]
    
    # For loop to append macaulay's duration
    for i in (period):
        mac.append(bplist[i - 1] * i)

    duration = sum(mac)/price
    
    return duration/m

### Test
#print(macaulay_duration(1000, 0, 5, 2, 950))
    


def modified_duration(fv, c, n, m, price):
    """
    To calculate and return the modified duration for a bond. The parameters are:
        
    fv is the future (maturity) value of the bond;
    c is the annual coupon rate expressed as percentage per year;
    n is the number of years until maturity;
    m is the number of coupon payments per year;
    and price is the current market price of the bond.
    """

    # Set statements
    period = cashflow_times(n, m)
    bcf = bond_cashflows(fv, c, n, m)
    ytm = bond_yield_to_maturity(fv, c, n, m, price)
    dft = discount_factors(ytm, n, m)
    
    # Call Macaulay's Duration
    dmac = macaulay_duration(fv, c, n, m, price)
    
    # Equation
    modified_duration = dmac / (1 + ytm/m)
    
    return modified_duration

### Test
#print(modified_duration(1000, 0.08, 5, 2, 950))
#print(modified_duration(1000, 0.08, 5,365, 950))



def bond_convexity(fv, c, n, m, r):
    """
    To calculate and return the convexity metric for a bond. The parameters are:

    fv is the future (maturity) value of the bond;
    c is the annual coupon rate expressed as percentage per year;
    n is the number of years until maturity;
    m is the number of coupon payments per year;
    and r is the annualized yield to maturity the bond
    """
    
    # Set statements
    period = cashflow_times(n, m)
    bcf = bond_cashflows(fv, c, n, m)
    price = bond_price(fv, c, n, m, r)
    dft = discount_factors(r, n, m)
    listconv = []
    
    # PV per period
    bplist = [dft[i] * bcf[i] for i in range (n * m)]
    
    # Numerator
    for i in (period):
        listconv.append(bplist[i - 1] * i * (i+1))
        
    num = sum(listconv)

    # Denominator
    den = (1 + r/2)**2
    
    return (1/price) * (num/den) * (1/2)**2

### Test
#print(bond_price(5000, 0.05, 3, 2, 0.05))
#print(bond_duration(5000, 0.05, 3, 2, 0.05))
#print(bond_convexity(5000, 0.05, 3, 2, 0.05))
#print(bond_duration(1000, 0, 3, 2, 0.05))
#print(bond_convexity(1000, 0, 3, 2, 0.05))



def estimate_change_in_price1(fv, c, n, m, price, dr):
    """
    Returns the estimated dollar change in price corresponding to a change in yield.

    The parameters describe a bond by its maturity value (fv), 
    coupon rate (c), years until maturity (n), the number of payments per year (m), 
    the current bond price (price), and the change in interest rate (dr) we are modeling.
    """

    mod_dur = modified_duration(fv, c, n, m, price)
    mod_dur = -mod_dur
    
    # Equation 
    ecip = mod_dur * dr 
    
    return ecip * price

### Test
#orig_price = bond_price(1000, 0.07, 5, 2, 0.07)
#print(orig_price)
#dr = 0.0001 
#est1 = estimate_change_in_price1(1000, 0.07, 5, 2, 1000, dr)
#print(est1)
#new_price = bond_price(1000, 0.07, 5, 2, 0.07+dr)
#print(new_price)



def estimate_change_in_price2(fv, c, n, m, price, dr):
    """
    Returns the estimated dollar change in price corresponding to a change in yield.

    The parameters describe a bond by its maturity value (fv), 
    coupon rate (c), years until maturity (n), the number of payments per year (m), 
    the current bond price (price), and the change in interest rate (dr) we are modeling.
    """
    
    # Call to modified duration
    mod_dur = modified_duration(fv, c, n, m, price)
    mod_dur = -mod_dur
    
    # Call to YTM
    r = bond_yield_to_maturity(fv, c, n, m, price)
    
    # Call to convexity
    conv = bond_convexity(fv, c, n, m, r)
    
    # Equation
    ecip = (mod_dur * dr) + (0.5 * conv * (dr**2)) 
    
    return ecip * price
    
### Test
#orig_price = bond_price(1000, 0.07, 5, 2, 0.07)
#print(orig_price)
#dr = -0.01 
#est2 = estimate_change_in_price2(1000, 0.07, 5, 2, 1000, dr)
#print(est2)
#new_price = bond_price(1000, 0.07, 5, 2, 0.07+dr)
#print(new_price)
#diff = new_price - orig_price - est2
#print(diff)



















