#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: IL WON SON
Assignment 2 - This program decrypts cipher 3 and 4.
Reference: http://practicalcryptography.com
           Hacking Secret Ciphers with Python by AI Sweigart
"""
from pycipher import SimpleSubstitution
import random, re
from quintgramScore import quintgramScore

fitness = quintgramScore('english_quintgrams.txt')

'''
#3. ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae
#4. iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq iihed yzhni ifnun sayiz yudhe
sqshu qesqa iluym qkque aqaqm oejjs hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshna
hnmyt isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun siiqa suoij qqfni syyle iszhn
bhmei squih nimnx hsead shqmr udquq uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz
'''

def hackThreeFour():
    # change the comment to decrypt other ciphertext
    #cipherText = 'ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae'
    cipherText = 'iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq iihed yzhni ifnun sayiz yudhe sqshu qesqa iluym qkque aqaqm oejjs hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshn hnmyt isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun siiqa suoij qqfni syyle bhmei squih nimnx hsead shqmr udquq uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz'
    cipherText = re.sub('[^A-Z]','',cipherText.upper()) # remove non-letters then 
    
    alphabetLetters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    maxScore = -99e9
    parentScore,parentKey = maxScore,alphabetLetters[:]
    print('Please wait while decrypting ciphertext.')
    print('Dectypting In-progress...')
    
    # Iterate until decryt ciphertext
    iteration = 0
    complete = False
    preScore = 0
    while complete != True:
        iteration = iteration + 1
        random.shuffle(parentKey) # create random key to begin with
        deciphered = SimpleSubstitution(parentKey).decipher(cipherText) # decryt the cipher with the key
        parentScore = fitness.getScore(deciphered) # get score of the deciphertext; looks up on the frequency analysis of quintgram of English texts.
        count = 0
        while count < 500:
            a = random.randint(0, 25) # generate random index from 0 to 25
            b = random.randint(0, 25) # generate random index from 0 to 25
            child = parentKey[:] # copy parent key
            child[a],child[b] = child[b],child[a] # swap two characters in the copied key
            deciphered = SimpleSubstitution(child).decipher(cipherText) # decrypt the cipher with the new swapped key
            score = fitness.getScore(deciphered) # get new score of the deciphertext
            
            if score > parentScore: # if the new key has better score, replace the parent with it
                parentScore = score
                parentKey = child[:]
                count = 0
            count = count+1
        
        if parentScore > maxScore: # keep track of best key and decrypted text
            maxScore,alphabetLetters = parentScore,parentKey[:]
            simplesub = SimpleSubstitution(alphabetLetters)
            print('\n    Iteration: ', iteration)
            print('\n    Best key: ' + ''.join(alphabetLetters))
            print('\n    plaintext: ' + simplesub.decipher(cipherText))
    
    '''
    Plaintext spaceing inprogress
    
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