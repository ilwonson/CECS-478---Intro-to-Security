# -*- coding: utf-8 -*-
"""
CECS 478 Assignment #4 - Malware.
@author: Il Won Son

This program modifies "SAVED.GAM" file from Ultima 5 (Dos Game).
Specifically game character's stat and item attricutes:
    Str to 99
    Dex to 99
    Int to 99
    Magic to 99
    HP to 999
    Max HP to 999
    Exp to 9999
    Level to 99
    Food to 9999
    Gold to 9999
    Keys to 99
    Gems to 99
    Torches to 99

Can change the file to its original stats with changing dictionary variable with commenting.
"""

def hack():
    sixtythree = b'\x63'
    eseven = b'\xe7'
    zerothree = b'\x03'
    zerof = b'\x0f'
    twentyseven = b'\x27'
    #---------------------#
    fourteen = b'\x14'
    twelve = b'\x12'
    seventeen = b'\x17'
    threec = b'\x3c'
    doublezero = b'\x00'
    nintysix = b'\x96'
    zerotwo = b'\x02'
    threef = b'\x3f'
    zerofour = b'\x04'
    
    #To reverse the hacked files to its original form use this dictionary.
    #dictionary = {fourteen:[0x0e,], twelve:[0x0f,], seventeen:[0x10, 0x11, ], threec:[0x12, 0x14], doublezero:[0x13, 0x15, 0x203, 0x205, 0x207], nintysix:[0x16, 0x204], zerotwo:[0x18, 0x206], threef:[0x202], zerofour:[0x208]}
    
    #To modify the stats from the SAVED.GAM file use this dictionary.
    dictionary = {sixtythree:[0x0e, 0x0f, 0x10, 0x11, 0x18, 0x206, 0x207, 0x208], eseven:[0x12, 0x14], zerothree:[ 0x13, 0x15], zerof:[ 0x16, 0x202, 0x204,], twentyseven:[0x17, 0x203, 0x205]}
    
    with open('SAVED.GAM', 'r+b') as f:
        for value, offset in dictionary.items():
            for i in range(len(offset)):
                f.seek(offset[i])
                f.write(value)
    
    print('File successfully modified.')