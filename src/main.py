from Cube import Cube
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

testcube = Cube()

testcube.scramble(4)

# for i in xrange(0,3):
#     temp = rand.randint(0,54)
#     testcube.move(temp)
#     print('\n' + str(temp) + ' '+moves[temp]+'\n--------')
#     testcube.printCube()

# printMoves()

err_accum = Util.ErrorAccumulator()

# def gp_move(faces,moveType): return testcube.fitness1(testcube.moveTypes(testcube.faces,moveType))
def gp_U(faces): return testcube.fitness1(testcube.moveTypes(faces,0))
def gp_D(faces): return testcube.fitness1(testcube.moveTypes(faces,1))
def gp_L(faces): return testcube.fitness1(testcube.moveTypes(faces,2))
def gp_R(faces): return testcube.fitness1(testcube.moveTypes(faces,3))
def gp_F(faces): return testcube.fitness1(testcube.moveTypes(faces,4))
def gp_B(faces): return testcube.fitness1(testcube.moveTypes(faces,5))
def gp_u(faces): return testcube.fitness1(testcube.moveTypes(faces,6))
def gp_d(faces): return testcube.fitness1(testcube.moveTypes(faces,7))
def gp_l(faces): return testcube.fitness1(testcube.moveTypes(faces,8))
def gp_r(faces): return testcube.fitness1(testcube.moveTypes(faces,9))
def gp_f(faces): return testcube.fitness1(testcube.moveTypes(faces,10))
def gp_b(faces): return testcube.fitness1(testcube.moveTypes(faces,11))
def gp_Uu(faces): return testcube.fitness1(testcube.moveTypes(faces,12))
def gp_Dd(faces): return testcube.fitness1(testcube.moveTypes(faces,13))
def gp_Ll(faces): return testcube.fitness1(testcube.moveTypes(faces,14))
def gp_Rr(faces): return testcube.fitness1(testcube.moveTypes(faces,15))
def gp_Ff(faces): return testcube.fitness1(testcube.moveTypes(faces,16))
def gp_Bb(faces): return testcube.fitness1(testcube.moveTypes(faces,17))
def gp_Ua(faces): return testcube.fitness1(testcube.moveTypes(faces,18))
def gp_Da(faces): return testcube.fitness1(testcube.moveTypes(faces,19))
def gp_La(faces): return testcube.fitness1(testcube.moveTypes(faces,20))
def gp_Ra(faces): return testcube.fitness1(testcube.moveTypes(faces,21))
def gp_Fa(faces): return testcube.fitness1(testcube.moveTypes(faces,22))
def gp_Ba(faces): return testcube.fitness1(testcube.moveTypes(faces,23))
def gp_ua(faces): return testcube.fitness1(testcube.moveTypes(faces,24))
def gp_da(faces): return testcube.fitness1(testcube.moveTypes(faces,25))
def gp_la(faces): return testcube.fitness1(testcube.moveTypes(faces,26))
def gp_ra(faces): return testcube.fitness1(testcube.moveTypes(faces,27))
def gp_fa(faces): return testcube.fitness1(testcube.moveTypes(faces,28))
def gp_ba(faces): return testcube.fitness1(testcube.moveTypes(faces,29))
def gp_Uua(faces): return testcube.fitness1(testcube.moveTypes(faces,30))
def gp_Dda(faces): return testcube.fitness1(testcube.moveTypes(faces,31))
def gp_Lla(faces): return testcube.fitness1(testcube.moveTypes(faces,32))
def gp_Rra(faces): return testcube.fitness1(testcube.moveTypes(faces,33))
def gp_Ffa(faces): return testcube.fitness1(testcube.moveTypes(faces,34))
def gp_Bba(faces): return testcube.fitness1(testcube.moveTypes(faces,35))
def gp_U2(faces): return testcube.fitness1(testcube.moveTypes(faces,36))
def gp_D2(faces): return testcube.fitness1(testcube.moveTypes(faces,37))
def gp_L2(faces): return testcube.fitness1(testcube.moveTypes(faces,38))
def gp_R2(faces): return testcube.fitness1(testcube.moveTypes(faces,39))
def gp_F2(faces): return testcube.fitness1(testcube.moveTypes(faces,40))
def gp_B2(faces): return testcube.fitness1(testcube.moveTypes(faces,41))
def gp_u2(faces): return testcube.fitness1(testcube.moveTypes(faces,42))
def gp_d2(faces): return testcube.fitness1(testcube.moveTypes(faces,43))
def gp_l2(faces): return testcube.fitness1(testcube.moveTypes(faces,44))
def gp_r2(faces): return testcube.fitness1(testcube.moveTypes(faces,45))
def gp_f2(faces): return testcube.fitness1(testcube.moveTypes(faces,46))
def gp_b2(faces): return testcube.fitness1(testcube.moveTypes(faces,47))
def gp_Uu2(faces): return testcube.fitness1(testcube.moveTypes(faces,48))
def gp_Dd2(faces): return testcube.fitness1(testcube.moveTypes(faces,49))
def gp_Ll2(faces): return testcube.fitness1(testcube.moveTypes(faces,50))
def gp_Rr2(faces): return testcube.fitness1(testcube.moveTypes(faces,51))
def gp_Ff2(faces): return testcube.fitness1(testcube.moveTypes(faces,52))
def gp_Bb2(faces): return testcube.fitness1(testcube.moveTypes(faces,53))

