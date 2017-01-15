# Code for working with word search puzzles
#
# Do not modify the existing code
#
# Complete the tasks below marked by *task*
#
# Before submission, you must complete the following header:
#
# I hear-by decree that all work contained in this file is solely my own
# and that I received no help in the creation of this code.
# I have read and understood the University of Toronto academic code of
# behaviour with regards to plagiarism, and the seriousness of the
# penalties that could be levied as a result of committing plagiarism
# on an assignment.
#
# Name: Mohammad Minhal Syed
# MarkUs Login: syedmo17

PUZZLE1 = '''
tlkutqyu
hyrreiht
inokdcne
eaccaayu
riainpaf
rrpnairb
ybybnick
ujvaynak
'''

PUZZLE2 = '''
fgbkizpyjohwsunxqafy
hvanyacknssdlmziwjom
xcvfhsrriasdvexlgrng
lcimqnyichwkmizfujqm
ctsersavkaynxvumoaoe
ciuridromuzojjefsnzw
bmjtuuwgxsdfrrdaiaan
fwrtqtuzoxykwekbtdyb
wmyzglfolqmvafehktdz
shyyrreihtpictelmyvb
vrhvysciipnqbznvxyvy
zsmolxwxnvankucofmph
txqwkcinaedahkyilpct
zlqikfoiijmibhsceohd
enkpqldarperngfavqxd
jqbbcgtnbgqbirifkcin
kfqroocutrhucajtasam
ploibcvsropzkoduuznx
kkkalaubpyikbinxtsyb
vjenqpjwccaupjqhdoaw
'''


def rotate_puzzle(puzzle):
    '''(str) -> str
    Return the puzzle rotated 90 degrees to the left.
    '''

    raw_rows = puzzle.split('\n')
    rows = []
    # if blank lines or trailing spaces are present, remove them
    for row in raw_rows:
        row = row.strip()
        if row:
            rows.append(row)

    # calculate number of rows and columns in original puzzle
    num_rows = len(rows)
    num_cols = len(rows[0])

    # an empty row in the rotated puzzle
    empty_row = [''] * num_rows

    # create blank puzzle to store the rotation
    rotated = []
    for row in range(num_cols):
        rotated.append(empty_row[:])
    for x in range(num_rows):
        for y in range(num_cols):
            rotated[y][x] = rows[x][num_cols - y - 1]

    # construct new rows from the lists of rotated
    new_rows = []
    for rotated_row in rotated:
        new_rows.append(''.join(rotated_row))

    rotated_puzzle = '\n'.join(new_rows)

    return rotated_puzzle


def lr_occurrences(puzzle, word):
    '''(str, str) -> int
    Return the number of times word is found in puzzle in the
    left-to-right direction only.

    >>> lr_occurrences('xaxy\nyaaa', 'xy')
    1
    '''
    return puzzle.count(word)

# ---------- Your code to be added below ----------

# *task* 3: write the code for the following function.
# We have given you the header, type contract, example, and description.


def total_occurrences(puzzle, word):
    '''(str, str) -> int
    Return total occurrences of word in puzzle.
    All four directions are counted as occurrences:
    left-to-right, top-to-bottom, right-to-left, and bottom-to-top.
    >>> total_occurrences('xaxy\nyaaa', 'xy')
    2
    '''
    # your code here
    # call left-to-right function and rotate puzzle function
    lr_occurrences(puzzle, word)
    rotate_puzzle(puzzle)
    # number of times word occours at 0 rotation
    left_right_occurrence = (lr_occurrences(puzzle, word))
    # number of times word occours at 1 rotation
    top_bottom_occurrence = (lr_occurrences(rotate_puzzle(puzzle), word))
    # number of times word occours at 2 rotation
    right_left_occurrence = (lr_occurrences(rotate_puzzle(rotate_puzzle
                                                          (puzzle)), word))
    # number of times word occours at 3 rotation
    bottom_top_occurrence = (lr_occurrences(rotate_puzzle(rotate_puzzle
                             (rotate_puzzle(puzzle))), word))
    # return how many times word has occured
    result = ((left_right_occurrence) + (top_bottom_occurrence) +
              (right_left_occurrence) + (bottom_top_occurrence))
    return result
