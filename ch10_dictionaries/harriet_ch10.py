# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:54:39 2018

@author: 612383249
"""

#----------------------------------------------------------------------------------------------------------------------
# CHAPTER 10 - DICTIONARIES
#----------------------------------------------------------------------------------------------------------------------

# about dictionaries
#---------------------------------------------------------------------------------------------------------------------------

# dictionaries are compound data types
# they contain keys, which are mapped to values within the dictionary
# you use the keys to access the values associated with them (can think of keys like index system)
# dictionaries work by linking values to a hash of the key
# this means that the keys must be immutable data types (e.g. strings, ints or tuples)
# the values can be any data types, even dictionaries themselves


example={'bo':50000, 'al':20000, 7:('Joke', 'Chen', 'Bond')}

# the syntax is {key1:value1, key2:value2, key3:value3}

# TASK 1 - CREATE A DICTIONARY, ASSIGN AND UPDATE VALUES
#--------------------------------------------------------------------------------------------------------------------------

#### how to create a dictionary

# create the empty dictionary
salary={}

# use the dict name, in square brackets the name of the key, and then set that as equal to the value
salary['al']=20000

print(salary)

salary['po']=35000

salary['kl']=76000

salary['bg']=31000

print(salary)


#### you can also assign a new value to an existing key

# to overwrite the value associated with the key 'po':

salary['po']=49000

print(salary)


# TASK 2 - CREATE YOUR OWN DICTIONARY
#--------------------------------------------------------------------------------------------------------------------------

# creating a dictionary
phonebook={'john':123, 'peter':234, 'james':345}

print(phonebook)

# updating values associated with the keys
phonebook['john']=1234

phonebook['peter']=2345

phonebook['james']=3456

print(phonebook)


# TASK 3 - UPDATING VALUES IN THE DICTIONARY 
#----------------------------------------------------------------------------------------------------------------------------

# performing an adding operation on the values
phonebook['john']+=1000

phonebook['peter']+=2000

phonebook['james']+=3000

print(phonebook)


# adding new entries to the dictionary
phonebook['paul']=9876

phonebook['tom']=8765

print(phonebook)


##### deleting key:value pairs from the dictionary
# in a dictionary, a key:valye pair counts as one item
# therefore when you delete a key/value you have to delete them together

del phonebook['john']
print(phonebook)


# TASK 3 - ACCESSING VALUES FROM THE DICTIONARY
#-----------------------------------------------------------------------------------------------------------------------

##### accessing values from a dictionary
print(phonebook['james'])
print(phonebook['james'])


# TASK 4 - GETTING KEYS OR VALUES FROM A DICTIONARY
#---------------------------------------------------------------------------------------------------------------------

##### getting lists of keys or values from a dictionary
# useful to print out all keys and all values from a dictionary
# you might want to sort the dictionary by one of the values, and then only extract the ordered keys as a list
# this could give you, for example, an ordered list of customer names, without printing out the value that they were being ordered by

print(phonebook.keys())

print(phonebook.values())

list_of_phonebook_keys=list(phonebook.keys())

list_of_phonebook_values=list(phonebook.values())


print(type(list_of_phonebook_keys))

print(type(list_of_phonebook_values))


# TASK 6 - HOW TO AVOID KEY ERRORS
#------------------------------------------------------------------------------------------------------------------

##### how to test for key errors
m="michael"

if m in phonebook:
    print(m, ':', phonebook[m])
else:
    print(m, 'not found')
    

# TASK 7 - SORTING A DICTIONARY WITH LAMBDA
#------------------------------------------------------------------------------------------------------------------------
#### sorting a dictionary
# using lambda function to sort
# because you can get values from the keys, you can use the lambda function to return keys' values to the dictionary
    
# example list
counts={'a':3, 'c':1, 'b':5}

# create a variable called labels which is a list of the dict counts' keys
labels=list(counts.keys())

# the below line sorts the labels list that we created
# it uses lambda to sort k by counts[k]
# for the example above, this sorts the values (a, b, c) into the order of their values
labels.sort(key=lambda k:counts[k])

##### another example
# dictionary where the key is a name, and it is associated with a list containing two values, a birth month and a lucky number

classmates={'amy':[1, 99], 'beth':[5, 3], 'caroline':[12, 9], 'diane':[9, 10]}

print(classmates)

# print out the keys
print(classmates.keys())

# create a new variable that is a list containing the keys
label_list=list(classmates.keys())

# check that the new variable is a list
print(type(label_list))

# this returns the list sorted according to the birth month
label_list.sort(key=lambda k:classmates[k])

# this reutrns the list sorted according to the lucky number 
label_list.sort(key=lambda k:classmates[k][-1])


# this appends a new value to each key in the dictionary - this will be their favourite colour

classmates['amy'].append('blue')
classmates['beth'].append('red')
classmates['caroline'].append('yellow')
classmates['diane'].append('green')

print(classmates)

# this line creates a new list of labels

new_label_list=list(classmates.keys())
print(type(new_label_list))

# this sorts the new list sorted by the alphabetical order of the new last item
new_label_list.sort(key=lambda k:classmates [k][-1])

# this sorts the new list sorted by the lucky number
new_label_list.sort(key=lambda k:classmates [k][-2])


##### sorting a list with the sorted() function

# sorted() is different to .sort in that sorted() creates a new sorted object

# creates a new list of labels to do the sorted() function on
additional_label_list=list(classmates.keys())

#print to check type
print(type(additional_label_list))

# print out the list of labels sorted by the key
print(sorted(additional_label_list, key=lambda k:classmates[k]))

#print out the list of labels sorted by the birth month
print(sorted(additional_label_list, key=lambda k:classmates[k][0]))

# print the dictionary sorted by keys (only keys)
print(sorted(classmates))

#print the dictionary sorted by values (only values)
print(sorted(classmates.values()))


# print both key and values, sorted by the element in position 1
print(sorted(classmates.items(), key=lambda kv:kv[1]))

# print both key and values, sorted by the last element in the list
print(sorted(classmates.items(), key=lambda kv:kv[1][-1]))


# this sorts by the key
sorted(counts, key=lambda k:counts[k])


# this prints out the keys only
for i in classmates:
    print (i)

# this prints out the values too    
for i in classmates.items():
    print(i)


# this option also works though it is not good practice
# this is less efficient, as it has to go through the dict twice
    
for i in classmates:
    print (i, classmates[i])
    

# TASK 8 - SORTING A DICTIONARY WITH LAMBDA PART 2
#----------------------------------------------------------------------------------------------------------------------

##### sorting dictionaries in descending order

densities = {'iron':7.8, 'gold':19.3, 'zinc':7.13, 'lead':11.4}

metals=list(densities.keys())

print(metals)

metals.sort(reverse=True, key=lambda m:densities[m])

print(metals)

print(sorted(densities.items(), key=lambda kv: kv[1], reverse=True))


# TASK 

# this creates a dictionary called metals
# each key is the name of a metal
# associated with the key is the density, share price and number of times an experiment succeeded
metals={'iron':[7.8, 65.35, 0],  
        'gold':[19.3, 1242.70, 18], 
        'zinc':[7.13, 2604.00, 11], 
        'lead':[11.4, 2.58, 5]}


# create a list of keys so can sort by value
metal_key_list=list(metals.keys())

print(type(metal_key_list))


# sort the list of metals using the first thing in the value
metal_key_list.sort(key= lambda k:metals [k])

print(metal_key_list)

# sort the list of metals by the order of the last element in the value
metal_key_list.sort(key=lambda k:metals[k][-1])

print(metal_key_list)


# sort the list of metals with the sorted() function, and print out keys and values
# to do this, use the .items method
# the below will sort according to the item in position 0 (i.e. metal name)

sorted_metal_key_list=(sorted(metals.items(), key=lambda kv:kv[0]))

print(sorted_metal_key_list)

# the below will sort according to the item in position 1 (i.e. tuple)
sorted_metal_key_list=(sorted(metals.items(), key=lambda kv:kv[1]))

print(sorted_metal_key_list)


# the below will sort the keys according to the item in the tuple at index 0 (density)

sorted_metal_key_list=(sorted(metals.items(), key=lambda kv:kv[1][0]))

print(sorted_metal_key_list)


# the below will sort the keys according to the item in the tuple at index 1 (share price)

sorted_metal_key_list=(sorted(metals.items(), key=lambda kv:kv[1][1]))

print(sorted_metal_key_list)


# the below will sort the keys according to the item in the tuple at index 2 (experiments)

sorted_metal_key_list=(sorted(metals.items(), key=lambda kv:kv[1][2]))

print(sorted_metal_key_list)


# the below will sort according to the item in position 1, index 1 of the tuple (cost of metal)

sorted_metal_key_list=(sorted(metals.items(), key=lambda kv:kv[1][1]))

print(sorted_metal_key_list)

# the below will sort according to the position in position 1, index 2 of the tuple (experiment)

sorted_metal_key_list=(sorted(metals.items(), key=lambda kv:kv[1][2]))

print(sorted_metal_key_list)


# the below will sort in reverse order, according to the value at position 1

metal_key_list.sort(reverse=True, key=lambda m:metals[m][1])
    
print(metal_key_list)






