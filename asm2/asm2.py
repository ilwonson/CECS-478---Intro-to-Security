#from itertools import zip_longest

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = LETTERS + LETTERS.lower() + ' \t\n'

def hack():
    
    '''
    #1. fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc
    #2. oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy
    #3. ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae
    #4. iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq iihed yzhni ifnun sayiz yudhe
    sqshu qesqa iluym qkque aqaqm oejjs hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshna
    hnmyt isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun siiqa suoij qqfni syyle iszhn
    bhmei squih nimnx hsead shqmr udquq uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz
    '''
    
    ciphertext = 'fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc'
    #ciphertext = 'oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy'
    
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
    
    #----------------------------------------
    result = 0
    for k in range(len(listOfDeciphertext)):
        text = ''.join(listOfDeciphertext[k].split())
        #print(text)
        candidates = []
        for n in range(8):
            i, j = 0, n 
            for x in range(len(text)):
                temp = text[i:j]
                if temp in ENGLISH_WORDS:
                    candidates.append(temp)
                i += 1
                j += 1
        #print(candidates, len(candidates))
        if len(candidates) > 15:
            result = k
    if result > 0:
        print('\nCiphertext: ' + ciphertext)
        print(' Plaintext: ' + listOfDeciphertext[result])
        print('       Key: %d' % (result))
    else:
        print('Sorry, could not decrypt the text.')
    
    
    '''
    for word in listtemp:
        if word in ENGLISH_WORDS:
            candidates.append(word)
    '''
    
    
    '''#spaces
    for x in range(len(frontspace)):
        print(frontspace[x],backspace[x])
        text = text[:space[x]] + ' ' + text[space[x]:]
    print(text)
    '''
    '''
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

