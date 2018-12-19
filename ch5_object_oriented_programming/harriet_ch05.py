# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:07:06 2018

@author: 612383249
"""

#----------------------------------------------------------------------------------------------------------------------
# CHAPTER5 - OBJECT ORIENTED PROGRAMMING
#----------------------------------------------------------------------------------------------------------------------


# TASK 1 - USING CLASSES
#-------------------------------------------------------------------------------------------------------------------

class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the following properties: 
        Attributes:
            name: A string representing the customer's name.
            balance: a float tracking the current balance of the customer's account.
            """
            
    def __init__(self, name, balance=0.0):
        """Return a customer object whose name is *name* and starting balance is *balance*."""
        self.name=name
        self.balance=balance
        
    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount* dollars."""
        if amount > self.balance:
            raise RuntimeError("Amount greater than available balance.")
       
        self.balance-=amount
        return self.balance
    
    def deposit(self, amount):
        """Return the balance remaining after depositing *amount* dollars."""
        self.balance+=amount
        return self.balance
    
jason=Customer('Jason Taylor', 1000.0)

mark=Customer('Mark Taylor', 1231.39)

susan=Customer('Susan Taylor', 91.32)

matt=Customer('Matt Taylor', 80.30)

john=Customer('John Taylor', 1.09)

tom=Customer('Tom Taylor', 15.99)

jack=Customer('Jack Taylor', 9.03)


all_balances=[jason.balance, mark.balance, susan.balance, matt.balance, john.balance, tom.balance, jack.balance]

print(all_balances)

sorted_balances=sorted(all_balances)

print(sorted_balances)

lowest_balance=sorted_balances[0]

highest_balance=sorted_balances[-1]

print(highest_balance)
print(lowest_balance)

jason.withdraw(120.30)
john.deposit(333.00)

print(jason.balance)
print(john.balance)


#updated customer class
#-------------------------------------------------------------------------------------------------------------

class Customer_Debt():
            
    def __init__(self, name, balance=0.0, interest=1.12):
        self.name=name
        self.balance=balance
        self.interest=interest
        
 
    def calucate_new_total(self):
        new_total=self.balance*self.interest
        print (new_total )
        return new_total
    

jason=Customer_Debt('Jason Taylor', 1000.0)

mark=Customer_Debt('Mark Taylor', 1231.39)

susan=Customer_Debt('Susan Taylor', 91.32)


#for printing
#--------------------------------------------------------------------------------------------------------------

# def __str__(self):
    #return ("Customer "+self.name+" has a balance of "+str(self.balance)+"."  )
    

# TASK 2 - CREATE OBJECTS
#----------------------------------------------------------------------------------------------------------

class Animal ():
    def eat (self):
            print('yum')

class Dog (Animal):
    def bark(self):
            print('Woof!')
            
class Cat(Animal):
    def meow(self):
            print('Meow')
            
Snoopy=Dog()
Snoopy.bark()
Snoopy.eat()

print(type(Snoopy))

fluffy=Cat()
fluffy.meow()
fluffy.eat()

print(type(fluffy))


# TASK 3 - ROBOT CLASS
#-----------------------------------------------------------------------------------------------------------

class Robot():
    def move(self):
        print("...move move move...")

class CleanRobot(Robot):
    def clean(self):
        print("I vaccuum dust.")
        
class CookingRobot (Robot):
    def cook(self):
        print("I can make rice.")
        
robot1=Robot()
robot2=CleanRobot()
robot3=CookingRobot()
        
robot1.move()
robot2.move()
robot2.clean()
robot3.move()
robot3.cook()


#animal class updated
#------------------------------------------------------------------------------------------------------------------

class Animal2():
    def __init__ (self, name, age=0):
        self.name=name
        self.age=age
        
    def eat(self):
        print("yum")
        
class Dog(Animal2):
    def __init__ (self, name, age=0, barknumber=0):
        self.barknumber=barknumber
    
    def bark(self):
        print("Woof! "*self.barknumber)
        
class DogAgent(Dog):
    def detect(self):
        if self.barknumber>=3:
            print("Stranger coming!!!")
            
class Cat(Animal2):
    def meow(self):
        print("Meow")

name=input("What is your pet\'s name? ")
age=int(input("What is your pet\'s age? "))
bark=int(input("How many times did your pet bark? "))


dog007 = DogAgent(name, age, bark)
dog007.bark()
dog007.eat()
dog007.detect()



# TASK 4 - ASSOCIATION
#-----------------------------------------------------------------------------------------------------------------

class Dog(Animal):
    def bark(self):
        print("Woof")
        
class Robot():
    def move(self):
        print("move move move")
        
class CleanRobot(Robot):
    def clean(self):
        print("I vaccuum dust.")

class Super_Robot():
    def __init__(self):
        self.o1=Robot()
        self.o2=Dog()
        self.o3=CleanRobot()
        
    def playgame(self):
        print("alphago game")
   
    def move(self):
        return self.o1.move()
    
    def bark(self):
        return self.o2.bark()
    
    def clean(self):
        return self.o3.clean()
    
machinedog=Super_Robot()
machinedog.move()
machinedog.bark()



#practice
#----------------------------------------------------------------------------------------------------
class Person:
    def __init__ (self, name, age):
        self.name=name
        self.age=age

    def myfunc(self):
        print("Hello my name is " + self.name)
        
person1=Person("John", 21)
print(person1.name)
print(person1.age)

person1.myfunc()

person1.age=40
