from reading import *
from database import *
# Below, write:
# *The cartesian_product function
# *All other functions and helper functions
# *Main code that obtains queries from the keyboard,
#  processes them, and uses the below function to output csv results


def cartesian_product(Table1, Table2):
    '''
    (Table, Table) -> Table
    The function takes 2 tables and joins them together to make a new one.
    REQ: must be tables with dictionaries inside them
    '''
    # create a new cartesian product Table
    cartesian_table = Table()
    # obtain the keys of the first Table
    Table1Keys = Table1.get_keys()
    # declare an empty list to store the values of the first Table
    Table2Keys = Table2.get_keys()
    # empty list
    Table3Lists = []
    # length of table1 column
    table1len = len(Table1.get_column(Table1Keys[0]))
    # length of table2 column
    table2len = len(Table2.get_column(Table2Keys[0]))
    # keys of cartesian_table are table1keys + table2keys
    cartesian_table.col_titles(Table1Keys+Table2Keys)
    # for loop through table1Keys
    for i in Table1Keys:
        temp = Table1.get_column(i)
        hold = []
        # loop through the length of temp
        for j in range(len(temp)):
            # loop throught the range of table2
            for k in range(table2len):
                hold.append(temp[j])
                # append and hold table3list
        Table3Lists.append(hold)
        # repeat loop for table2keys
    for i in Table2Keys:
        temp = Table2.get_column(i)
        hold = []
        for j in temp:
            hold.append(j)
        hold = hold*table1len
        Table3Lists.append(hold)
    # set cartesian table to the table3lists
    cartesian_table.cartesian_set_column(Table3Lists)
    # return
    return cartesian_table


def parse_query(query):
    # split at commas
    query[3] = query[3][1:len(query[3])-1].split(",")
    for i in range(len(query[3])):
        query[3][i] = str(query[3][i])+".csv"

    tables = query[3]
    if ((query[1][0] == "[") and (query[1][len(query[1])-1] == "]")):
        query[1] = query[1][1:len(query[1])-1].split(",")
    return query


def select_columns(query, Table):
    '''(str, Table) -> Table
    Takes a table column and pops it
    '''
    # for loop to get table keys
    for i in Table.get_keys():
        # if i is not in query incremint 1 then pop
        if i not in query[1]:
            Table.pop_column(i)
    # return
    return Table


def perform_query(query, where_clause = False):
    # equate database to readdatabase
    database = read_database()
    # create table
    cartesian_table_product = Table()
    # for loop that runs the range of length of query at increment 3
    for i in range(len(query[3])):
        # if i is less then the lehth of query
        if i < len(query[3])-2:
            # cartesian product is called and the query is run through it
            hold = cartesian_product(
                database.get_table(query[3][i]), database.get_table(
                    query[3][i+1]))
            cartesian_table_product = cartesian_product(
                hold, database.get_table(query[3][i+2]))
    # depending on the operation it returns a value
    if query[1] == "*" and where_clause == False:
        return cartesian_table_product
    if where_clause == False and query[1] != "*":
        return select_columns(query, cartesian_table_product)
    if where_clause == True and query[1] != "*":
        return perform_where_clause(select_columns(
            query, cartesian_table_product), query[5])
    if where_clause == True and query[1] == "*":
        return perform_where_clause(cartesian_table_product, query[5])


def perform_where_clause(table, clause):
    pass


def run_query(query):
    '''
    (str)-> bool
    with the use of helper functions will run query and use the cartesian
    product as needed.
    '''
    # strip and split
    query = query.strip().split(" ")
    # setting the base for the program
    if ((query[0] == "select" and query[2] == "from" and len(query) == 4)):
        query = parse_query(query)
        # return
        return perform_query(query)
    # else run parse_query and return
    elif (query[0] == "select" and query[2] == "from" and len(
        query) == 6 and query[4] == "where"):
        query = parse_query(query)
        return perform_query(query, True)
