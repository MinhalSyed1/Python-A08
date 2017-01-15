def function_names(file_name):
    # make a new list to store the names of the functions
    total = []
    # read the file as a list
    function_name = file_name.readlines()
    # check every line
    for x in function_name:
        # split every word of the sentance into a list
        list_list = x.split()
        # look for the word "def"
        if "def" in list_list:
            # find the word after "def"
            name_with_parentheses = list_list[list_list.index("def") + 1]
            # remove the parentheses
            name_without_parentheses = (
                name_with_parentheses[:name_with_parentheses.index('(')])
            # add it to the list of names of functions
            total.append(name_without_parentheses)
    return (total)


def justified(file_name):
    # read the first line
    next_line = file_name.readline()
    # set justified to be True to begin with
    justified = True
    # so long as there is more to read, read the next line
    while(next_line != ''):
        # if any lines start with a space and tab return False
        if next_line.startswith(' ') and next_line.startswith('\t'):
            justified = False
            # read the next line
            next_line = file_name.readline()
        else:
            # read the next line
            next_line = file_name.readline()
    # close the file
    file_name.close()
    return (justified)
