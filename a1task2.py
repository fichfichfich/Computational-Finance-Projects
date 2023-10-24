#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Man Chi Chan (Fiona)
 
 fich@bu.edu
 
 FE459 - Prof. Aaron Stevens
 
 Assignment 1 Part 2: Python Functions and the Time Value of Money
 
 https://cs-people.bu.edu/azs/fe459/assignments/a1.html
 
 a1task2.py
"""

from a1task1 import *

def dollar_format(amount):
    """ 
    Takes a parameter amount which is a number, 
    and returns a beautifully-formatted string of dollars and cents, 
    including the dollar sign and comma-separated thousands and millions.
    """
    
    money = f"${amount:13,.2f}"
    return money

### Testing
### print(dollar_format(-123.92))





def life_cycle_model():
    """
    The Life-Cycle Sustainable Spending Calculator.
    Takes your risk free return, age, retirement age, and annual income
    and gives you the details and a chart on how you should spend your money
    for the rest of your life.
    """
    
    print("Welcome to the Life-Cycle Sustainable Spending Calculator.", "\n")
    
    
    #Inputs 
    r = float(input("Enter the current inflation-indexed risk-free rate of return: "))
    age_now = int(input("Enter your age now: "))
    retirement_age = int(input("Enter your expected retirement age: "))
    annual_income = int(input("Enter your current annual income: "))
    
    
    # Test inputs
    # r = 0.03
    # age_now = 35
    # retirement_age = 67
    # annual_income = 83000
    
    
    human_cap = pv_annuity(r, retirement_age - age_now, annual_income)
    
    
    
    print("\n" + "You have ", retirement_age - age_now, 
          " remaining working years with an income of ", dollar_format(annual_income),
          " per year." + "\n" +
          "The present value of your human capital is about ", dollar_format(human_cap)
          + "\n")
    
    
    
    #Takes an input for assets
    fin_assets = int(input("Enter the value of your financial assets: "))
    
    #Test asset 
    #fin_assets = 150000
    

    
    print("\n" + "Your economic net worth is: ", dollar_format(human_cap + fin_assets))
    
    

    yoc = 100 - age_now
    sus_standard_of_living = annuity_payment(r, yoc, human_cap + fin_assets)
    
    
    
    print("Your sustainable standard of living is about ", 
          dollar_format(sus_standard_of_living), " per year.",
          "\n" +
          "To achieve this standard of living to age 100, you must save ", 
          dollar_format((human_cap + fin_assets) / 100), " per year."
          + "\n")
    
    
    
    print("Age", "     ", "Income", 
          "       ", "Consumption", "  ", 
          "Savings", "      ", "Assets", "          ")
    
    n = age_now + 1
    save = annual_income - sus_standard_of_living
    fin_assets = fin_assets * (1 + r) + save
    

    while (n < 101):
        if (n == 100):
            save = (annual_income - sus_standard_of_living)
            fin_assets = fin_assets * (1 + r) + save 
            print (n, #age now
                   "     ",
                   dollar_format(annual_income), #income
                   dollar_format(sus_standard_of_living), #consumption
                   dollar_format(save), #savings = income - consumption
                   dollar_format(fin_assets)) #assets = assets * (1 + rate of return) + savings
            break
        if (n > retirement_age):
            annual_income = 0
            save = (annual_income - sus_standard_of_living)
            fin_assets = fin_assets * (1 + r) + save 
            print (n, 
                   "      ",
                   dollar_format(annual_income), 
                   dollar_format(sus_standard_of_living), 
                   dollar_format(save), 
                   dollar_format(fin_assets))
            n = n + 1
        if (n <= retirement_age):
            print (n, 
                   "      ",
                   dollar_format(annual_income), 
                   dollar_format(sus_standard_of_living), 
                   dollar_format(annual_income - sus_standard_of_living), 
                   dollar_format(fin_assets))
            if (n == retirement_age):
                n = n + 1
            else:
                save = annual_income - sus_standard_of_living
                fin_assets = fin_assets * (1 + r) + save
                n = n + 1


    
    
    
    
    
    
    
if __name__ == '__main__':
    
    # call the function:
    life_cycle_model()
    
          
