# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28
# Write your functions here:
Letters_in_alphabet = 26

def clean_message(message):
    ''' str-> str
    Will take a line of text. Returns a copy of the message with only
    the alphabetical which will all be capital. 

    Req: Only be 1 line

    >>> clean_message('I213123L123o1232v2134e2134321bri09898an')
    'ILOVEBRIAN'
    >>> clean_message('123456789')
    ''
    '''
    # declare upper case letters
    upper_case = ''
    # for char in messages
    for char in message:
        # check if has an alphabetical charachter
        if (char.isalpha()):
            # make the letters uppercase
            upper_case += char.upper()
    return upper_case


def encrypt_letter(charachter, keystream):
    ''' (str, int) -> str
    Takes the charachter and a keystream value then encrypts and returns
    result.

    Req: Charachter first then number
    Req: Letter should be alphabetical string 
    Req: int must be between 0 and 26

    >>>encrypt_letter('B', 0)
    'B'
    >>>encrypt_letter('M', 1) 
    'N'
    >>>encrypt_letter('Z', 26)
    'Z'
    '''
    # Uppercase the letter
    upper_case = charachter.upper()
    # find the number value of A
    numerical_charachter = (ord(upper_case)-ord('A'))
    # add the keystone value to nymber value of A
    # take the answer mod 26 as there is 26 letters in the alphabet
    encrypted_charachter = ((numerical_charachter + keystream)
                                  % Letters_in_alphabet)
    # turn the number back into the letter
    encrypted_letter = chr(encrypted_charachter + ord('A'))
    return encrypted_letter


def decrypt_letter(charachter, keystream):
    ''' (str, int)->str
    Takes in a charachter and string value and will decrypt the result
    REQ: letter should be string
    REQ: int must be between 0 and 26
    REQ: Char first, then number

    >>>decrypt_letter('A', 9)
    'R'
    >>>decrypt_letter('D', 25)
    'E'
    >>>decrypt_letter('Z', 29)
    'W'
    '''
    # Uppercase the letter
    upper_case = charachter.upper()
    # find the number value of A
    numerical_charachter = (ord(upper_case) - ord('A'))
    # subtract the numerical value of the charachter by the keystream
    # if positive then
    if ((numerical_charachter - keystream) >= 0):
	# decrypt
        Decryptchar = (numerical_charachter - keystream)
    else:
	# else add 26
        Decryptchar = (
                    numerical_charachter - keystream + Letters_in_alphabet)
        # decrypt
    decrypted = chr(Decryptchar + ord('A'))
    return decrypted


def swap_cards(deck, index):
    '''
    (list of int, int) -> NoneType

    The function takes the first parameter as a deck and the
    other as an index for the deck where the card will be swapped with
    the one that follows it.
    
    REQ: index must 0 <= index < len(deck)
    REQ: ints only

    >>> deck = [101, 102, 103, 104, 105]
    >>> swap_cards(deck, 104)
    >>> print(deck)
    [105, 102, 103, 104, 101]
    '''    
    # if index is equivalent to the length of the deck to the last card
    if (index == len(deck)-1):
        # the first card's value is the last card's value
        deck1 = deck[-1]
        # the first card's value is the last card's value
        deck[-1] = deck[0]
        deck[0] = deck1
    else:
        # the index card's value is the next card's value
        deck2 = deck[index + 1]
        # the card next to the index's value is the index card's value
        deck[index + 1] = deck[index]  
        deck[index] = deck2 


def move_joker_1(deck):
    '''
    (list of int) -> NoneType

    Function will find a joker in the deck of cards and swap it with the 
    following card. 

    REQ: must have 27

    >>> deck_of_cards = [11, 12, 13, 14, 27]
    >>> move_joker_1(deck)
    >>> print(deck)
    [27, 12, 13, 14, 11]
    '''
    # joker1 index and then swap it with the next card
    index = deck.index(JOKER1)
    swap_cards(deck, index)    


def move_joker_2(deck):
    '''
    (list of int) -> NoneType

    Will find joker2 and move it 2 cards down.
    
    REQ: must include 28

    >>> deck_of_cards = [1, 2, 3, 4, 27, 28]
    >>> move_joker_2(deck_of_cards)
    >>> print(deck_of_cards)
    [2, 28, 3, 4, 27, 1]
    '''
    # find joker 2 and then move it down 2 spots.
    for shifts in range(0, 2):
        index = deck.index(JOKER2)
        swap_cards(deck, index)


def triple_cut(deck):
    '''
    (list of int) -> NoneType

    This function will takethe deck, find the jokers and do a triple cut

    REQ:deck must include 27 and 28

    >>> deck = [21, 22, 27, 28, 23, 24]
    >>> triple_cut(deck)
    [21, 22, 27, 28, 23, 24]

    >>> deck = [1, 27, 2, 28, 3, 4]
    >>> triple_cut(deck)
    [3, 4, 27, 2, 28, 1]
    '''
    # searches index to see if joker 1 comes before joker 2
	# deck = index of joker 1
	# deck = indec of joker 2
	# everything agter joker 1 will now be after joker 2
	# if joker 2 comes before joker 1
	# find position of joker 2
	# everything agter joker 2 will now be after joker 1
    if(deck.index(JOKER1) > deck.index(JOKER2)):  
	    deck = deck[deck.index(JOKER1) + 1:] + \
	    deck[deck.index(JOKER2):deck.index(JOKER1) + 1] + \
	    deck[:deck.index(JOKER2)]
	    return deck
    if(deck.index(JOKER1) < deck.index(JOKER2)):
	    deck = deck[deck.index(JOKER2) + 1:] + \
	    deck[deck.index(JOKER1):deck.index(JOKER2) + 1] + \
	    deck[:deck.index(JOKER1)]
	    return deck


