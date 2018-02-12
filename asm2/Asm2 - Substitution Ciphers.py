# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 15:43:08 2018
@author: Il Won Son
CECS 478 Assignment #2 - Substitution Ciphers
"""
'''
#1. fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc
#2. oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr
dnzno jahvi fdiyv xcdzq zoczn zxjiy
#3. ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittk
stqfj cae
#4. iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq iihed yzhni ifnun sayiz yudhe
sqshu qesqa iluym qkque aqaqm oejjs hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshna
hnmyt isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun siiqa suoij qqfni syyle iszhn
bhmei squih nimnx hsead shqmr udquq uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz
'''
import numpy
import crypto
def subcipher():
    # Calculate the frequency distribution of the letters in the cipher text.
    # This consists of counting how many times each letter appears.
    # Natural english tetxt has a very distinct distribution that can be used help crack codes.
    
    cipher = 'fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc'
    
    ss = SimpleSubstitution('phqgiumeaylnofdxjkrcvstzwb')
    ss.encipher('defend the east wall of the castle')
    
    ss.decipher('GIUIFGCEIIPRCTPNNDUCEIQPRCNI')