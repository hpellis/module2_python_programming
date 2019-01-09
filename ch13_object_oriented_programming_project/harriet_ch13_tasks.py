# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 09:15:06 2019

@author: 612383249
"""


#----------------------------------------------------------------------------------------------------------------------
# CHAPTER 13 - OBJECT-ORIENTED PROGRAMMING TASKS
#----------------------------------------------------------------------------------------------------------------------


# TASK 1 - INITIALISE THE PERSON CLASS
#---------------------------------------------------------------------------------------

class Person:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        if gender == 'm':
            self.isMale=True
        elif gender == 'f':
            self.isMale=False
        else:
            print ('Gender not recognised.')
            
    def greetingInformal(self):
        print('Hi', self.name)
        
    def greetingFormal(self):
        if self.isMale:
            print('Welcome, Mr ', self.name)
        else:
            print('welcome, Ms ', self.name)
            
    def greetingAgeBased(self):
        if self.age < 18:
            print('Welcome, young ', self.name)
        elif self.age > 60:
            print('Welcome, venerable ', self.name)
        else:
            self.greetingFormal()
        
            

p1=Person('John', 25, 'm')

print(p1.name)
print(p1.isMale)



# TASK 2 - ADD MORE METHODS
#---------------------------------------------------------------------------------------

p2=Person('Harry', 12, 'm')
p3=Person('Jean', 30, 'f')

p2.greetingInformal()
p3.greetingFormal()


# TASK 3 - ADD GREETING FILTER
#---------------------------------------------------------------------------------------

# test new method (age-based greeting) added to class above

p4=Person('Susan', 90, 'f')
p5=Person('Thomas', 3, 'm')
p6=Person('Anna', 35, 'f')

p4.greetingAgeBased()
p5.greetingAgeBased()
p6.greetingAgeBased()


# TASK 4 - CREATE A SUBCLASS FOR THE PERSON CLASS
# TASK 5 - REDEFINE THE INIT FUNCTION
#TASK 6 - ADD NEW METHODS TO THE WIZARD CLASS
#---------------------------------------------------------------------------------------

class Wizard(Person):
    def __init__(self, name, age, gender):
       Person.__init__(self, name, age, 'm')
    
    def greetingFormal(self):
        print('Welcome, Mr ', self.name, end=' ')
        print('- you\'re a fine wizard!')
        
    def spell(self):
        print('Expelliarmus')
        
p7=Person('Harry', 12, 'm')
p7.greetingFormal()

p8=Wizard('Harry', 12, 'm')
p8.greetingFormal()

p8.spell()



