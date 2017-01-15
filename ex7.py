def create_dict(file):
    username_to_description = {}
    next_line = file.readline()
    words_list = next_line.split()
    list_in_order = ([words_list[2]] + [words_list[1]] + [words_list[-1]] +
                     words_list[3:5])
    while(next_line != ''):
        username_to_description[words_list[0]] = list_in_order
        next_line = file.readline()
        if next_line != '':
            words_list = next_line.split()
            list_in_order = ([words_list[2]] + [words_list[1]] +
                             [words_list[-1]] + words_list[3:5])
    return (username_to_description)


def update_field(my_dict, username, field, value):
    values_list = my_dict[username]
    if field == 'LAST':
        values_list[0] = value
        my_dict[username] = values_list
    elif field == 'FIRST':
        values_list[1] = value
        my_dict[username] = values_list
    elif field == 'E-MAIL':
        values_list[2] = value
        my_dict[username] = values_list
    elif field == 'AGE':
        values_list[3] = value
        my_dict[username] = values_list
    elif field == 'GENDER':
        values_list[4] = value
        my_dict[username] = values_list
