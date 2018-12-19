# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 09:47:19 2018

@author: 612383249
"""
#----------------------------------------------------------------------------------------------------------------------
# CHAPTER 9 - LISTS AND TUPLES
#----------------------------------------------------------------------------------------------------------------------


# TASK 1 - CREATE A LIST
#-----------------------------------------------------------------------------------------------------------------------

my_favourite_fruits=['apple', 'orange', 'banana']
print(my_favourite_fruits)

x=['this', 55, 'that', my_favourite_fruits]
print(x[0])
print(x[1])
print(x[2])
print(x[3])

print(x[3][0])


# TASK 2 - MODIFY THE LIST
#---------------------------------------------------------------------------------------------------------------------

# remove to delete from list (removes based on value, not index. only removes first instance)
#----------------------------------------------------------------------------------------------------------------------
x.remove(my_favourite_fruits)
print(x)

# append to add to list
#----------------------------------------------------------------------------------------------------------------------
x.append(my_favourite_fruits)
print(x)

x.append('more')
print(x)


##### del function (remove an element by index)
#----------------------------------------------------------------------------------------------------------------------
del x[2]
print(x)


##### pop function (removes element at given index and updates the list)
#----------------------------------------------------------------------------------------------------------------------
popped_element=x.pop(1)
print(popped_element)

print(x)

second_popped_element=x.pop(-1)
print(second_popped_element)
print(x)


##### list operations
#----------------------------------------------------------------------------------------------------------------------
a=['one', 'two', 'three']
b=['four', 'five', 'six']

c=a+b

print(c)

numbered_list=[1, 2, 3, 4, 5]
numbered_list2=[5, 6, 7, 8, 9, 10]

another_numbered_list=numbered_list + numbered_list2

print(another_numbered_list)

set(another_numbered_list)

print(another_numbered_list)

print(3*another_numbered_list)

##### set operation on lists
#-------------------------------------------------------------------------------------------------
unordered_collection=set(a+b)
print(unordered_collection)


# TASK 3 - SLICING A LIST
#--------------------------------------------------------------------------------------------------------------------

#slicing a list (first number inclusive, last number exclusive)
#-----------------------------------------------------------------------------------------------------------------

example_list=['cat', 'dog', 'bird', 'snake', 'rat']
print(example_list[1:4])
print(example_list[0:2])
# cannot start at -1 because nowhere to go --- this line will print out an empty list
print(example_list[-1:-2])
#this works for negative indexes
print(example_list[-3:-1])


# TASK 4 - SORTING A LIST
#----------------------------------------------------------------------------------------------------------------------

# there are two sort methods
# list.sort()
    # use this when you want to mutate the list
# sorted(list)
    # use this when you want a new sorted object back
    
another_list=[100, 381, 3, 5, 76, 119, 87, 74, 33, 2, 9, 45, 75]
another_list_sorted=sorted(another_list)
print(another_list)
print(another_list_sorted)

yet_another_list=[43, 54, 62, 1, 22, 600, 543, 52, 1, 534, 90]
print(yet_another_list)
yet_another_list.sort()
print(yet_another_list)


alpha_list=['a', 'c', 'd', 'x', 'b', 'k', 'help', 'animal', 'p']
alpha_list.sort()
print(alpha_list)


# reverse sort
#----------------------------------------------------------------------------------------------------------------------------
print(sorted(another_list, reverse=True))

print(sorted(alpha_list, reverse=True))



# TASK 5 - TUPLES
#--------------------------------------------------------------------------------------------------------------------------

# tuples are immutable objects
# this means you cannot change them in the same way you can change lists
# you cannot delete items from a tuple
# you cannot overwrite items inside a tuple
# you cannot append elements to a tuple
# to make changes to a tuple, you cast the tuple to a list, make changes and then recast to tuple


a= [1,2,3,4,5,6,7,8,9]
del a[-1]
print(a)
a[3]=15
print(a)
a.append(9)
a.append(10)
print(a)

b=(0,1,2,3,4,5,6,7,8,9)
#del b[-1]
# b[-1]=65
# b.append(10)

# casting b to a list - tuple b will not change, but you can make changes to list c, and then create a new tuple
c=list(b)
print(type(c))


# TASK 6 - USING THE LAMBDA FUNCTION TO SORT A LIST
#---------------------------------------------------------------------------------------------------------------------------------

# lambda is a notation for writing functions

# lambda x:(x * x) ---> means given input x, I will return the result x * x +1

# lambda s:s[1] ---> means given the item s, lambda will compute s1, whihc only makes sense if s is a sequence, so that s[1] is its 2nd element, or if s is a dicitonary, so s[1] looks for the value for key 1


a = [0,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)
myFavF = ["apple", "orange", "banana"]
x = ["aa", "sb", "lf", "hw", "ed", "fy"]
z = ["fg", "uj", "sx", "uj", "ww", "cf"]
y = sorted(x)

x2=[('a', 3, z), ('c', 1, y), ('b', 5, x)]

print(x2)
print(sorted(x2))
print("------------------------------------------------------------------\n")

### the examples below pass an argument to the method sorted
### key is an optional argument for sorted
### below examples set the key to lambda s:s[i]
### this means the list will be sorted according to the specified index position

# this sorts x2 by the element that is in index position 1
# the s:s are just keywords -- can be anything
print(sorted(x2, key=lambda s:s[1]))

# this sorts x2 by the element that is in index position 2
print(sorted(x2, key=lambda s:s[2]))

# this sorts x2 by the 
print(sorted(x2, key=lambda s:s [2][1]))


##### more practice examples
print("------------------------------------------------------------------\n")
d=[1,2,3,4]
e=[3,4,10,3]
f=[20,10,30,40]

x3=[('a', 3, d), ('c', 1, e), ('b', 5, e)]

print(x3)

print(sorted(x3, key=lambda s:s[2]))

# this sorts by the last element in the item at index 2
print(sorted(x2, key=lambda s:s[2][-1]))


# TASK 6 - CREATE A LIST OF TUPLES
#-------------------------------------------------------------------------------------------------------------------------

print("------------------------------------------------------------------\n")
g=["apple", "orange", "pear", "plum"]
h= ["car", "bicycle", "bus", "train"]
i=["pen", "paper", "backpack", "desk"]

x4=[('hi', 6, g), ('yo', 1, h), ('go', 9, i)]


print(x4)

# this will print the list sorted by the last element in the second element
print(sorted(x4, key=lambda s:s[2][-1]))

# this will print the list sorted by the second letter in the first element
print(sorted(x4, key=lambda s:s[0][1]))