def insert_top_to_bottom(deck):
    '''
    (list of int) -> NoneType

    This function will look at the bottom card of the deck
    move that many cards from the top of the deck to the bottom
    inserting them just above the bottom card.

    REQ: deck  must include 27

    >>> deck = [1, 2, 3, 4, 5, 6, 28, 8, 9, 10, 11, 12, 13, 14,
    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 7]
    >>> insert_top_to_bottom(deck)
    >>> print(deck)
    [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
    25, 26, 27, 1, 2, 3, 4, 5, 6, 28, 7]
    ''' 
    # clone deck
    deckcloned = deck[:]
    # find the value of the last card
    last = deck[-1]
    # if the value of the last card is JOKER2
    if (last == JOKER2):
        # change it to JOKER1
        last = JOKER1
    # list starts from the value of the last card to the last card
    beginning = deck[last:-1]
    # put together the middle of the deck
    middle = deck[0:last]
    # last card
    end = [deckcloned[-1]]
    # put the deck together
    deck[:] = beginning + middle + end


def get_card_at_top_index(deck):
    '''
    (list of int) -> int

    This function will take a deck of cards as the parameter and
    looking at the top card. Using that value as an index, return the
    card in that deck at that index.

    REQ: must include 27 and 28

    >>> get_card_at_top_index([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3,
    6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    4
    '''
    # get the value at the 0th index
    topcard = deck[0]
    # if the card's value is JOKER2, use JOKER1 as the index
    if (topcard == JOKER2):
        topcard = JOKER1
    # get the value
    value= deck[topcard]
    return (value)


def get_next_value(deck):
    '''
    (list of int) -> int

    This function will return the next potential key string value.

    REQ: must include 27 and 28
    >>> get_next_value([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9,
    12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    11
    '''
    # move JOKER1 down a position
    move_joker_1(deck)
    # move JOKER2 down 2 positions
    move_joker_2(deck)
    # do a triple cut
    triple_cut(deck)
    # look at bottom card, move that many cards from the top of the
    # deck to the bottom
    insert_top_to_bottom(deck)
    # keystream value is at the top card's index of deck
    keystream = get_card_at_top_index(deck)
    return(keystream)


def get_next_keystream_value(deck):
    '''
    (list of int) -> int

    Function that repeats all five steps of the algorithm until
    it gets a valid answer

    REQ: must include 27 and 28 

    >>> get_next_keystream_value([12, 21, 22, 2, 20, 1, 17, 15, 26, 18,
    6, 4, 7, 10, 13, 16, 19, 14, 23, 25, 9, 27, 28, 3, 5, 8, 11, 24])
    22
    '''
    # first card equals joker2
    key_stream_value = JOKER2
    # while value is a joker
    while (key_stream_value == JOKER1 or key_stream_value == JOKER2):
        # get next value 
        key_stream_value = get_next_value(deck)
    return(key_stream_value)


def process_message(deck, message, encrypt_or_decrypt):
    '''
    (list of int, str, str) -> str

    The first parameter represents a deck of cards. The second
    represents a message to encrypt or decrypt based on the third
    parameter, which is either 'e' (to encrypt) or 'd' (to decrypt).

    REQ: must have 27 or 28
    REQ: encrypt_or_decrypt is 'd' or 'e'

    >>>process_message([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12,
    15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26], 'ok!', 'e')
    'ZT'
    '''
    # declare encrypted or decrypted_message
    encrypted_decrypted_message = ''
    # clean the message
    all_letters = clean_message(message)
    # for every letter in message
    for letters in all_letters:
        # if the message should be encrypted
        if encrypt_or_decrypt == 'e':
            # find a keystream value
            keystream_value = get_next_keystream_value(deck)
            # encrypt letter with keystream
            encrypted_letter = encrypt_letter(letters, keystream_value)
            # add the encrypted letter to the message
            encrypted_decrypted_message += encrypted_letter
        # else
        else:
               # # find a keystream value
                keystream_value = get_next_keystream_value(deck)
                # decrypt letter with keystream
                decrypted_letter = decrypt_letter(letters, keystream_value)
                # add the decrypted letter to the decrypted message
                encrypted_decrypted_message += decrypted_letter
    return(encrypted_decrypted_message)


def process_messages(deck, messages_list, encrypt_or_decrypt):
    '''
    (list of int, list of str, str) -> list of str
    
    This function will use the process_message function to return a
    list of messages.    
    '''
    # a list ofa list of messages
    list_messages =[]
    # for all message in list
    for message in messages_list:
	# process message
        message = process_message(deck, encrypt_or_decrypt)
	# add to message
        list_message.append(message)
    return(list_message)


def read_messages(file):
    '''
    (io.TextIOWrapper) -> list of str
    Read and return the contents of the file as a list of messages. 
    Strip the newline from each line.
    
    REQ: Open file
    ''' 
    # declare list of messages
    messages = []
    # do all inside
    for line_read in list2:
        # strip
        line_read = line_read.strip()
        # add the message to the list of messages
        messages.append(line_read)
    return (list_messages)


def read_deck(file):
    '''
    (io.TextIOWrapper) -> list of int    
   Read and return the contents of the file.

    REQ: Open file
    '''
    # read the first line
    each_line = file.readline()
    # put each string into a list
    cards_as_list = each_line.split()
    # make an empty cards list
    cards_values_list = []
    # do everything inside so long as there is another line after
    while(each_line != ''):
        # do everything inside so long as there is a string in the list
        for every_card in cards_as_list:
            # add every individual number as an integer to the list
            cards_values_list.append(int(every_card))
        # read the next line
        each_line = file.readline()
        # put each string into a list
        cards_as_list = each_line.split()
    return (cards_values_list)