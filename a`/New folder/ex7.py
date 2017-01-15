def create_dict(file):
    '''
    (io.TextIOWrapper) -> dict of {str: [str, str, str, int, str]}
    This function takes one parameter, an open file handle and returns a
    dictionary that maps a string to a list of strings and ints
    REQ: each line of the file must contain the username, first name, last
    name, age, gender and email in that order separated with a space
    REQ: first name, last name, gender and email must be string values
    REQ: age must be a integer
    '''
    # create an empty dictionary
    username_to_description = {}
    # read first line of the file
    next_line = file.readline()
    # split each line up to its individual words
    words_list = next_line.split()
    # rearrange the order of the words
    list_in_order = ([words_list[2]] + [words_list[1]] + [words_list[-1]] +
                     words_list[3:5])
    # so long as there is more to read, read the next line
    while(next_line != ''):
        # match the username to its values
        username_to_description[words_list[0]] = list_in_order
        # read the next line
        next_line = file.readline()
        # so long as there's more lines to read:
        if next_line != '':
            # split each line up to its individual words
            words_list = next_line.split()
            # rearrange the order of the words
            list_in_order = ([words_list[2]] + [words_list[1]] +
                             [words_list[-1]] + words_list[3:5])
    return (username_to_description)


def update_field(my_dict, username, field, value):
    '''
    (dict of {str: [str, str, str, int, str]}, str, str, str/int) -> None
    This function takes 4 parameters: A dictionary in the format created by
    the previous function, a username, the name of a field, and a new value
    to replace the current value of the specified field
    REQ: dictionary must be in the format created by the previous function
    REQ: username must match username in dictionary
    REQ: field must be a captial string value of either 'LAST’, ’FIRST’,
    ’E-MAIL’, ’AGE’ or ’GENDER’
    REQ: value should be an integer for AGE and string for any of the other
    fields
    '''
    # get the stored information from the username
    values_list = my_dict[username]
    # if the last name field is asked to be changed
    if field == 'LAST':
        # change the last name value
        values_list[0] = value
        # update the dictionary
        my_dict[username] = values_list
    # if the last name field is asked to be changed
    elif field == 'FIRST':
        # change the first name value
        values_list[1] = value
        # update the dictionary
        my_dict[username] = values_list
    # if the last name field is asked to be changed
    elif field == 'E-MAIL':
        # change the email value
        values_list[2] = value
        # update the dictionary
        my_dict[username] = values_list
    # if the last name field is asked to be changed
    elif field == 'AGE':
        # change the age value
        values_list[3] = value
        # update the dictionary
        my_dict[username] = values_list
    # if the last name field is asked to be changed
    elif field == 'GENDER':
        # change the gender value
        values_list[4] = value
        # update the dictionary
        my_dict[username] = values_list
