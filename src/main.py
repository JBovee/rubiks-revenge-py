from Cube import Cube
from move import *
from collections import Counter
import sys
import numpy as np
import random as rand
import operator as op
from functools import partial
from deap import algorithms, creator, base, tools, gp
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

def fitness1(faces):
    goalFaces = ['w','r','y','o','b','g']
    faceTotals = [sum([faces[x][y].tolist().count(goalFaces[x]) for y in range(0,4)]) for x in range(0,6)]
    return sum(faceTotals)

def fitness2(faces):
    return np.sum([Counter(x for face in faces[y].tolist() for x in face).most_common(1)[0][1] for y in range(0,6)])

def fitness3(faces):
    centerOptions = ['w','r','y','o','b','g']
    centers = faces[:,1:3,1:3]
    tempCent = np.full([6,4], '', dtype=np.str)
    faceColors = np.full([6], '', dtype=np.str)
    for i in range(0,6):
        np.copyto(tempCent[i], np.hstack((centers[i][0],centers[i][1])))
    tempCentL = tempCent.tolist()
    dicts = [{'w': row.count('w'), 'r': row.count('r'), 'y': row.count('y'), 'o': row.count('o'), 'b': row.count('b'), 'g': row.count('g')} for row in tempCentL]
    sorted_dicts = [sorted(el.items(), key=op.itemgetter(1), reverse=True) for el in dicts]
    has_space = True
    while has_space:
        for i in range(0,6):
            if sorted_dicts[i][0][1] == 3 or sorted_dicts[i][0][1] == 4:
                faceColors[i] = sorted_dicts[i][0][0]
        for i in range(0,6):
            if sorted_dicts[i][0][1] == 2 and sorted_dicts[i][1][1] == 1:
                rand_pos = rand.randint(0,3)
                if sorted_dicts[i][rand_pos%3][0] not in faceColors:
                    faceColors[i] = sorted_dicts[i][rand_pos%3][0]
            elif sorted_dicts[i][0][1] == 2 and sorted_dicts[i][1][1] == 2:
                rand_pos = rand.randint(0,1)
                if sorted_dicts[i][rand_pos][0] not in faceColors:
                    faceColors[i] = sorted_dicts[i][rand_pos][0]
            elif sorted_dicts[i][0][1] == 1 and sorted_dicts[i][1][1] == 1:
                rand_pos = rand.randint(0,3)
                if sorted_dicts[i][rand_pos][0] not in faceColors:
                    faceColors[i] = sorted_dicts[i][rand_pos][0]
        has_space = '' in faceColors
    faceTotals = [sum([faces[x][y].tolist().count(faceColors[x]) for y in range(0,4)]) for x in range(0,6)]
    return sum(faceTotals)

def fitness4(faces,moveCount):
    return float("{0:.2f}".format(np.average([Counter(x for face in faces[y].tolist() for x in face).most_common(1)[0][1] for y in range(0,6)]) - np.sqrt(moveCount)))

def fitness5(faces,moveCount):
    goalFaces = ['w','r','y','o','b','g']
    faceTotals = [sum([faces[x][y].tolist().count(goalFaces[x]) for y in range(0,4)]) for x in range(0,6)]
    return sum(faceTotals)-moveCount

def progn(*args):
    for arg in args:
        arg()

def prog2(out1, out2):
    return partial(progn, out1, out2)

def prog3(out1, out2, out3):
    return partial(progn, out1, out2, out3)

def prog4(out1, out2, out3, out4):
    return partial(progn, out1, out2, out3, out4)

def prog5(out1, out2, out3, out4, out5):
    return partial(progn, out1, out2, out3, out4, out5)

def prog6(out1, out2, out3, out4, out5, out6):
    return partial(progn, out1, out2, out3, out4, out5, out6)

def prog7(out1, out2, out3, out4, out5, out6, out7):
    return partial(progn, out1, out2, out3, out4, out5, out6, out7)

def prog8(out1, out2, out3, out4, out5, out6, out7, out8):
    return partial(progn, out1, out2, out3, out4, out5, out6, out7, out8)

def prog9(out1, out2, out3, out4, out5, out6, out7, out8, out9):
    return partial(progn, out1, out2, out3, out4, out5, out6, out7, out8, out9)

def prog10(out1, out2, out3, out4, out5, out6, out7, out8, out9, out10):
    return partial(progn, out1, out2, out3, out4, out5, out6, out7, out8, out9, out10)

