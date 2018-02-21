#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: IL WON SON
Assignment 2 - This program decrypts cipher 1 and 2.
Reference: http://practicalcryptography.com
           Hacking Secret Ciphers with Python by AI Sweigart
"""
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = LETTERS + LETTERS.lower() + ' \t\n'

def hackOneTwo():
    
    '''
    #1. fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc
    #2. oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy
    '''
    
    # change the comment to decrypt other ciphertext
    #ciphertext = 'fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc'
    ciphertext = 'oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy'
    
    #print(ciphertext.split())
    #print(ciphertext)
    listOfDeciphertext = []
    
    # Loop through every possible key.
    for key in range(len(LETTERS)):
        
        # It is important to set translated to the black string so that the
        # previous iteration's value for translated is cleared.
        plaintext = ''
        
        # Run the decription code on each symbol in the cipher.
        for char in ciphertext.upper():
            if char.isalpha():
                num = LETTERS.find(char) # Get the index number of the symbol.
                num = num - key # Caesar cipher, subtracking the key decrypts and adding the key encrypts.
                
                if num < 0: # Check if num is negative, if so, wrap around with 26 to make positive.
                    num = num + len(LETTERS)
                    
                plaintext = plaintext + LETTERS[num] # add number's symbol at the end of plaintext.
            
            else:
                plaintext = plaintext + char # Add non-letters to plaintext
        
        #print('Key #%s: %s' % (key, plaintext.upper()))
        listOfDeciphertext.append(plaintext)
    #print(listOfDeciphertext)
    
    #---------Check for complete--------------#
    result = 0
    for k in range(len(listOfDeciphertext)):
        text = ''.join(listOfDeciphertext[k].split())
        #print(text)
        candidates = []
        for n in range(8):
            i, j = 0, n 
            for x in range(len(text)):
                temp = text[i:j]
                if temp in ENGLISH_WORDS: # if Words are in Dictionary add to candidates
                    candidates.append(temp)
                i += 1
                j += 1
        #print(candidates, len(candidates))
        if len(candidates) > 15: # if candidates are sufficent, then program completes
            result = k
    if result > 0:
        print('\nCiphertext: ' + ciphertext)
        print(' Plaintext: ' + listOfDeciphertext[result])
        print('       Key: %d' % (result))
    else:
        print('Sorry, could not decrypt the text.')
    
    
    '''
    Plaintext spaceing inprogress.
    
    for word in listtemp:
        if word in ENGLISH_WORDS:
            candidates.append(word)
    
    #spaces
    for x in range(len(frontspace)):
        print(frontspace[x],backspace[x])
        text = text[:space[x]] + ' ' + text[space[x]:]
    print(text)
    args = [iter(text)] * 5
    listOfText = [''.join(k) for k in zip_longest(*args,fillvalue='_')]
    print(listOfText)
    '''
    
#-----------------------------------------------------------
def loadDictionary():
    dictionaryFile = open('dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()

