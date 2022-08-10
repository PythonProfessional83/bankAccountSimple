    # bankClass.py
'''
Very simple recall.
Refer to the README.md
Testing setters, getters, __repr__, __str__
Creating class which manages the bank acount
'''
from decimal import Decimal
from simple_colors import *

class BankClass:
    '''Manages bank account.''' # ipython session: BankClass?
    
    def __init__(self, name, balance):
        '''Initializing the attributes''' 
        # if balance < Decimal('0.00'):
        #     raise ValueError(f'Balance= {balance:,} < 0.00 and it must be >= 0.00')
        
        if balance < Decimal('0.00'):
            raise ValueError(f'Balance= {balance:,} must be >=0')
         
        self.name = name
        self.balance = balance
        
    def deposit(self, deposi_t):
        '''Adding additional money to the account'''
        
        if deposi_t < Decimal('0.00'):
            raise ValueError(f'Amount must be >= 0')
        
        self.balance  += deposi_t
    
    def withdrawal(self, amount):
        '''Substracting money from the account'''
        if amount > self.balance:
            raise ValueError('You don"t have enoufgh money!')
        
        self.balance -= amount
    
    def __repr__(self):
        '''status of the attributes'''
        return (f'\nYour current balance is: {self.balance:,}')
    

        
        
        
    