"""
 Man Chi Chan (Fiona)
 
 fich@bu.edu
 
 FE459 - Prof. Aaron Stevens
 
 Assignment 5: Thinking in Objects - Bonds
 Task 1: A Bond Class
 
 
 https://cs-people.bu.edu/azs/fe459/assignments/a5.html
 
 a5task1.py
"""

class Bond:
    """ Define a Bond object """
    
    def __init__(self, maturity_value, maturity_time, 
                 coupon_rate = 0, coupon_frequency = 2):
        """For initializing the new Bond object class"""
        
        # Initializing the data attributes
        self.__maturity_value = maturity_value
        self.__maturity_time = maturity_time
        self.__coupon_rate = coupon_rate
        self.__coupon_frequency = coupon_frequency
        
        # Other attributes
        self.__price = maturity_value
        self.__ytm = coupon_rate
        
        
        
    def __repr__(self):
        """Returns a beautifully-formatted string representation of the Bond object"""
        
        # Formatting for Bond attributes
        s = f'${self.__maturity_value:.2f}-maturity ' + \
            f'{self.__maturity_time}-year {self.__coupon_rate:.4%} bond, ' + \
            f'price=${self.__price:.2f}, ytm={self.__ytm:.4%}' + "\n" + \
            f'    duration={self.get_duration():.4f}, convexity={self.get_convexity():.4f}'
            
        return s # Return not print
        
        
        
    ### Accessor Mehtods ###
    def get_maturity_value(self):
        """Retrieves the maturity value of the bond"""
        return self.__maturity_value
        
        
        
    def get_maturity_time(self):
        """Retrieves the maturity time of the bond"""
        return self.__maturity_time
        
        
    def get_coupon_frequency(self):
        """Retrieves the coupon frequency of the bond"""
        return self.__coupon_frequency
        
        
    def get_coupon_rate(self):
        """Retrieves the coupon rate of the bond"""
        return self.__coupon_rate
        
        
        
    def get_coupon_amount(self):
        """Retrieves the coupon amount of the bond"""
        # Sets up the coupon amount equation
        cpa = self.__maturity_value * self.__coupon_rate  * (1/self.__coupon_frequency)
        
        return cpa
        
        
    def get_price(self):
        """Retrieves the price of the bond"""
        return self.__price
        
        
    def get_yield_to_maturity(self):
        """Retrieves the yield to maturity of the Bond"""
        return self.__ytm
        
        
        
    def get_pmt_times(self):
        """Calculates and retrieves the payment times of the Bond"""
      
        # Create list that draws out the periods
        pmt_times = list(range(1, self.__maturity_time * self.__coupon_frequency + 1))
        
        return pmt_times
        
        
        
    def get_cashflows(self):
        """Calculates and retrieves the cashflows of the Bond"""
        # Set up list for cashflow coupon payments
        cf = [self.__coupon_rate / self.__coupon_frequency * self.__maturity_value for x in range (self.__maturity_time * self.__coupon_frequency - 1)]
        
        # Append the last payment in the cashflow
        cf.append(self.__maturity_value + (self.__coupon_rate / self.__coupon_frequency * self.__maturity_value))
        
        return cf
        
        
        
    def get_discount_factors(self):
        """Calculates and retrieves the discount factors of the Bond"""
        # Set up list for discount factors
        dft = [1/ (1 + (self.__ytm / self.__coupon_frequency))**(x + 1) for x in range (self.__maturity_time * self.__coupon_frequency)]
        
        return dft
    ### End of Accessor Methods ###
    
    
    
    def calculate_price(self): #Helper
        """Helper Function for set_yeild_to_maturity()
        Calculates new bond bond price with new ytm"""
        
        # Calculates the discount factor using the discount factors accessor method
        dft = self.get_discount_factors() 
        
        # Calculates the cashflows using the cashflow accessor method
        cf = self.get_cashflows()
        
        # Set up a list that calculates the discounted cashflows
        bplist = [dft[i] * cf[i] for i in range (self.__maturity_time * self.__coupon_frequency)]
        
        # Sets the price of the Bond object as the present value of the discounted cashflows
        self.__price = sum(bplist)
        
    
    
    def set_yield_to_maturity(self, new_ytm):
        """Gives the bond a new ytm"""
        
        # Set the new YTM
        self.__ytm = new_ytm
        
        # Calls the helper function to update the price of the Bond object
        self.calculate_price()
        
        
        
    def calculate_yield_to_maturity(self, accuracy=0.0001): #Helper
        """Helper Function for set_price()
        Calculates the YTM of the bond after the user changes the price"""
        
        # Record the original price
        price = self.__price
        
        # Prerequisites to the loop
        self.set_yield_to_maturity(0.5) #Sets the YTM at 0.5
        testrate = self.__ytm #Sets the testrate as the YTM (starts at 0.5)
        ptestrate = 0.5 #For updating the testrate
        diff = self.__price - price #Difference between test price and price
        
        # Loop
        while True:
        
            # When test price is bigger than price
            if self.__price > price:
                ptestrate = ptestrate * 0.5 #Update the ptestrate
                testrate = testrate + ptestrate #Update the testrate to be bigger
                self.set_yield_to_maturity(testrate) #Update the Bond YTM (and price)
                diff = self.__price - price # Calculate the difference between test price and price
                
            # When test price is smaller than price
            elif self.__price < price:
                ptestrate = ptestrate * 0.5 #Update the ptestrate
                testrate = testrate - ptestrate #Update the testrate to be smaller
                self.set_yield_to_maturity(testrate) #Update the Bond YTM (and price)
                diff = self.__price - price # Calculate the difference between test price and price
                
            # Break when difference between test price and price is <= 0.0001
            if (abs(diff) <= accuracy):
                break
        
        # Set the new YTM as the Bond's YTM
        self.set_yield_to_maturity(testrate)
        
        
        
    def set_price(self, price):
        """Allows the user to set the price of the Bond Object"""
        
        # Set the new price
        self.__price = price
        
        # Calls the helper function to update the YTM of the Bond object
        self.calculate_yield_to_maturity()
        
        
        
    def get_duration(self):
        """To calculate and return the duration metric for the Bond Object"""
        
        # Set Statements
        periods = self.get_pmt_times()
        cf = self.get_cashflows()
        df = self.get_discount_factors()
        
        # Empty list for collecting the duration
        twpv = []
        
        # Calculate the PV per period
        bplist = [df[i] * cf[i] for i in range(self.__maturity_time * self.__coupon_frequency)]
        
        # For loop to append time weight PV
        for i in (periods):
            twpv.append(bplist[i - 1] * i)

        # Equation for duration
        duration = sum(twpv)/self.__price
        
        # Return the full equation for Duration
        return duration/self.__coupon_frequency
    
    
    
    def get_convexity(self):
        """To calculate and return the convexity metric for the Bond Object"""
        
        # Set statements
        periods = self.get_pmt_times()
        cf = self.get_cashflows()
        df = self.get_discount_factors()
        
        # Empty list for collecting the convexity
        listconv = []
        
        # Calculate the PV per period
        bplist = [df[i] * cf[i] for i in range(self.__maturity_time * self.__coupon_frequency)]
        
        # Numerator of Convexity equation
        for i in (periods):
            listconv.append(bplist[i - 1] * i * (i+1))
            
        num = sum(listconv)

        # Denominator of Convexity equation
        den = (1 + self.__ytm/self.__coupon_frequency)**2
        
        # Return the full equation for Convexity
        return (1/self.__price) * (num/den) * (1/self.__coupon_frequency)**2
        
        
        
        
        

    
###############################################################################
### unit test code:
if __name__ == '__main__':

     b1 = Bond(10000, 2, .06)
     b1.set_yield_to_maturity(0.07)
     print(b1)
     
     print(b1.get_pmt_times())


### end of unit test code
    
    
    
    
    
    
    
    
    