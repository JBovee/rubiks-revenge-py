from Cube import Cube
from pyevolve import Util
from pyevolve import GTree
from pyevolve import GSimpleGA
from pyevolve import Consts
import math
import numpy as np
'''
    0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35
T   U   D   L   R   F   B   u   d   l   r   f   b   Uu  Dd  Ll  Rr  Ff  Bb  U2  D2  L2  R2  F2  B2  u2  d2  l2  r2  f2  b2  Uu2 Dd2 Ll2 Rr2 Ff2 Bb2
F   U'  D'  L'  R'  F'  B'  u'  d'  l'  r'  f'  b'  Uu' Dd' Ll' Rr' Ff' Bb'
'''

# error_accum = Util.ErrorAccumulator()

def printMoves():
    movnum = np.array([" ","0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35"])
    mov = np.array(["T","U","D","L","R","F","B","u","d","l","r","f","b","Uu","Dd","Ll","Rr","Ff","Bb","U2","D2","L2","R2","F2","B2","u2","d2","l2","r2","f2","b2","Uu2","Dd2","Ll2","Rr2","Ff2","Bb2"])
    movA = np.array(["F","U'","D'","L'","R'","F'","B'","u'","d'","l'","r'","f'","b'","Uu'","Dd'","Ll'","Rr'","Ff'","Bb'"])
    print(''.join(['{:4}'.format(item) for item in movnum]))
    print(''.join(['{:4}'.format(item) for item in mov]))
    print(''.join(['{:4}'.format(item) for item in movA]))

testcube = Cube()

for i in range(0,10):
    testcube.scramble(20)
    testcube.fitness2()
