"""
October 3 2023

FE459

In Class Exercise

"""



class BankAccount:
    """ Define a bank account object"""
     
    def __init__(self, routing_no, account_no, 
                 owner_name, init_balance, interest_rate):
        
        # Initialize the data attributes:
            self.__routing_no = routing_no
            self.__account_no = account_no
            self.__owner_name = owner_name
            self.__balance = init_balance
            self.__interest_rate = interest_rate
            
            
            
    def __repr__(self):
        """Return a string representation of the object"""
        
        s = f'BankAccount: Account Number: ' + \
            f'{self.__account_no}, Balance: ${self.__balance:.2f}'
            
        return s
            
            
            
    def deposit(self, amount):
        """Deposit funds to this BankAccount."""
        
        # Update this data attribute to add the "amount"
        # to the previous balance
        self.__balance += amount
        
    
    
    def withdraw(self, amount):
        """Withdraws the amount from this BankAccount"""
        if amount > self.__balance:
            print(f"Insufficient funds; cannot withdraw {amount}")
        else:
            self.__balance -= amount
    
    def get_balance(self):
        """Return the balance amount as a floating-point number"""
        
        return float(self.__balance)
            
            
            
            
if __name__ == '__main__':
    
    # Create an account object here
    accounts = [
        BankAccount(22222222, 88888888, "Fif", 0, 0.2),
        BankAccount(33333333, 99999999, "Dingo", 0, 0.2),
        BankAccount(11111111, 44444444, "Bobo", 0, 0.2)
        ]
    
    balances = [a.get_balance() for a in accounts]
    total = sum(balances)
    
    
    
    
    