from Cube import Cube
import numpy as np
'''
    0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17
T   U   D   L   R   F   B   u   d   l   r   f   b   Uu  Dd  Ll  Rr  Ff  Bb
F   U'  D'  L'  R'  F'  B'  u'  d'  l'  r'  f'  b'  Uu' Dd' Ll' Rr' Ff' Bb'
'''

def printMoves():
    movnum = np.array([" ","0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17"])
    mov = np.array(["T","U","D","L","R","F","B","u","d","l","r","f","b","Uu","Dd","Ll","Rr","Ff","Bb"])
    movA = np.array(["F","U'","D'","L'","R'","F'","B'","u'","d'","l'","r'","f'","b'","Uu'","Dd'","Ll'","Rr'","Ff'","Bb'"])
    print(''.join(['{:4}'.format(item) for item in movnum]))
    print(''.join(['{:4}'.format(item) for item in mov]))
    print(''.join(['{:4}'.format(item) for item in movA]))

testcube = Cube()

testcube.printCube()

testcube.scramble(10)

print()

testcube.printCube()
