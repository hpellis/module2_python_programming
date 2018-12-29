# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:32:22 2018

@author: 612383249
"""

#----------------------------------------------------------------------------------------------------------------------
# CHAPTER 12 - FOR LOOPS
#----------------------------------------------------------------------------------------------------------------------

# the for loop is a counting loop
# it iterates over items
# you can use it to do operations on mutable data types
# the while loop is conditional, the for loop is not

# syntax
# for x in name_of_thing_to_iterate_through:
    # print x


# TASK 1 - LOOP THROUGH A LIST USING A FOR LOOP
#---------------------------------------------------------------------------------------

my_shopping_cart=["cake", "plates", "plastic forks", "juice", "cups"]

for item in my_shopping_cart:
    print (item)
    

# TASK 2 - UPDATE LIST VALUES
#---------------------------------------------------------------------------------
    
values=[875,23,451]

for val in values:
    print("--->"+str(val))
    print("--->"+str(val+50))


# TASK 3 - CREATE YOUR OWN LIST
#--------------------------------------------------------------------------------- 
    
values=["this", 55, "that"]

for item in values:
    print("***", item)

    
    
# TASK 4 - LOOP THROUGH A STRING
#------------------------------------------------------------------------------
    
# looping through a string
    
practice_string="This is a string to practice with."

for i in practice_string:
    print(i)
    
another_practice="Yes"

for char in another_practice:
    print(char)
    
    
# using the split method to loop through a string and print out each word
    
for char in "I like to code".split():
    print(char)
    

# TASK 5 -LOOP THROUGH A TUPLE
#-------------------------------------------------------------------------------

practice_tuple=("this", "is", "a", "practice", "tuple")

for item in practice_tuple:
    print (item)
    
    
# TASK 6 - CREATE A DICTIONARY
#------------------------------------------------------------------------------

metals={'iron':[7.8, 65.35, 0],  
        'gold':[19.3, 1242.70, 18], 
        'zinc':[7.13, 2604.00, 11], 
        'lead':[11.4, 2.58, 5]}


densities={"iron":7.8, "gold":19.3, "zinc":7.13, "lead":11.4}
  

# OPTION 1  FOR SORTING
#--------------------------------------------------------------------------------
# this option is better as it only goes through the list once

for k, v in sorted(densities.items()):
    print (k, v)
    
for k, v in sorted(metals.items()):
    print(k, v)
    

key_value=sorted(densities.items(), key=lambda kv:kv, reverse=True)


for item in metals:
    print(item)

for metal, metal_value in key_value:
    print(metal, metal_value)



# OPTION 2 FOR SORTING
#--------------------------------------------------------------------------------  
metals_list=list(metals.keys())

# this prints out the keys and their values
# metal is a placeholder
# metals_list is the list of keys
# for every item in that list, this loop prints out the key
# the metals[metal] is dictionaryname[placeholder] to get the value for the key
# then it all gets printed out

for metal in metals_list:
    print(metal, metals[metal])

print("\n")

# this option is the same, but it uses the index to print out only the value at position 1 for the key
for metal in metals_list:
    print(metal, metals[metal][1])
 

print("\n")
    
# FORMATTING THE PRINT STATEMENT
#-------------------------------------------------------------------------------

# this prints out the results
for metal in metals:
    print('{} = {}'.format(metal, densities[metal]))

print("\n")
  
# this is another way of formatting the results

for metal in metals:
    print('{0:>8} = {1:5.1f}'.format(metal, densities[metal]))
    
print("\n")

# TASK 8 - COMBINE THE FOR LOOP WITH CONDITIONALS TO FILTER OUT VALUES
#------------------------------------------------------------------------------------
for metal in metals:
    if densities[metal] >= 8:
        print (metal, densities[metal])

print(type(densities))

print("\n")

# TASK 9 - DESIGN A SUM FUNCTION
#--------------------------------------------------------------------------------

amounts=[2,12,9]

total=0

for val in amounts:
    print(total, "before adding", val)
    total+=val  
    print(total, "after adding", val)
    
print("TOTAL: " +str(total))


print("\n")

# TASK 10 - USING A LOOP WITH INDEX VALUES
#-------------------------------------------------------------------------------------

numbers=[1,5,30,200,101,100,22]

for index in range (len(numbers)):
    print('loop index', index, 'has value:', numbers[index])
    
    if numbers[index] > 100:
        print("Need to break: ", numbers[index], "with index", index)
    
    else:
        print("You didn't break the loop on", numbers[index], "with index", index)
    

print("\n")

# TASK 11 - USING A LOOP WITH THE RANGE FUNCTION
#--------------------------------------------------------------------------------------

practice_list=[3,12,9]

for i in range(len(practice_list)):
    values[i]=values[i] * 2    

print("\n")

# use range to set the starting point, end point and step
# this prints out every second value from 3 to 10    
for i in range(3,10,2):
    print (i)

print("\n")    

# this prints out every second value from 2 to 10
for i in range(2,10,2):
    print(i)

print("\n")   

# this also prints out every second value, starting from 2 and going to the end of the list
another_list=[1,2,3,4,5,6,7,89,10]

for i in range(2, len(another_list), 2):
    print (i)
    
print("\n")    
    
# TASK 12 - USING A BREAK STATEMENT IN A FOR LOOP
#-------------------------------------------------------------------------------------
    
test_list=[1,5,30,200,101,100,22]

for i in test_list:
    if i > 100:
        print ("Over 100")
        break

print("\n")

# TASK 13 - NESTED LOOPS
#------------------------------------------------------------------------------------    
outer_values=[1,2,3]
inner_values=['A', 'B', 'C']
dict={}

for oval in outer_values:
    for ival in inner_values:
        print(oval, ival)
        dict[oval]=ival

print(dict)

print("\n")


# multiplication table

for i in range(1,11):
    for j in range(1,11):
        print('{0:>3}'.format(i * j), end='')
        
print("\n")


##### bubble sort

# buble sort is a method that moves along a list, comparing adjacent values and swapping them if they are out of order

sorting_list=[4,3,6,5,2,1]

n=len(sorting_list)

#for i in range (n-1):
#    if sorting_list[i] > sorting_list[i+1]:
#        tmp=sorting_list[i]
#        sorting_list[i]=sorting_list[i+1]
#        sorting_list[i+1]=tmp
#        
#    print (sorting_list)

for j in range(n-1):
    for i in range (n-1-j):
        if sorting_list[i] > sorting_list[i+1]:
            tmp=sorting_list[i]
            sorting_list[1]=sorting_list[i+1]
            sorting_list[i+1]=tmp
            
print(sorting_list)

print("\n")


# COUNTERS
#--------------------------------------------------------------------------------------
colours=['red', 'green', 'red', 'green', 'blue', 'green', 'green']
d={}

for c in colours:
    if c not in d:
        d[c]=0
    d[c]+=1
    print(d)
    
# this prints out inside the for loop, so it provides an intermediary result



# TASK 14 - MULTIPLICATION TABLE WITH FOR LOOP
#------------------------------------------------------------------------------------    

for i in range(1, 10):
    for j in range(1, 11):
        print("{0:>3}".format(i * j), end="")


    