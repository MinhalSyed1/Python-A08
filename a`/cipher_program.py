"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck.txt'
MSG_FILENAME = 'message.txt'
MODE = 'e'  # 'e' for encryption, 'd' for decryption.
def main():
    """ () -> NoneType

    open DECK_FILENAME. Use it to encrypt/decrypt the message in 
    MSG_FILENAME; if MODE is = 'e' encrypt otherwise decrypt if mode = 'd'
    """
    # open the file
    deck1 = open("deck1.txt", 'r')
    deck = read_deck(file)
    deck = cipher_functions.read_deck(deck)
  
    # open the message to read
    messages1 = open("message.txt", 'r')
    message = read_deck(file)
    messages = cipher_functions.read_messages(messages1)
    # encrypt or decrypt
    messages = cipher_functions.process_messages(deck,
                                                 messages, MODE)
    for message in messages:
        # print
        print(message)
main()