def eval_func(chromosome):
    global err_accum
    err_accum.reset()
    code_comp = chromosome.getCompiledCode()

    # faces = np.full([6,4,4], '', dtype=np.str)
    # print(faces)
    # print(faces.shape)
    # np.copyto(faces, testcube.faces)
    # print(faces)
    # print(faces.shape)
    for i in xrange(0,54):
        faces = testcube.faces
        evaluated   = eval(code_comp)
        target      = 96
        err_accum  += (target, evaluated)
        # print(str(target),' ',str(evaluated))

    return err_accum.getRMSE()

def main_run():
    genome = GTree.GTreeGP()
    genome.setParams(max_depth=4, method="ramped")
    genome.evaluator.set(eval_func)

    ga = GSimpleGA.GSimpleGA(genome)
    ga.setParams(gp_terminals       = ['faces'],
                 gp_function_prefix = "gp")

    ga.setMinimax(Consts.minimaxType["minimize"])
    ga.setGenerations(10)
    ga.setCrossoverRate(1.0)
    ga.setMutationRate(0.25)
    ga.setPopulationSize(10)

    ga(freq_stats=10)
    genome.writePopulationDot(ga, "treegraph.png", "png", 0, 10)
    best = ga.bestIndividual()
    best.writeDotImage("besttree.png")
    print best

if __name__ == "__main__":
   main_run()

# Traceback (most recent call last):
#   File ".\main.py", line 145, in <module>
#     main_run()
#   File ".\main.py", line 138, in main_run
#     ga(freq_stats=10)
#   File "C:\Python27\lib\site-packages\pyevolve\GSimpleGA.py", line 281, in __call__
#     return self.evolve(kwargs.get("freq_stats"))
#   File "C:\Python27\lib\site-packages\pyevolve\GSimpleGA.py", line 755, in evolve
#     self.internalPop.evaluate()
#   File "C:\Python27\lib\site-packages\pyevolve\GPopulation.py", line 378, in evaluate
#
#     ind.evaluate(**args)
#   File "C:\Python27\lib\site-packages\pyevolve\GenomeBase.py", line 138, in evaluate
#     for it in self.evaluator.applyFunctions(self, **args):
#   File "C:\Python27\lib\site-packages\pyevolve\FunctionSlot.py", line 180, in applyFunctions
#     yield f(obj, **args)
#   File ".\main.py", line 116, in eval_func
#     evaluated   = eval(code_comp)
#   File "<string>", line 1, in <module>
#   File ".\main.py", line 51, in gp_R
#     def gp_R(faces): return testcube.fitness1(testcube.moveTypes(faces,3))
#   File "D:\School\College\Capstone\rubiks-revenge-py\src\Cube.py", line 58, in moveTypes
#     faces = self.XtoY(faces)
#   File "D:\School\College\Capstone\rubiks-revenge-py\src\Cube.py", line 319, in XtoY
#     faces = self.rotateFace(faces,0,True)
#   File "D:\School\College\Capstone\rubiks-revenge-py\src\Cube.py", line 431, in rotateFace
#     tempFace = np.rot90(faces[face])
# TypeError: 'int' object has no attribute '__getitem__'