def prog11(out1, out2, out3, out4, out5, out6, out7, out8, out9, out10, out11):
    return partial(progn, out1, out2, out3, out4, out5, out6, out7, out8, out9, out10, out11)

def prog12(out1, out2, out3, out4, out5, out6, out7, out8, out9, out10, out11, out12):
    return partial(progn, out1, out2, out3, out4, out5, out6, out7, out8, out9, out10, out11, out12)

def loopn(n, arg):
    for i in xrange(n):
        arg()

def loop2(arg):
    return partial(loopn, 2, arg)

def loop3(arg):
    return partial(loopn, 3, arg)

def loop4(arg):
    return partial(loopn, 4, arg)

def loop5(arg):
    return partial(loopn, 5, arg)

def loop6(arg):
    return partial(loopn, 6, arg)

#def if_then_else(condition, out1, out2):
#    out1() if condition() else out2()
#
#def if_0_red_gt4(testcube, out1, out2):
#    return partial(if_then_else, sum([testcube.self.faces[0][y].tolist().count('r') for y in range(0,4)]) > 4, out1, out2)

testcube = Cube()
testcube.setFitFunc(sys.argv[4])

pset = gp.PrimitiveSet("MAIN", 0)
pset.addPrimitive(prog2, 2)
pset.addPrimitive(prog3, 3)
pset.addPrimitive(prog4, 4)
pset.addPrimitive(prog5, 5)
pset.addPrimitive(prog6, 6)
pset.addPrimitive(prog7, 7)
pset.addPrimitive(prog8, 8)
pset.addPrimitive(prog9, 9)
pset.addPrimitive(prog10, 10)
pset.addPrimitive(prog11, 11)
pset.addPrimitive(prog12, 12)
pset.addPrimitive(loop2, 1)
pset.addPrimitive(loop3, 1)
#pset.addPrimitive(loop4, 1)
#pset.addPrimitive(loop5, 1)
#pset.addPrimitive(loop6, 1)
pset.addPrimitive(testcube.if_better, 2)
pset.addPrimitive(testcube.if_w_0, 2)
pset.addPrimitive(testcube.if_w_1, 2)
pset.addPrimitive(testcube.if_w_2, 2)
pset.addPrimitive(testcube.if_w_3, 2)
pset.addPrimitive(testcube.if_w_4, 2)
pset.addPrimitive(testcube.if_w_5, 2)
pset.addPrimitive(testcube.if_r_0, 2)
pset.addPrimitive(testcube.if_r_1, 2)
pset.addPrimitive(testcube.if_r_2, 2)
pset.addPrimitive(testcube.if_r_3, 2)
pset.addPrimitive(testcube.if_r_4, 2)
pset.addPrimitive(testcube.if_r_5, 2)
pset.addPrimitive(testcube.if_o_0, 2)
pset.addPrimitive(testcube.if_o_1, 2)
pset.addPrimitive(testcube.if_o_2, 2)
pset.addPrimitive(testcube.if_o_3, 2)
pset.addPrimitive(testcube.if_o_4, 2)
pset.addPrimitive(testcube.if_o_5, 2)
pset.addPrimitive(testcube.if_y_0, 2)
pset.addPrimitive(testcube.if_y_1, 2)
pset.addPrimitive(testcube.if_y_2, 2)
pset.addPrimitive(testcube.if_y_3, 2)
pset.addPrimitive(testcube.if_y_4, 2)
pset.addPrimitive(testcube.if_y_5, 2)
pset.addPrimitive(testcube.if_b_0, 2)
pset.addPrimitive(testcube.if_b_1, 2)
pset.addPrimitive(testcube.if_b_2, 2)
pset.addPrimitive(testcube.if_b_3, 2)
pset.addPrimitive(testcube.if_b_4, 2)
pset.addPrimitive(testcube.if_b_5, 2)
pset.addPrimitive(testcube.if_g_0, 2)
pset.addPrimitive(testcube.if_g_1, 2)
pset.addPrimitive(testcube.if_g_2, 2)
pset.addPrimitive(testcube.if_g_3, 2)
pset.addPrimitive(testcube.if_g_4, 2)
pset.addPrimitive(testcube.if_g_5, 2)
pset.addTerminal(testcube.move_U)
pset.addTerminal(testcube.move_D)
pset.addTerminal(testcube.move_L)
pset.addTerminal(testcube.move_R)
pset.addTerminal(testcube.move_F)
pset.addTerminal(testcube.move_B)
pset.addTerminal(testcube.move_u)
pset.addTerminal(testcube.move_d)
pset.addTerminal(testcube.move_l)
pset.addTerminal(testcube.move_r)
pset.addTerminal(testcube.move_f)
pset.addTerminal(testcube.move_b)
pset.addTerminal(testcube.move_Uu)
pset.addTerminal(testcube.move_Dd)
pset.addTerminal(testcube.move_Ll)
pset.addTerminal(testcube.move_Rr)
pset.addTerminal(testcube.move_Ff)
pset.addTerminal(testcube.move_Bb)
pset.addTerminal(testcube.move_Ua)
pset.addTerminal(testcube.move_Da)
pset.addTerminal(testcube.move_La)
pset.addTerminal(testcube.move_Ra)
pset.addTerminal(testcube.move_Fa)
pset.addTerminal(testcube.move_Ba)
pset.addTerminal(testcube.move_ua)
pset.addTerminal(testcube.move_da)
pset.addTerminal(testcube.move_la)
pset.addTerminal(testcube.move_ra)
pset.addTerminal(testcube.move_fa)
pset.addTerminal(testcube.move_ba)
pset.addTerminal(testcube.move_Uua)
pset.addTerminal(testcube.move_Dda)
pset.addTerminal(testcube.move_Lla)
pset.addTerminal(testcube.move_Rra)
pset.addTerminal(testcube.move_Ffa)
pset.addTerminal(testcube.move_Bba)
pset.addTerminal(testcube.move_U2)
pset.addTerminal(testcube.move_D2)
pset.addTerminal(testcube.move_L2)
pset.addTerminal(testcube.move_R2)
pset.addTerminal(testcube.move_F2)
pset.addTerminal(testcube.move_B2)
pset.addTerminal(testcube.move_u2)
pset.addTerminal(testcube.move_d2)
pset.addTerminal(testcube.move_l2)
pset.addTerminal(testcube.move_r2)
pset.addTerminal(testcube.move_f2)
pset.addTerminal(testcube.move_b2)
pset.addTerminal(testcube.move_Uu2)
pset.addTerminal(testcube.move_Dd2)
pset.addTerminal(testcube.move_Ll2)
pset.addTerminal(testcube.move_Rr2)
pset.addTerminal(testcube.move_Ff2)
pset.addTerminal(testcube.move_Bb2)

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("expr_init", gp.genFull, pset=pset, min_=1, max_=2)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr_init)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalCube(individual):
    #print(individual)
    moves = gp.compile(individual, pset)
    testcube.run(moves)
    fit = testcube.fitness()
    #print("fit:"+str(fit)+'\n')
    return fit,