# *task* 5: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle_horizontal(puzzle, word):
    '''(str,str)-> bool
        The function searches throughout the puzzle to see the users inputted
        word. If the user's word is found horizontally it returns true
        otherwise it returns a false.
        REQ: Puzzle must be PUZZLE1 or PUZZLE2
        >>>in_puzzle_horizontal(PUZZLE1, 'nick')
        True
        >>>in_puzzle_horizontal(PUZZLE1, 'mineralz')
        False
        >>>in_puzzle_horizontal(PUZZLE2, 'jim')
        False
        >>>in_puzzle_horizontal(PUZZLE2, 'brian')
        True
        '''
    # setting left to right occourence
    left_right_occurrence = ((lr_occurrences(puzzle, word)) > 0)
    # setting right to left occourence
    right_left_occurrence = ((lr_occurrences(rotate_puzzle(rotate_puzzle(
                                                          puzzle)), word)) > 0)
    in_puzzle_horizontal = (left_right_occurrence or right_left_occurrence)
    # return  true or false
    return in_puzzle_horizontal
    # *task* 8: write the code for the following function.
    # We have given you the function name only.
    # You must follow the design recipe and complete all parts of it.
    # Check the handout for what the function should do.


def in_puzzle_vertical(puzzle, word):
    '''(str,str)-> bool
    The function searches throughout the puzzle to see the users inputted
    word. If the user's word is found vertically it returns true
    otherwise it returns a false.
    REQ: Puzzle must be PUZZLE1 or PUZZLE2
    >>>in_puzzle_vertical(PUZZLE1, 'thierry')
    True
    >>>in_puzzle_vertical(PUZZLE1, 'Mineralz')
    False
    >>>in_puzzle_vertical(PUZZLE2, 'nick')
    True
    >>>in_puzzle_vertical(PUZZLE2, 'Mineralz')
    False
    '''
    # set top to bottom occourence
    top_bottom_occurrence = ((lr_occurrences(rotate_puzzle(puzzle), word)) > 0)
    # set bottom to top occourence
    bottom_top_occurrence = ((lr_occurrences(rotate_puzzle(rotate_puzzle
                                             (rotate_puzzle
                                                 (puzzle))), word)) > 0)
    in_puzzle_vertical = (top_bottom_occurrence or bottom_top_occurrence)
    # return true or false
    return in_puzzle_vertical

# *task* 9: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle(puzzle, word):
    ''' (str,str)->bool
    returns true if word is found anywhere in the puzzle in any direction
    REQ: Puzzle must be PUZZLE1 or PUZZLE2
    >>>in_puzzle(PUZZLE1, 'brian')
    True
    >>> in_puzzle(PUZZLE1, 'Mineralz')
    False
    >>> in_puzzle(PUZZLE2, 'nick')
    False
    >>>in_puzzle(PUZZLE2, 'Mineralz')
    False
    '''
    # if word is found top to bottom or bottom to top it will be true
    up_down = (in_puzzle_vertical(puzzle, word) > 0)
    # if word is fount left to right or right to left it will be true
    left_right = (in_puzzle_horizontal(puzzle, word) > 0)
    in_puzzle = (up_down or left_right)
    return in_puzzle


# *task* 10: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_exactly_one_dimension(puzzle, word):
    ''' (str, str,) -> bool
    only rerturns true if the given word is in the puzzle only one way.
    REQ: Puzzle must be PUZZLE1 or PUZZLE2
    >>>in_exactly_one_dimension (PUZZLE1, 'Mineralz')
    False
    >>>in_exactly_one_dimension (PUZZLE1, 'brian')
    True
    >>>in_exactly_one_dimension (PUZZLE2, 'brian')
    True
    >>>in_exactly_one_dimension (PUZZLE1, 'Mineralz')
    False
    '''

    # horizontal function
    horizontal = in_puzzle_horizontal(puzzle, word)
    # vertical function
    vertical = in_puzzle_vertical(puzzle, word)
    # let result  be true when its one or the other, not both
    result1 = (horizontal and vertical) == False
    result2 = (horizontal or vertical) == True
    # return result 1 and 2
    return (result1 and result2)

