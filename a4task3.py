"""
 Man Chi Chan (Fiona)
 
 fich@bu.edu
 
 FE459 - Prof. Aaron Stevens
 
 Assignment 4 Part 3: Matrices
 Matrix Applications: Portfolio Return, Bond Pricing, and Duration
 
 https://cs-people.bu.edu/azs/fe459/assignments/a4.html
 
 a4task3.py
"""

from a2task1 import cashflow_times, bond_cashflows, discount_factors # bond functions
from a4task1 import *
from a4task2 import *



def portfolio_return(weights, returns):
    """ 
    To calculate and return the portfolio return for an investment portfolio.
    E[rp] = e * w^T
    
    """
    
    # Verify
    assert len(weights) == len(returns), "Error!"
    
    # Check to see if weights/returns is a list (and turn it into a matrix)
    if not isinstance(weights[0], (list)):
       weights = [weights]
       returns = [returns]
        
    # Calculations
    dot = dot_product(returns, transpose(weights))
    
    # Set up returns
    r = 0
    
    # For loop to get the sum of the dot products
    for x in range(len(dot)):
        for y in range(len(dot[x])):
            r += dot[x][y]
            
    return r

### Testing
#weights = [0.3, 0.4, 0.3]
#returns = [0.12, 0.10, 0.05]
#portfolio_return(weights, returns)
#print(portfolio_return(weights, returns))



def bond_price(fv, c, n, m, ytm):
    """
    Function to calculate and return the price of a bond using linear algebra. 
    
    The parameters are:
        fv is the future (maturity) value of the bond;
        c is the annual coupon rate expressed as percentage per year;
        n is the number of years until maturity;
        m is the number of coupon payments per year;
        and ytm, the annualized yield to maturity of the bond
    
    """

    # Call to bond_cashflows() and discount_factors()
    cf = [bond_cashflows(fv, c, n, m)]
    df = [discount_factors(ytm, n, m)]
    
    # Calculations
    dot = dot_product(df, transpose(cf))
    
    # Set up returns
    r = 0
    
    # For loop to get the sum of the dot products
    for x in range(len(dot)):
        for y in range(len(dot[x])):
            r += dot[x][y]
            
    return r
    
### Testing
#print(bond_price(1000, 0.08, 5, 2, 0.08))
#print(bond_price(1000, 0.08, 5, 2, 0.09))
#print(bond_price(1000, 0.00, 5, 2, 0.09))
    
    
    
def bond_duration(fv, c, n, m, ytm):
    """
    function to calculate and return the annulized duration 
    of a bond using linear algebra. 
    
    The parameters are:
        fv is the future (maturity) value of the bond;
        c is the annual coupon rate expressed as percentage per year;
        n is the number of years until maturity;
        m is the number of coupon payments per year;
        and ytm, the annualized yield to maturity of the bond

    """
    
    # Call to cashflow_times(), bond_cashflows(), and discount_factors()
    cf_times = [cashflow_times(n, m)]
    cf = [bond_cashflows(fv, c, n, m)] 
    df = [discount_factors(ytm, n, m)]
    
    # Call to element_product()
    prod = element_product(cf, df)
    
    # Calculating the dot_product()
    dot = dot_product(prod, transpose(cf_times))
    
    # Calculating the numerator
    numerator = 0
    
    # For loop to get the sum of the dot products
    for x in range(len(dot)):
        for y in range(len(dot[x])):
            numerator += dot[x][y]
    
    # Calculating the denominator
    denominator = bond_price(fv, c, n, m, ytm)
    
    # Calculations (full equation)
    bond_dur = numerator / denominator * (1/m)
    
    return bond_dur

### Testing
#print(bond_duration(1000, 0.05, 2, 2, 0.05))
#print(bond_duration(1000, 0.00, 2, 2, 0.05))
#print(bond_duration(1000, 0.05, 10, 2, 0.03))
    
    
    
    