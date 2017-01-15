def insert(ListA, ListB, index):
    '''(list, list)->float

     Places list 2 into list 1 after the index and then outputs the rest of
     list1

     REQ: original and inserted are either lists or strings
     REQ: index is an integer > = 0

     >>> insert([1, 2, 3], ['a', 'b', 'c'], 2)
     [1, 2, 'a', 'b', 'c', 3]
     >>> insert("123","abc",2)
     '12abc3'
    '''
    # Basically it is saying the list goes from term1 to the index
    # and then it inserts list2 after the first list.
    # and then continues the list after.
    newline = ListA[0:index] + ListB + ListA[index:]
    return(newline)


def up_to_first(ListA, object):
    '''(list,object) -> list
    Returns a copy of the list up to (but not including) the first
    occurrence of that object, or all of the elements if that object is not
    in the list.
    REQ: Do not pass an empty.
    >>> up_to_first([1, 2, 3, 4], 3)
    [1, 2]
    >>> up_to_first([1, 2, 3, 4], 9)
    [1, 2, 3, 4]
    '''
    if (type(ListA) is str):
        list1 = list(str)
        return "".join(list1[:object-1])  # -1 because one less value then
    # the index.
    else:
        return ListA[:object-1]  # -1 because one less value then
    # the index.


def cut_list(list1, index):
    '''(list, int,)->list
    Returns list after it has been switched on either side of the index.
    >>> cut_list([0,1,2,3,4,5,6,7,8,9], 3)
    [4, 5, 6, 7, 8, 9, 3, 0, 1, 2]
    >>> cut_list("ABCDEFGX1234",7)
    '1234XABCDEFG'
    '''
    if type(list1) is str:
        # if the list is a string, split the original list at the index
        # add the index value to the end of the list
        new = list1[index+1:] + list1[index]
        new1 = list1[0:index]
    else:
        # if the list is a list, split the original list at the index
        # add the index value to the end of the list
        new = list1[index+1:] + [list1[index]]
        new1 = list1[0:index]
    return (new + new1)
