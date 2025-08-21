'''
# Abstarctions: To hide the complexity of data.
when ever we are going with abstraction we have to go with

from abc import ABC, abstractmethod
- every child need to have the abstract method in polymorphism
- in abstraction we need to have every method 

'''

from abc import ABC, abstractmethod

class Bankaccount:
    def deposit(self):
        print("You can deposit amount")

    def checkbalance(self):
        print("You can check your balance")

    @abstractmethod 
    def withdraw(self):  # withdraw differ's from diff classes
        pass

    def viewhistory(self):
        print("You can check the history")

class CurrentAccount(Bankaccount):
    def withdraw(self):
        print("You can withdraw Extra amount also")

class SavingAccount(Bankaccount):
    def withdraw(self):
        print("You can withdraw youramount")


# example 2:

from abc import ABC,abstractmethod

class Order(ABC):
    @abstractmethod
    def process_order(self):
        print("Processing Food Order: Check chef availability,estimate time,")

class GroceryOrder(Order):
    def process_order(self):
        print("Processing Grocery Order: Check inventory per item,bag & dispatch,")

class MedicineOrder(Order):
    def process_order(self):
        print("Processing Medicine Order: Validate prescription, assign secure")





