# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:54:13 2018

@author: 612383249
"""

#----------------------------------------------------------------------------------------------------------------------
# CHAPTER 8 - MOBILE DATA PURCHASE BUNDLE
#----------------------------------------------------------------------------------------------------------------------

# TEST FILE
#-----------------------------------------------------------------------------------------------------------------

from harriet_data_functions import data_bundle_purchase

#test call to programme

print("TEST EXAMPLE !")

#database input, you still still need to check user pin
result = data_bundle_purchase('1234', 34.55)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

print ('TEST EXAMPLE 2')
result = data_bundle_purchase('2345', -22.00)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

print ('TEST EXAMPLE 3')
result = data_bundle_purchase('3456', 17.55)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

