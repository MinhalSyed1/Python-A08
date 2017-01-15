def copy_me(OG_list):
    # create a copy of the original list
    NewG_list = OG_list[:]
    # loop through every value in the list
    for x in range(0, len(NewG_list)):
        # if the value is a string, convert all letters to upper-case
        if type(NewG_list[x]) is str:
            NewG_list[x] = NewG_list[x].upper()
        # if the value is an integer or float, have their value increased by 1
        if type(NewG_list[x]) is int or type(NewG_list[x]) is float:
            NewG_list[x]=NewG_list[x] + 1
        # if the value is a boolean, the value is negated
        if type(NewG_list[x]) is bool:
            NewG_list[x] = not(NewG_list[x])
        # if the value is a list, "list" becomes the value
        if type(NewG_list[x]) is list:
            NewG_list[x] = "List"
    return (NewG_list)


def mutate_me(OG_list):
    # loop through every value in the list
    for x in range(0, len(OG_list)):
        # if the value is a string, convert all letters to upper-case
        if type(OG_list[x]) is str:
            OG_list[x] = OG_list[x].upper()
        # if the value is an integer or float, have their value increased by 1
        if type(OG_list[x]) is int or type(OG_list[x]) is float:
            OG_list[x] += 1
        # if the value is a boolean, the value is negated
        if type(OG_list[x]) is bool:
            OG_list[x] = not(OG_list[x])
        # if the value is a list, "list" becomes the value
        if type(OG_list[x]) is list:
            OG_list[x] = "List"

