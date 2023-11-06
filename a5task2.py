"""
 Man Chi Chan (Fiona)
 
 fich@bu.edu
 
 FE459 - Prof. Aaron Stevens
 
 Assignment 5: Thinking in Objects - Bonds
 Task 2: A Bond Portfolio Class 
 
 
 https://cs-people.bu.edu/azs/fe459/assignments/a5.html
 
 a5task2.py
"""

from a5task1 import *



class BondPortfolio:
    """ Define a BondPortfolio object """
    
    def __init__(self):
        """For initializing the new BondPortfolio object class"""
        # Data member of type list
        self.list = []
        
        
        
    def __repr__(self):
        """Returns a string representation of the BondPortfolio, 
        and will also show some details about the portfolio’s contents 
        and risk characteristics"""
        
        if self.list == []: #If the list is empty
            s = 'BondPortfolio contains 0 bonds: '
            
            # Formatting for other values
            s += 'Portfolio value:              $0.00' + "\n"
            s += 'Portfolio yield to maturity:  0%' + "\n"
            s += 'Portfolio duration:           0.0' + "\n"
            s += 'Portfolio convexity:          0.0'
            
        else:
            s = f'BondPortfolio contains {len(self.list)} bonds: ' + "\n"
            
            # Formatting per bond in portfolio
            for i in range(len(self.list)): #List loops around each bond in BondPortfolio
                s += repr(self.list[i]) + '\n' #And calls the repr for each bond
                
            # Formatting for other values
            s += f'Portfolio value:              ${self.get_value():.2f}' + "\n"
            s += f'Portfolio yield to maturity:  {self.get_yield_to_maturity():.4%}' + "\n"
            s += f'Portfolio duration:           {self.get_duration():.2f}' + "\n"
            s += f'Portfolio convexity:          {self.get_convexity():.2f}'
            
            
        return s #Returns the string
    

    
    def add_bond(self, b):
        """Method will add one Bond to this portfolio. 
        To add a Bond, this method should add a referene
        to the Bond b to the list of Bonds"""
        self.list.append(b) #append() method to add a Bond Object to BondPortfolio
        
        
    def rem_bond(self, b):
        """Method will remove one Bond from this portfolio"""
        if self.list == []: #Check to see if list is empty or not
            self.list = []
        else:
            self.list.remove(b) #remove() method to add a Bond Object to BondPortfolio
        
        
        
    def get_value(self):
        """Returns the overall value of the portfolio.

        The portfolio’s value is the sum of the values
        of all of the Bonds in the portfolio"""
        
        # Set variable for collecting value
        value = 0
        
        for i in range(len(self.list)): #List loops through each bond in BondPortfolio
            value += self.list[i].get_price() #Collects the price and adds it to the value
        
        return value #Returns the total sum of all prices in BondPortolio
            
        
    
    def get_yield_to_maturity(self):
        """Returns the overall YTM of the portfolio.
        
        The portfolio’s yield to maturity is the weighted-average 
        of all of the individual Bonds yields to maturity. 
        The weights to use are the Bonds prices, 
        i.e., their present values. 
        The higher the Bond‘s price (present value), 
        the more it’s yield to maturity contributes to the 
        overall portfolio’s yield to maturity."""
        
        # Set variable for collecing YTM
        ytm = 0
        
        # Get the overall value of the BondPortfolio
        total_value = self.get_value()
        
        for i in range(len(self.list)): #List loops through each bond in BondPortfolio
            this_ytm = self.list[i].get_yield_to_maturity() #Get the YTM of the bond object
            this_weight = self.list[i].get_price() / self.get_value() #Find the weight of the bond in the portfolio by dividing the price of the singular bond by the overall value of the portfolio
            ytm += this_ytm * this_weight #Add weighted value of YTM to the overall YTM of the portfolio
            
        return ytm #Return the overall ytm of BondPortfolio
    
    
    
    def get_duration(self):
        """Returns the overall duration of the portfolio.
        
        The portfolio’s duration is approximately the weighted-average
        of all of the individual Bonds durations. 
        The weights to use are the Bonds prices, 
        i.e., their present values. """
        
        # Set variable for collecting duration
        duration = 0
        
        for i in range(len(self.list)): #List loops through each bond in BondPortfolio
            this_weight = self.list[i].get_price() / self.get_value() #Find the weight of the bond in the portfolio by dividing the price of the singular bond by the overall value of the portfolio
            duration += self.list[i].get_duration() * this_weight #Add weighted value of bond duration to overall duration of the portfolio
            
        return duration #Return the overall duration of BondPortfolio
    
    
    
    def get_convexity(self):
        """Returns the overall convexity of the portfolio.
        
        The portfolio’s convexity is approximately the weighted-average 
        of all of the individual Bonds convexity. 
        The weights to use are the Bonds prices, 
        i.e., their present values."""
        
        # Set variable for collecting duration
        convexity = 0
        
        for i in range(len(self.list)): #List loops through each bond in BondPortfolio
            this_weight = self.list[i].get_price() / self.get_value() #Find the weight of the bond in the portfolio by dividing the price of the singular bond by the overall value of the portfolio
            convexity += self.list[i].get_convexity() * this_weight #Add weighted value of bond convexity to overall convexity of the portfolio
            
        return convexity #Return the overall convexity of BondPortfolio
    
    
    
    def shift_ytm(self, delta_ytm):
        """To handle a uniform shift in interest rates. 
        The method will take a parameter delta_ytm 
        (which could be positive or negative) 
        and apply this change to all bonds in the portfolio. """
        
        # For loop to change the YTM of each Bond object
        for i in range(len(self.list)):
            this_ytm = self.list[i].get_yield_to_maturity() #Get the YTM of the bond object
            self.list[i].set_yield_to_maturity(this_ytm + delta_ytm) #use set_ytm to manipulate the YTM of each individual bond in BondPortfolio
        
            

     
###############################################################################
### unit test code:
if __name__ == '__main__':

     bp = BondPortfolio()    

     b1 = Bond(10000, 2, .06)
     b1.set_yield_to_maturity(0.07)
     bp.add_bond(b1)
    
     b2 = Bond(10000, 5, .08)
     b2.set_yield_to_maturity(0.09)
     bp.add_bond(b2)
         
     b3 = Bond(5000, 10) # 10-year zero-coupon bond
     b3.set_yield_to_maturity(0.10)
     bp.add_bond(b3)
     
     print(bp)
     print()
     
     bp.shift_ytm(0.01)
     
     
     print(bp)
     print()
     
     
     bp.shift_ytm(-0.005)
     
     
     print(bp)
     print()
     
     
### end of unit test code

