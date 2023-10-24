#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Man Chi Chan (Fiona)
 
 fich@bu.edu
 
 FE459 - Prof. Aaron Stevens
 
 Assignment 3 Part 1: Descriptive Statistics for Stock Investors
 Descriptive Statistics
 
 https://cs-people.bu.edu/azs/fe459/assignments/a3.html
 
 a3task1.py
"""

def mean(values):
    """
    Takes as a parameter a list of numbers, and calculates and 
    returns the mean of those values.
    
    """

    mean = sum(values)/len(values)
    return mean

### Testing
#x = [4,4,3,6,7]
#print(mean(x))



def variance(values):
    """
    Takes as a parameter a list of numbers, 
    and calculates and returns the population variance of the values in that list.
    
    """
    
    # Call to mean()
    avg = mean(values)
    
    # Empty list for backing up numbers
    lis = []
    
    # Definite loop to find the difference between the mean and each value
    for x in values:
        diff = x - avg
        diff = diff**2
        lis.append(diff)
    
    # Equation for calculating the Variance
    var = sum(lis)/len(values)
    
    return var
    
### Testing
#x = [4,4,3,6,7]
#print(variance(x))
    


def stdev(values):
    """
    Takes as a parameter a list of numbers, and calculates and returns
    the population standard deviation of the values in that list. 
    The population standard deviation is the square-root of the population variance.
    
    """
    
    # Call to variance()
    var = variance(values)
    
    # Stdev is sqrt of Variance
    stdev = var**0.5
    
    return stdev

### Testing
#x = [4,4,3,6,7]
#print(stdev(x))
    


def covariance(x,y):
    """
    Takes as parameters two lists of values, and calculates and 
    returns the population covariance for those two lists.
    
    """
    
    # Call to mean() for list x and list y
    meanx = mean(x)
    meany = mean(y)
    
    # Empty lists
    lis = []
    
    # Being assertive okurrr~
    assert len(x) == len(y), "error"
    
    # Definite loop for calculating difference between x values and means and y values and means
    count = len(x) -1
    while (count >= 0):
        diffx = x[count] - meanx
        diffy = y[count] - meany
        xy = diffx * diffy
        lis.append(xy)
        count -= 1
  
    # Equation for numerator
    sumxy = sum(lis)
    
    # Equation for covariance
    cov = sumxy/ (len(x))
    
    return cov
    
### Testing
#x = [4,4,3,6,7]
#y = [6,7,5,10,12]
#print(covariance(x,y))



def correlation(x,y):
    """
    Takes as parameters two lists of values, and calculates and 
    returns the correlation coefficient between these data series. 
    """
    
    # Equation
    cor = covariance(x,y)/(stdev(x) * stdev(y))
    
    return cor
    
### Testing
#x = [4,4,3,6,7]
#y = [6,7,5,10,12]
#print(correlation(x,y))
#print(correlation(list(range(10)), list(range(10,0,-1))))



def rsq(x,y):
    """
    Takes as parameters two lists of values, and calculates and returns
    the square of the correlation between those two data series, w
    hich is a measure of the goodness of fit measure to explain 
    variation in y as a function of variation of x.

    """
    
    # Call to correlation()
    cor = correlation(x,y)
    
    # Equation
    rsq = cor**2
    
    return rsq

### Testing
#x = [4,4,3,6,7]
#y = [6,7,5,10,12]
#print(rsq(x,y))



def simple_regression(x,y):
    """
    Takes as parameters two lists of values, and calculates and returns
    the regression coefficients between these data series. 
    The function should return a list containing two values: 
        the intercept and regression coefficients, α (a) and β (b).

    """
    
    # Calculation for b
    b = covariance(x,y)/variance(x)
    
    # Calculation for a
    a = mean(y) - b * mean(x)
    
    return [a, b]

### Testing
#x = [4,4,3,6,7]
#y = [6,7,5,10,12]
#print(simple_regression(x,y))




    
    