# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 11:25:26 2018

@author: 612383249
"""

class Relationship():
   def __init__ (self, name, name2, score=0):
       self.name=name
       self.name2=name2
       self.score=score


class Length(Relationship):

 def __init__ (self, name, name2, score=0, months=0):
       Relationship.__init__ (self, name, name2, score=0)
       self.months=months

 def how_long(self):
       if self.months >= 5:
           #print('month', self.months)
           self.score += 10
       #print('score', self.score)
       return self.score

class Friends(Relationship):

 def __init__ (self, name, name2, score=0,number_friends=0):
        Relationship.__init__ (self, name, name2, score=0)
        self.number_friends=number_friends

 def how_friends(self):
       if self.number_friends >= 3:
           self.score += 5
       elif self.number_friends >= 5:
           self.score += 10
       #print('score', self.score)
       return self.score


class Brunch(Relationship):

 def __init__ (self, name, name2, score=0,do_brunch=0):
    Relationship.__init__ (self, name, name2, score=0)
    self.do_brunch = do_brunch

 def brunch_test(self):
        if self.do_brunch == str("Y"):
            self.score += 10
        #print('score', self.score)
        return self.score


class Cooking(Relationship):

 def __init__ (self, name, name2, score=0,cooking_skills=0):
        Relationship.__init__ (self, name,name2,  score=0)
        self.cooking_skills=cooking_skills

 def cooking_test(self):
       if self.cooking_skills >= 6:
           self.score += 5
       elif self.cooking_skills >= 8:
           self.score += 10
       #print('score', self.score)
       return self.score



class Move_in(Relationship):
    def __init__ (self, name, name2, score):
        Relationship.__init__ (self, name, name2, score)
        self.score = score

    def big_move (self):
       if self.score >= 15:
           print ("\nTime to move in!")
           positive_result(self.name, self.name2)
       else:
           print("\nTime to move on!")
           negative_result(self.name, self.name2)
        
     # return self.score

def positive_result(name, name2):
    file= open("Test_Results.txt", "w+")
    file.write(f"Dear {name}, \n\nCongratulations! We are happy to inform you that you are ready to move in with {name2}.\n\nKind regards,\nOfficial Moving In Together Quiz.")
    file.close()

def negative_result(name, name2):
    file= open("Test_Results.txt", "w+")
    file.write(f"Dear {name}, \n\nUnfortunately on this occasion we found that it would not be appropriate for you to move in with {name2}. \n\nKind regards,\nOfficial Moving In Together Quiz.")
    file.close()