toolbox.register("evaluate", evalCube)
#toolbox.register("select", tools.selTournament, tournsize=7)
toolbox.register("select", tools.selDoubleTournament, fitness_size=7, parsimony_size=1.4, fitness_first=False)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

def main():
    #testcube.scramble(15)
    testcube.move_R()
    testcube.move_U2()
    testcube.move_Ra()
    testcube.move_D()
    testcube.move_b2()
    testcube.move_Ra()
    testcube.move_D()
    testcube.move_R2()
    testcube.move_b()
    testcube.move_u()
    testcube.move_Bb2()
    testcube.move_U2()
    testcube.move_Ll2()
    testcube.move_d2()
    testcube.move_u2()
    #print(fitness1(testcube.getFaces()))
    #testcube.printCube()
    testcube._store()
    testcube._restore()

    pop = toolbox.population(n=80)
    hof=tools.HallOfFame(2)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    gen = int(sys.argv[1])
    cxpb = float(sys.argv[2])
    mutpb = float(sys.argv[3])

    print("CXPB = "+str(cxpb)+"  MUTPB = "+str(mutpb)+"  GEN = "+str(gen))

    algorithms.eaSimple(pop, toolbox, cxpb, mutpb, gen, stats, halloffame=hof, verbose=False)

    print(hof[0])
    print(hof[0].fitness)
    print(hof[1])
    print(hof[1].fitness)
    bestMoves = gp.compile(hof[0],pset)
    testcube.run(bestMoves)
    #testcube.printCube()
    print

    return pop, stats, hof

if __name__ == "__main__":
   main()
