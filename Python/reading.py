# Functions for reading tables and databases

import glob
from database import *


# YOU DON'T NEED TO KEEP THE FOLLOWING CODE IN YOUR OWN SUBMISSION
# IT IS JUST HERE TO DEMONSTRATE HOW THE glob CLASS WORKS. IN FACT
# YOU SHOULD DELETE THE PRINT STATEMENT BEFORE SUBMITTING
file_list = glob.glob('*.csv')


# Write the read_table and read_database functions below

def read_table_helper(file_name):
    '''
    (str) -> Table
    The function returns a table when you have given it a file name and
    will read its contents. It will take the first row and put it as key
    for the dictionary and every row as a value of the dictionary.
    The keys and values are sent to the Table to create its own dictionary.

    REQ: File name must be a csv file type
    '''
    # create a new table
    new_dict = {}
    # strip the file
    new_table = Table(new_dict, file_name.strip())
    # open the file to read
    file = open("%s" % file_name, 'r')
    # create a multi dimensional list
    multi_dimensional_list = []
    # For loop
    for title in file:
        # new list
        new = []
        # split at the commas
        for i in title.split(","):
            # strip at each \n
            new.append(i.strip().strip("\n"))
        # add to the new list
        multi_dimensional_list.append(new)
    # remove the first row in the list
    headers = multi_dimensional_list.pop(0)
    # make the length of string x the length of the string of the headers
    multi_dimensional_list = [
        x for x in multi_dimensional_list if len(x) == len(headers)]
    # Dictionary keys are now the headers
    new_table.col_titles(headers)
    # set the column values as the values in the multi dimensional list
    new_table.col_values(multi_dimensional_list)
    return new_table


def read_table(file_name):
    # try x otherwise return none
    try:
        return read_table_helper(file_name)
    except:
        return None

def read_database():
    '''
    () -> Database
    This function reads the csv files and then cleans up the list
    and then sends it to a Database Class as the Keys and creates a list
    of Tables and returns.
    '''
    # create a database
    new_database = Database()
    # create a list
    table_list = []
    # for i in the list of files
    for i in file_list:
        # if the read table does not equal none
        if (read_table(i)) != None:
            # append the new database
            new_database.append_table(i, read_table(i))
    # return
    return new_database
