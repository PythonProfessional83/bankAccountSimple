# bankAccount.py
'''
This is very simple recall.
Please refer to the README.md
Testing different objects, __str__, __repr__
Testing assignment attribute to the property of the class.
'''
from decimal import Decimal
import bankClass

# creating object
account = bankClass.BankClass('Kris', Decimal('10_000.00'))

# yousing setter method to create deposit
account.deposit(deposi_t=Decimal('50_400'))
print(account)

# setting new ballance changing property: balance
# this property assignment dooesn't invoke ValueError
account.balance = Decimal('80_000')
print(account)

account.withdrawal(Decimal('20_000.345989'))
print(account)

# raiding ValueError
# account.withdrawal(Decimal('100_000'))