# *task* 11: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def all_horizontal(puzzle, word):
    '''(str,str)->bool
    return True iff all occurrences of the supplied word are
    horizontal in the puzzle. If the word is not in the puzzle at all, then
    True is returned.
    REQ: Puzzle must be PUZZLE1 or PUZZLE2
    >>>all_horizontal(PUZZLE1, 'brian')
    True
    >>>all_horizontal(PUZZLE1, 'thierry')
    False
    >>>all_horizontal(PUZZLE2, 'cam')
    True
    >>>all_horizontal(PUZZLE2, 'mineralz')
    True
    '''
    # left to right occourance is equal to no rotation
    left_right_occurrence = ((lr_occurrences(puzzle, word)) > 0)
    # right to left occourence is equal to 3 rotation
    right_left_occurrence = ((lr_occurrences(rotate_puzzle(rotate_puzzle(
                                                          puzzle)), word)) > 0)
    # setting horizontal, vertical and DNE as variables
    horizontal = in_puzzle_horizontal(puzzle, word)
    vertical = (in_puzzle_vertical(puzzle, word) == 0)
    DNE = (in_puzzle(puzzle, word) == 0)
    all_horizontal = ((horizontal and vertical) or DNE)
    return (all_horizontal)


# *task* 12: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def at_most_one_vertical(puzzle, word):
    '''(str,str)->bool
    True if the word occourse only once vertically. otherwise false.
    REQ: Puzzle must be PUZZLE1 or PUZZLE2
    >>>at_most_one_vertical(PUZZLE1, 'paco')
    True
    >>>at_most_one_vertical(PUZZLE1, 'brian')
    False
    >>>at_most_one_vertical(PUZZLE2, 'paco')
    True
    >>>at_most_one_vertical(PUZZLE2, 'nick')
    False
    '''
    # occurs only once vertically
    vertical = (in_puzzle_vertical(puzzle, word) == 1)
    # Horizontal does not exist
    HorizontalDNE = (in_puzzle_horizontal(puzzle, word) == 0)
    # result is the combination of the 2 variables
    result = (vertical and HorizontalDNE)
    # return result
    return result


def do_tasks(puzzle, name):
    '''(str, str) -> NoneType
    puzzle is a word search puzzle and name is a word.
    Carry out the tasks specified here and in the handout.
    '''
    # *task* 1a: add a print call below the existing one to print
    # the number of times that name occurs in the puzzle left-to-right.
    # Hint: one of the two starter functions defined above will be useful.

    # the end='' just means "Don't start a newline, the next thing
    # that's printed should be on the same line as this text
    print('Number of times', name, 'occurs left-to-right: ', end='')
    # your print call here
    print(lr_occurrences(puzzle, name))
    # *task* 1b: add code that prints the number of times
    # that name occurs in the puzzle top-to-bottom.
    # (your format for all printing should be similar to
    # the print statements above)
    # Hint: both starter functions are going to be useful this time!
    print('Number of times', name, 'occurs top-to-bottom: ', end='')
    # rotate puzzle amd print call
    print(lr_occurrences(rotate_puzzle(puzzle), name))
    # *task* 1c: add code that prints the number of times
    # that name occurs in the puzzle right-to-left.
    print('Number of times', name, 'occurs right-to-left: ', end='')
    print(lr_occurrences(rotate_puzzle(rotate_puzzle(puzzle)), name))
    # *task* 1d: add code that prints the number of times
    # that name occurs in the puzzle bottom-to-top.
    print('Number of times', name, 'occurs bottom-to-top: ', end='')
    print(lr_occurrences(rotate_puzzle(rotate_puzzle(rotate_puzzle
                                                     (puzzle))), name))
    # *task* 4: print the results of calling total_occurrences on
    # puzzle and name.
    # Add only one line below.
    # Your code should print a single number, nothing else.
    print (total_occurrences(puzzle, name))
    # *task* 6: print the results of calling in_puzzle_horizontal on
    # puzzle and name.
    # Add only one line below. The code should print only True or False.
    print (in_puzzle_horizontal(puzzle, name))
#
do_tasks(PUZZLE1, 'brian')

# *task* 2: call do_tasks on PUZZLE1 and 'nick'.
# Your code should work on 'nick' with no other changes made.
# If it doesn't work, check your code in do_tasks.
# Hint: you shouldn't be using 'brian' anywhere in do_tasks.
do_tasks(PUZZLE1, 'nick')

# *task* 7: call do_tasks on PUZZLE2  and 'nick'.
# Your code should work on the bigger puzzle with no changes made to do_tasks.
# If it doesn't work properly, go over your code carefully and fix it.
do_tasks(PUZZLE2, 'nick')

# *task* 9b: print the results of calling in_puzzle on PUZZLE1 and 'nick'.
# Add only one line below. Your code should print only True or False.
print (in_puzzle(PUZZLE1, 'nick'))

# *task* 9c: print the results of calling in_puzzle on PUZZLE2 and 'thierry'.
# Add only one line below. Your code should print only True or False.
print (in_puzzle(PUZZLE2, 'thierry'))
