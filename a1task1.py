#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
 Man Chi Chan (Fiona)
 
 fich@bu.edu
 
 FE459 - Prof. Aaron Stevens
 
 Assignment 1 Part 1: Python Functions and the Time Value of Money
 
 https://cs-people.bu.edu/azs/fe459/assignments/a1.html
 
 a1task1.py
"""

def fv_lump_sum(r, n, pv):
    """ 
    Calculates and returns the future value of a lump sump pv 
    invested at the periodic rate r for n periods. 
    
    fv = pv (1 + r)^n
    """
    
    fv = (1 + r) ** n * pv
    return fv

### Testing
### print(fv_lump_sum(0.05, 2, 100))





def pv_lump_sum(r, n, fv):
    """
    Calculates and returns the present value of a lump sum fv
    to be received in the future, 
    discounted at the periodic rate r for n periods.
    
    pv = fv / ((1 + r)^n)
    """
    
    pv = fv / ((1 + r) ** n)
    return pv

### Testing
### print(pv_lump_sum(0.06/2, 5*2, 500))





def fv_annuity(r, n, pmt):
    """
    Calculates and returns the future value of an annuity of pmt 
    to be received each period for n periods, invested at the periodic rate r.
    
    fv = pmt[((1+r)^n - 1) / r]
    """
    
    fv = pmt * ((((1 + r) ** n) - 1) / r)
    return fv

### Testing
### print(fv_annuity(0.04, 5, 100))
### print(fv_annuity(0.09/12, 10*12, 100))





def pv_annuity(r, n, pmt):
    """
    Calculate and return the present value of an annuity of pmt to be received 
    each period for n periods, discounted at the rate r. 
    
    pv = pmt[(1 - (1 + r)^-n) / r]
    """

    pv = pmt * (((1 - (1 + r) ** -n)) / r)
    return pv
    
### Testing
### print(pv_annuity(0.05, 30, 250))
### print(pv_annuity(0.009/12,60, 471.75))





def annuity_payment(r, n, pv):
    """
    Calculates the amortizing annuity
    payment for a present value of pv 
    to be repaid at a periodic interest rate of r for n periods. 
    
    pmt = (r * pv) / (1 - (1 + r)^-n)
    """
    
    pmt = (r * pv) / (1 - (1 + r) ** -n)
    return pmt

### Testing
### print (annuity_payment(0.05, 10, 1000))
### print(annuity_payment(0.009/12, 60, 27667.44))
    
    
    
    
    
    