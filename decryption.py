"""

:Student: Craig Smith
:Week-4: Loops
:Module: Caesar Cyper Encryption
:Course: CMIT-135-40D (Champlain College)
:Professor: Steve Giles
:Author: Steve Giles
:Edited: Craig Smith

Purpose
-------
This program is provided by the course instructor to utilize in a group programming
project to come up with a decryption method.

Constraints
-----------
1. Determine how to modify the code to decrypt the message

"""
# Caesar Cypher Encryption

if __name__ == '__main__':                        # added to protect from sphinx
    # Get the message to encrypt from the user
    print('Enter your encrypted message:')                                                        # Prompt to enter encrypted message
    unencryptedMessage = input()                                                                  # Modify variable name to say encryptedMessage

    # Get the encryption key from the user.  Note the error handling to make sure we have a number from 1-26
    key = 0                                                                                       # No modification required
    while key < 1 or key > 26:                                                                    # No Modification required
        print('Enter the key number (1-26)')                                                      # No Modification required
        key = int(input())                                                                        # No Modification required

    print('The key is ' + str(key))                                                               # No Modification required

    # We will start with an empty string as our encryptedMessage
    encryptedMessage = ''                                                                         # Change variable to say decrptedMessage

    # For each symbol in the unencryptedMessage we will add an encrypted symbol into the encryptedMessage
    for symbol in unencryptedMessage:                                                             # Change for loop to go through the encryptedMessage
        if symbol.isalpha():                                                                      # No Change required here, since we know that non-alphas are left unchanged
            num = ord(symbol)                                                                     # No Change required here, we need to convert the symbol to its ordinal value to manipulate it
            num -= key                                                                            #

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            encryptedMessage += chr(num)
        else:
            encryptedMessage += symbol

    print("Your encrypted message is:")
    print(encryptedMessage)
