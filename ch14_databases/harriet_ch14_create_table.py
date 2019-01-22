# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:19:39 2019

@author: 612383249
"""
# this line imports sqlite
import sqlite3

# this line connects to sqlite 
# the input of the connect function is a database file called task1 
# conn refers to SOMETHING
conn = sqlite3.connect('task1.db')

# this line creates the cursor or pointer that will be used in the database
c=conn.cursor()

# don't want to create a new table every time this file is run
# this function checks for the existence of a table, and if it doesn't exist creates it
# stuff_to_build is the name of the database
# unix, datestamp, keyword and value are the column names in the database 
# these can be any required names, and should be in lowercase
# REAL and TEXT are SQL commands which specify the data types and formats for columns
# SQL is not case sensitive, but convention is to do uppercase to distinguish from cols
# the table created is at this point an empty data frame
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToBuild(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")
  
# this function adds data to the table
# this example inserts 4 values, one for each column
# the conn.commit() command commits this entry
# the c.close() and conn.close() commands close the cursor and database
def data_entry():
    c.execute("INSERT INTO stuffToBuild VALUES(142233222, '2018-01-01', 'python', 5)")
    conn.commit()
    c.close()
    conn.close()
    
create_table()
data_entry()