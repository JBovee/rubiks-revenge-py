from Cube import Cube
from move import *
import numpy as np
import random as rand
from pyevolve import Util
from pyevolve import GTree
from pyevolve import GSimpleGA
from pyevolve import Consts
import math

'''
0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17
U    D    L    R    F    B    u    d    l    r    f    b    Uu   Dd   Ll   Rr   Ff   Bb

18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35
U'   D'   L'   R'   F'   B'   u'   d'   l'   r'   f'   b'   Uu'  Dd'  Ll'  Rr'  Ff'  Bb'

36   37   38   39   40   41   42   43   44   45   46   47   48   49   50   51   52   53
U2   D2   L2   R2   F2   B2   u2   d2   l2   r2   f2   b2   Uu2  Dd2  Ll2  Rr2  Ff2  Bb2
'''

moves = np.array(['U','D','L','R','F','B','u','d','l','r','f','b','Uu','Dd','Ll','Rr','Ff','Bb','U\'','D\'','L\'','R\'','F\'','B\'','u\'','d\'','l\'','r\'','f\'','b\'','Uu\'','Dd\'','Ll\'','Rr\'','Ff\'','Bb\'','U2','D2','L2','R2','F2','B2','u2','d2','l2','r2','f2','b2','Uu2','Dd2','Ll2','Rr2','Ff2','Bb2'])

def printMoves():
    print(''.join(['{:5}'.format(str(num)) for num in xrange(0,18)]))
    print(''.join(['{:5}'.format(moves[num]) for num in xrange(0,18)]))
    print
    print(''.join(['{:5}'.format(str(num)) for num in xrange(18,36)]))
    print(''.join(['{:5}'.format(moves[num]) for num in xrange(18,36)]))
    print
    print(''.join(['{:5}'.format(str(num)) for num in xrange(36,54)]))
    print(''.join(['{:5}'.format(moves[num]) for num in xrange(36,54)]))

err_accum = Util.ErrorAccumulator()

def fitness1(faces):
    goalFaces = ['w','r','y','o','b','g']
    faceTotals = [sum([faces[x][y].tolist().count(goalFaces[x]) for y in range(0,4)]) for x in range(0,6)]
    return sum(faceTotals)

# def gp_move(faces,moveType): return testcube.fitness1(testcube.moveTypes(testcube.faces,moveType))
def gp_U(faces): return moveTypes(faces,0)
def gp_D(faces): return moveTypes(faces,1)
def gp_L(faces): return moveTypes(faces,2)
def gp_R(faces): return moveTypes(faces,3)
def gp_F(faces): return moveTypes(faces,4)
def gp_B(faces): return moveTypes(faces,5)
def gp_u(faces): return moveTypes(faces,6)
def gp_d(faces): return moveTypes(faces,7)
def gp_l(faces): return moveTypes(faces,8)
def gp_r(faces): return moveTypes(faces,9)
def gp_f(faces): return moveTypes(faces,10)
def gp_b(faces): return moveTypes(faces,11)
def gp_Uu(faces): return moveTypes(faces,12)
def gp_Dd(faces): return moveTypes(faces,13)
def gp_Ll(faces): return moveTypes(faces,14)
def gp_Rr(faces): return moveTypes(faces,15)
def gp_Ff(faces): return moveTypes(faces,16)
def gp_Bb(faces): return moveTypes(faces,17)
def gp_Ua(faces): return moveTypes(faces,18)
def gp_Da(faces): return moveTypes(faces,19)
def gp_La(faces): return moveTypes(faces,20)
def gp_Ra(faces): return moveTypes(faces,21)
def gp_Fa(faces): return moveTypes(faces,22)
def gp_Ba(faces): return moveTypes(faces,23)
def gp_ua(faces): return moveTypes(faces,24)
def gp_da(faces): return moveTypes(faces,25)
def gp_la(faces): return moveTypes(faces,26)
def gp_ra(faces): return moveTypes(faces,27)
def gp_fa(faces): return moveTypes(faces,28)
def gp_ba(faces): return moveTypes(faces,29)
def gp_Uua(faces): return moveTypes(faces,30)
def gp_Dda(faces): return moveTypes(faces,31)
def gp_Lla(faces): return moveTypes(faces,32)
def gp_Rra(faces): return moveTypes(faces,33)
def gp_Ffa(faces): return moveTypes(faces,34)
def gp_Bba(faces): return moveTypes(faces,35)
def gp_U2(faces): return moveTypes(faces,36)
def gp_D2(faces): return moveTypes(faces,37)
def gp_L2(faces): return moveTypes(faces,38)
def gp_R2(faces): return moveTypes(faces,39)
def gp_F2(faces): return moveTypes(faces,40)
def gp_B2(faces): return moveTypes(faces,41)
def gp_u2(faces): return moveTypes(faces,42)
def gp_d2(faces): return moveTypes(faces,43)
def gp_l2(faces): return moveTypes(faces,44)
def gp_r2(faces): return moveTypes(faces,45)
def gp_f2(faces): return moveTypes(faces,46)
def gp_b2(faces): return moveTypes(faces,47)
def gp_Uu2(faces): return moveTypes(faces,48)
def gp_Dd2(faces): return moveTypes(faces,49)
def gp_Ll2(faces): return moveTypes(faces,50)
def gp_Rr2(faces): return moveTypes(faces,51)
def gp_Ff2(faces): return moveTypes(faces,52)
def gp_Bb2(faces): return moveTypes(faces,53)

def eval_func(chromosome):
    global err_accum
    err_accum.reset()
    code_comp = chromosome.getCompiledCode()

    evaluated   = eval(code_comp)
    target      = cleanfaces
    err_accum  += (fitness1(target), fitness1(evaluated))

    return err_accum.getRMSE()

def main_run():
    global faces
    global cleanfaces
    testcube = Cube()
    cube2 = Cube()
    cleancube = Cube()
    cleanfaces = cleancube.getFaces()

    testcube.move(3)
    cube2.setFaces(testcube.getFaces())
    faces = testcube.getFaces()
    testcube.printCube()

    genome = GTree.GTreeGP()
    genome.setParams(max_depth=8, method="ramped")
    genome.evaluator.set(eval_func)

    ga = GSimpleGA.GSimpleGA(genome)
    ga.setParams(gp_terminals       = ['faces'],
                 gp_function_prefix = "gp")

    ga.setMinimax(Consts.minimaxType["minimize"])
    ga.setGenerations(10)
    ga.setCrossoverRate(1.0)
    ga.setMutationRate(0.25)
    ga.setPopulationSize(50)

    ga(freq_stats=10)
    best = ga.bestIndividual()
    print best
    print best
    testcube.printCube()
    cleancube.printCube()
    cube2.printCube()

if __name__ == "__main__":
   main_run()
