class Account:
    def __init__(owner,balance,action):
        owner.balance=balance
        owner.action=action
    def deposit(owner):
        print(owner.balance+owner.action)
    def withdraw(owner):
        if owner.action<=owner.balance:
            print(owner.balance-owner.action)    
p=Account(55000,35000)
p.deposit()
p.withdraw()
