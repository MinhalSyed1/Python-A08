class Table(object):

    def __init__(self, dict1={}, name=""):
        '''
        Initializes the code
        '''
        # contructors
        self._dict = dict1
        self._name = name
        self._current_dict = dict1

    def col_titles(self, col_name):
        '''
        (table, list of str) -> NoneType
        table is a list of titles
        Req: Column is a list of str
        '''
        # select column from column name
        self.col_name = col_name

    def get_title(self):
        '''
        gets the column names
        '''
        # getter helper function
        return self.col_name

    def cartesian_set_column(self, list_values):
        '''
        (table, list of list of str) -> NoneType
        Populates the columns that are used in cartesian product
        REQ: Must only contain strings and must be a list of a list
        '''
        # sets the coloumn headers it sets the values
        self.list_values = list_values
        # if the length of list_values is equivalent to col_name
        if len(self.list_values) == len(self.col_name):
            # construct a dict
            self._current_dict = {}
            # for indec in range of the length of the col name
            for i in range(len(self.col_name)):
                self._current_dict[self.col_name[i]] = self.list_values[i]

    def col_values(self, list_values):
        '''
        (table, list of list of str) -> NoneType
        Populates tables with the values of a list of a list and
        puts that values in the dictionary.
        REQ: Must only contain strings and must be a list of a list
        '''
        # equates self.values to list_values
        self.list_values = list_values
        # declare a new dictionary for the table
        self._current_dict = {}
        # for loop in the range of column name
        for i in range(len(self.col_name)):
            self._current_dict[self.col_name[i]] = [
                item[i]for item in self.list_values]

    def set_dict(self, input_dict):
        '''(table, dict of {str: list of str}) -> NoneType
        Populate this table with the data in input_dict.
        '''
        # Set the dictionary
        self._current_dict = input_dict

    def get_dict(self):
        '''(table) -> dict of {str: list of str}
        Return the dictionaryt with the list_values populating the
        columns and the headers being the eky
        '''
        # return the dictionary
        self._current_dict = {}
        return self._current_dict

    def get_column(self, name):
        '''(table) -> list
        REQ: name has to be a column title within the dictionary
        '''
        # return the values as a key
        return self._current_dict[name]

    def column(Table, query):
        '''
        (table, list of str) -> table

        Takes a table and a list of str as parameters and returns a table.
        Function would take 2 columns that the user told it to ant
        would pu that in a table and return.

        REQ: must be table with dictionaries
        '''
        self._current_dict = {}
        return _current_dict

    def get_keys(self):
        '''(table) -> list
        Returns all the keys of the dictionary within the table.
        '''
        # calls the keys function of the dictionary and casted as a list
        return list(self._current_dict.keys())

    def print_csv(self):
        '''(table) -> NoneType
        Print a representation of table in csv format.
        '''
        # no need to edit this one, but you may find it useful (you're welcome)
        dict_rep = self.get_dict()
        columns = list(dict_rep.keys())
        print(','.join(columns))
        rows = self.num_rows()
        for i in range(rows):
            cur_column = []
            for column in columns:
                cur_column.append(dict_rep[column][i])
            print(','.join(cur_column))

    def pop_column(self, name):
        # remove a column
        del self._current_dict[name]


class Database():

    def __init__(self, input_data={}):
        # constructor
        self._data_dict = input_data

    def get_file_titles(self):
        '''(database) -> list
        Populates this database with a list of file names
        REQ: table_name is only a list of strings
        '''
        return list(self._data_dict.keys())

    def append_table(self, table_name, inpt_table):
        '''(database) -> NoneType
        '''
        self._data_dict[table_name] = inpt_table

    def set_dict(self, input_dict):
        '''(Database, dict of {str: table}) -> NoneType
        Populate this database with the data in input_dict.
        input_dict must have the format:
            table_name: table
        '''
        self._data_dict = input_dict

    def get_dict(self):
        '''(Database) -> dict of {str: table}
        Return the dictionary representation of this database.
        The database keys will be the name of the table, and the value
        with be the table itself.
        '''
        return self._data_dict

    def get_table(self, table_name):
        # try x otherwise return none
        try:
            return self._data_dict[table_name]
        except:
            return None
