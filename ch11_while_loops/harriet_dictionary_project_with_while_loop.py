# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:17:34 2018

@author: 612383249
"""

#----------------------------------------------------------------------------------------------------------------------
# CHAPTER 10 - DICTIONARIES
#----------------------------------------------------------------------------------------------------------------------


# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:13:35 2018

@author: 612383249
"""

# phonebook dictionary which contains information for 4 people
# name: [last three digits, Lucky number, postcode, city, year of birth, difference between age and queen#'s age]

# sort the dictionary by name
# sort the dictionary by city
# sort the dictionary by lucky number

# use user input and append to append more items to the dictionary

def main_phonebook():
    phonebook={}
    name=""
    number_of_entries=0
    while number_of_entries < 4:
        phonebook_input(phonebook, name)
        number_of_entries += 1
    phonebook_sort(phonebook)
    write_phonebook(phonebook)


def phonebook_input(phonebook, name):
    name=input("Enter name. ")
    phonenumber=input("Enter the last three digits of the phone number. ")
    lucky_no=int(input("Enter lucky number. "))
    postcode=input("Enter postcode. ")
    city=input("Enter city. ")
    birth_year=int(input("Enter year of birth. "))  
    queens_birth_year=1926
    phonebook[name]=[phonenumber, lucky_no, postcode, city, birth_year, birth_year-queens_birth_year]
    return phonebook, name
  
def phonebook_sort(phonebook):
    choice=input("Enter 1 to sort by name, 2 to sort by city or 3 to sort by lucky number.")
#    key_list=list(phonebook.keys())
    if choice == "1":
#        key_list.sort(key=lambda k:phonebook[k][0])
#        print (key_list)
        print(sorted(phonebook.items(), key=lambda kv:kv[0]))
    elif choice == "2":
#        key_list.sort (key=lambda k:phonebook[k][3])
#        print (key_list)
         print(sorted(phonebook.items(), key=lambda kv:kv[1][3]))
    elif choice == "3":
#        key_list.sort (key=lambda k:phonebook [k][1])
#        print (key_list)
        print(sorted(phonebook.items(), key=lambda kv:kv[1][1]))
    else:
        print("Error")

def write_phonebook(phonebook):
    file=open("Phonebook.txt", "w+")
    file.write(str(phonebook))
    file.close()

main_phonebook()

