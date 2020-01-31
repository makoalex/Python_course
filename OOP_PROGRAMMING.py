# OOP is a part of programming that allows for real world representations, through code with the use of:
# CLASSES: THE MOLD, BLUEPRINT THAT WILL BE USED : it can have attributes (colour, shape) and it can have functionality
# to create a cookie cutter for objects that will be created
# OBJECTS ARE INSTANCES, OF THE CLASS THAT WE CREATED
# ATTRIBUTES ARE PIECES OF DATA THAT WE GIVE TO EACH INSTANCE/OBJECT
# ENCAPSULATION allows us to structure and encapsulate code based on some hierarchical, logical conditions using CLASSES
# ABSTRACTION REFERS TO EXPOSING ONLY RELEVANT DATA , AND HIDING PRIVATE ATTRIBUTES AND METHODS


# CLASS DEFINITION:
class Comment:

    def __init__(self, username, text, likes=0):
        self.name = username
        self.comment = text
        self.likes = likes


c = Comment('mako', 'omg so cute', 3)
print(c.name)


# BANK ACCOUNT
class BankAccount:
    new_account=0
    def __init__(self, owner, balance=0.00):
        self.name = owner
        self.balance = balance
        BankAccount.new_account= BankAccount.new_account+1
    def create_account(self):
        BankAccount.new_account += 1
        return 'a new account has been made on the name of {}'.format(self.name)

    def depoosit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, summ):
        withdraw = self.balance - summ
        return withdraw

print(BankAccount.new_account)
account1 = BankAccount('mako')
print(account1.create_account())
print(BankAccount.new_account)
account2=BankAccount('Ola')
print(account2.create_account())
print(id(account2.new_account))
print(id(account1.new_account))


# CLASS ATTRIBUTE AND CLASS METHODS LIVE WITHIN THE CLASS THEMSELVES, AND ARE TAKEN BY ALL THE INSTANCES OF THE CLASS

