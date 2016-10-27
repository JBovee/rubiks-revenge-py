from __future__ import print_function
import numpy as np
import random as rand
import operator as op
from functools import partial

def if_then_else(condition, out1, out2):
    out1() if condition else out2()

facesum = 8

class Cube(object):

    def __init__(self):
        self.faces = np.array([[['w','w','w','w'],
                                ['w','w','w','w'],
                                ['w','w','w','w'],
                                ['w','w','w','w']],
                                [['r','r','r','r'],
                                ['r','r','r','r'],
                                ['r','r','r','r'],
                                ['r','r','r','r']],
                                [['y','y','y','y'],
                                ['y','y','y','y'],
                                ['y','y','y','y'],
                                ['y','y','y','y']],
                                [['o','o','o','o'],
                                ['o','o','o','o'],
                                ['o','o','o','o'],
                                ['o','o','o','o']],
                                [['b','b','b','b'],
                                ['b','b','b','b'],
                                ['b','b','b','b'],
                                ['b','b','b','b']],
                                [['g','g','g','g'],
                                ['g','g','g','g'],
                                ['g','g','g','g'],
                                ['g','g','g','g']]])

        self.storedfaces = np.full([6,4,4], '', dtype=np.str)

        self.temp = np.full([6,4,4], '', dtype=np.str)

        self.moves = np.array(['U','D','L','R','F','B','u','d','l','r','f','b','Uu','Dd','Ll','Rr','Ff','Bb','Ua','Da','La','Ra','Fa','Ba','ua','da','la','ra','fa','ba','Uua','Dda','Lla','Rra','Ffa','Bba','U2','D2','L2','R2','F2','B2','u2','d2','l2','r2','f2','b2','Uu2','Dd2','Ll2','Rr2','Ff2','Bb2'])

        self.functions = [self.move_U, self.move_D,
                          self.move_L, self.move_R,
                          self.move_F, self.move_B,
                          self.move_u, self.move_d,
                          self.move_l, self.move_r,
                          self.move_f, self.move_b,
                          self.move_Uu, self.move_Dd,
                          self.move_Ll, self.move_Rr,
                          self.move_Ff, self.move_Bb,
                          self.move_Ua, self.move_Da,
                          self.move_La, self.move_Ra,
                          self.move_Fa, self.move_Ba,
                          self.move_ua, self.move_da,
                          self.move_la, self.move_ra,
                          self.move_fa, self.move_ba,
                          self.move_Uua, self.move_Dda,
                          self.move_Lla, self.move_Rra,
                          self.move_Ffa, self.move_Bba,
                          self.move_U2, self.move_D2,
                          self.move_L2, self.move_R2,
                          self.move_F2, self.move_B2,
                          self.move_u2, self.move_d2,
                          self.move_l2, self.move_r2,
                          self.move_f2, self.move_b2,
                          self.move_Uu2, self.move_Dd2,
                          self.move_Ll2, self.move_Rr2,
                          self.move_Ff2, self.move_Bb2]

    def _reset(self):
        self.faces = np.array([[['w','w','w','w'],
                                ['w','w','w','w'],
                                ['w','w','w','w'],
                                ['w','w','w','w']],
                                [['r','r','r','r'],
                                ['r','r','r','r'],
                                ['r','r','r','r'],
                                ['r','r','r','r']],
                                [['y','y','y','y'],
                                ['y','y','y','y'],
                                ['y','y','y','y'],
                                ['y','y','y','y']],
                                [['o','o','o','o'],
                                ['o','o','o','o'],
                                ['o','o','o','o'],
                                ['o','o','o','o']],
                                [['b','b','b','b'],
                                ['b','b','b','b'],
                                ['b','b','b','b'],
                                ['b','b','b','b']],
                                [['g','g','g','g'],
                                ['g','g','g','g'],
                                ['g','g','g','g'],
                                ['g','g','g','g']]])

    def _store(self):
        np.copyto(self.storedfaces, self.faces)

    def _restore(self):
        np.copyto(self.faces,self.storedfaces)

    def printCube(self):
        print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in self.faces[4]]))
	print('-  -  -  -')
        for y in range(0,4):
	    for x in range(0,4):
		print(''.join(['{:3}'.format(self.faces[x][y][z]) for z in range(0,3)])+self.faces[x][y][3]+' | ',end="")
	    print()
	print('-  -  -  -')
        print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in self.faces[5]]))
	print()

    def getFaces(self):
        np.copyto(self.temp, self.faces)
        return self.temp

    def setFaces(self,faces):
        np.copyto(self.faces, faces)

    def scramble(self,n):
        for i in range(0,n):
            func = rand.choice(self.functions)
            print(func)
            func()

    def run(self,moves):
        self._restore()
        moves()

    def sum_w(self,face):
        return sum([self.faces[face][y].tolist().count('w') for y in range(0,4)]) > facesum

    def if_w_0(self, out1, out2):
        return partial(if_then_else, self.sum_w(0), out1, out2)

    def if_w_1(self, out1, out2):
        return partial(if_then_else, self.sum_w(1), out1, out2)

    def if_w_2(self, out1, out2):
        return partial(if_then_else, self.sum_w(2), out1, out2)

    def if_w_3(self, out1, out2):
        return partial(if_then_else, self.sum_w(3), out1, out2)

    def if_w_4(self, out1, out2):
        return partial(if_then_else, self.sum_w(4), out1, out2)

    def if_w_5(self, out1, out2):
        return partial(if_then_else, self.sum_w(5), out1, out2)

    def sum_r(self,face):
        return sum([self.faces[face][y].tolist().count('r') for y in range(0,4)]) > facesum

    def if_r_0(self, out1, out2):
        return partial(if_then_else, self.sum_r(0), out1, out2)

    def if_r_1(self, out1, out2):
        return partial(if_then_else, self.sum_r(1), out1, out2)

    def if_r_2(self, out1, out2):
        return partial(if_then_else, self.sum_r(2), out1, out2)

    def if_r_3(self, out1, out2):
        return partial(if_then_else, self.sum_r(3), out1, out2)

    def if_r_4(self, out1, out2):
        return partial(if_then_else, self.sum_r(4), out1, out2)

    def if_r_5(self, out1, out2):
        return partial(if_then_else, self.sum_r(5), out1, out2)

    def sum_y(self,face):
        return sum([self.faces[face][y].tolist().count('y') for y in range(0,4)]) > facesum

    def if_y_0(self, out1, out2):
        return partial(if_then_else, self.sum_y(0), out1, out2)

    def if_y_1(self, out1, out2):
        return partial(if_then_else, self.sum_y(1), out1, out2)

    def if_y_2(self, out1, out2):
        return partial(if_then_else, self.sum_y(2), out1, out2)

    def if_y_3(self, out1, out2):
        return partial(if_then_else, self.sum_y(3), out1, out2)

    def if_y_4(self, out1, out2):
        return partial(if_then_else, self.sum_y(4), out1, out2)

    def if_y_5(self, out1, out2):
        return partial(if_then_else, self.sum_y(5), out1, out2)

    def sum_o(self,face):
        return sum([self.faces[face][y].tolist().count('o') for y in range(0,4)]) > facesum

    def if_o_0(self, out1, out2):
        return partial(if_then_else, self.sum_o(0), out1, out2)

    def if_o_1(self, out1, out2):
        return partial(if_then_else, self.sum_o(1), out1, out2)

    def if_o_2(self, out1, out2):
        return partial(if_then_else, self.sum_o(2), out1, out2)

    def if_o_3(self, out1, out2):
        return partial(if_then_else, self.sum_o(3), out1, out2)

    def if_o_4(self, out1, out2):
        return partial(if_then_else, self.sum_o(4), out1, out2)

    def if_o_5(self, out1, out2):
        return partial(if_then_else, self.sum_o(5), out1, out2)

    def sum_b(self,face):
        return sum([self.faces[face][y].tolist().count('b') for y in range(0,4)]) > facesum

    def if_b_0(self, out1, out2):
        return partial(if_then_else, self.sum_b(0), out1, out2)

    def if_b_1(self, out1, out2):
        return partial(if_then_else, self.sum_b(1), out1, out2)

    def if_b_2(self, out1, out2):
        return partial(if_then_else, self.sum_b(2), out1, out2)

    def if_b_3(self, out1, out2):
        return partial(if_then_else, self.sum_b(3), out1, out2)

    def if_b_4(self, out1, out2):
        return partial(if_then_else, self.sum_b(4), out1, out2)

    def if_b_5(self, out1, out2):
        return partial(if_then_else, self.sum_b(5), out1, out2)

    def sum_g(self,face):
        return sum([self.faces[face][y].tolist().count('g') for y in range(0,4)]) > facesum

    def if_g_0(self, out1, out2):
        return partial(if_then_else, self.sum_g(0), out1, out2)

    def if_g_1(self, out1, out2):
        return partial(if_then_else, self.sum_g(1), out1, out2)

    def if_g_2(self, out1, out2):
        return partial(if_then_else, self.sum_g(2), out1, out2)

    def if_g_3(self, out1, out2):
        return partial(if_then_else, self.sum_g(3), out1, out2)

    def if_g_4(self, out1, out2):
        return partial(if_then_else, self.sum_g(4), out1, out2)

    def if_g_5(self, out1, out2):
        return partial(if_then_else, self.sum_g(5), out1, out2)

    def move_U(self):
        tempFaces = self.faces
        tempFaces = self.xRegTurn(tempFaces,0)
        tempFaces = self.rotateFace(tempFaces,4,True)
        self.faces = tempFaces

    def move_D(self):
        tempFaces = self.faces
        tempFaces = self.xAntiTurn(tempFaces,3)
        tempFaces = self.rotateFace(tempFaces,5,True)
        self.faces = tempFaces

    def move_L(self):
        tempFaces = self.faces
        tempFaces = self.XtoY(tempFaces)
        tempFaces = self.xRegTurn(tempFaces,0)
        tempFaces = self.rotateFace(tempFaces,4,True)
        tempFaces = self.YtoX(tempFaces)
        self.faces = tempFaces

    def move_R(self):
        tempFaces = self.faces
        tempFaces = self.XtoY(tempFaces)
        tempFaces = self.xAntiTurn(tempFaces,3)
        tempFaces = self.rotateFace(tempFaces,5,True)
        tempFaces = self.YtoX(tempFaces)
        self.faces = tempFaces

    def move_F(self):
        tempFaces = self.faces
        tempFaces = self.XtoZ(tempFaces)
        tempFaces = self.xRegTurn(tempFaces,0)
        tempFaces = self.rotateFace(tempFaces,4,True)
        tempFaces = self.ZtoX(tempFaces)
        self.faces = tempFaces

    def move_B(self):
        tempFaces = self.faces
        tempFaces = self.XtoZ(tempFaces)
        tempFaces = self.xAntiTurn(tempFaces,3)
        tempFaces = self.rotateFace(tempFaces,5,True)
        tempFaces = self.ZtoX(tempFaces)
        self.faces = tempFaces

    def move_u(self):
        tempFaces = self.faces
        tempFaces = self.xRegTurn(tempFaces,1)
        self.faces = tempFaces

    def move_d(self):
        tempFaces = self.faces
        tempFaces = self.xAntiTurn(tempFaces,2)
        self.faces = tempFaces

    def move_l(self):
        tempFaces = self.faces
        tempFaces = self.XtoY(tempFaces)
        tempFaces = self.xRegTurn(tempFaces,1)
        tempFaces = self.YtoX(tempFaces)
        self.faces = tempFaces

    def move_r(self):
        tempFaces = self.faces
        tempFaces = self.XtoY(tempFaces)
        tempFaces = self.xAntiTurn(tempFaces,2)
        tempFaces = self.YtoX(tempFaces)
        self.faces = tempFaces

    def move_f(self):
        tempFaces = self.faces
        tempFaces = self.XtoZ(tempFaces)
        tempFaces = self.xRegTurn(tempFaces,1)
        tempFaces = self.ZtoX(tempFaces)
        self.faces = tempFaces

    def move_b(self):
        tempFaces = self.faces
        tempFaces = self.XtoZ(tempFaces)
        tempFaces = self.xAntiTurn(tempFaces,2)
        tempFaces = self.ZtoX(tempFaces)
        self.faces = tempFaces

    def move_Uu(self):
        tempFaces = self.faces
        tempFaces = self.xRegTurn(tempFaces,0)
        tempFaces = self.xRegTurn(tempFaces,1)
        tempFaces = self.rotateFace(tempFaces,4,True)
        self.faces = tempFaces

    def move_Dd(self):
        tempFaces = self.faces
        tempFaces = self.xAntiTurn(tempFaces,2)
        tempFaces = self.xAntiTurn(tempFaces,3)
        tempFaces = self.rotateFace(tempFaces,5,True)
        self.faces = tempFaces

    def move_Ll(self):
        tempFaces = self.faces
        tempFaces = self.XtoY(tempFaces)
        tempFaces = self.xRegTurn(tempFaces,0)
        tempFaces = self.xRegTurn(tempFaces,1)
        tempFaces = self.rotateFace(tempFaces,4,True)
        tempFaces = self.YtoX(tempFaces)
        self.faces = tempFaces

    def move_Rr(self):
        tempFaces = self.faces
        tempFaces = self.XtoY(tempFaces)
        tempFaces = self.xAntiTurn(tempFaces,2)
        tempFaces = self.xAntiTurn(tempFaces,3)
        tempFaces = self.rotateFace(tempFaces,5,True)
        tempFaces = self.YtoX(tempFaces)
        self.faces = tempFaces

    def move_Ff(self):
        tempFaces = self.faces
        tempFaces = self.XtoZ(tempFaces)
        tempFaces = self.xRegTurn(tempFaces,0)
        tempFaces = self.xRegTurn(tempFaces,1)
        tempFaces = self.rotateFace(tempFaces,4,True)
        tempFaces = self.ZtoX(tempFaces)
        self.faces = tempFaces

    def move_Bb(self):
        tempFaces = self.faces
        tempFaces = self.XtoZ(tempFaces)
        tempFaces = self.xAntiTurn(tempFaces,2)
        tempFaces = self.xAntiTurn(tempFaces,3)
        tempFaces = self.rotateFace(tempFaces,5,True)
        tempFaces = self.ZtoX(tempFaces)
        self.faces = tempFaces

    def move_Ua(self):
        tempFaces = self.faces
        tempFaces = self.xAntiTurn(tempFaces,0)
        tempFaces = self.rotateFace(tempFaces,4,False)
        self.faces = tempFaces

    def move_Da(self):
        tempFaces = self.faces
        tempFaces = self.xRegTurn(tempFaces,3)
        tempFaces = self.rotateFace(tempFaces,5,False)
        self.faces = tempFaces

    def move_La(self):
        tempFaces = self.faces
        tempFaces = self.XtoY(tempFaces)
        tempFaces = self.xAntiTurn(tempFaces,0)
        tempFaces = self.rotateFace(tempFaces,4,False)
        tempFaces = self.YtoX(tempFaces)
        self.faces = tempFaces

    def move_Ra(self):
        tempFaces = self.faces
        tempFaces = self.XtoY(tempFaces)
        tempFaces = self.xRegTurn(tempFaces,3)
        tempFaces = self.rotateFace(tempFaces,5,False)
        tempFaces = self.YtoX(tempFaces)
        self.faces = tempFaces

    def move_Fa(self):
        tempFaces = self.faces
        tempFaces = self.XtoZ(tempFaces)
        tempFaces = self.xAntiTurn(tempFaces,0)
        tempFaces = self.rotateFace(tempFaces,4,False)
        tempFaces = self.ZtoX(tempFaces)
        self.faces = tempFaces

    def move_Ba(self):
        tempFaces = self.faces
        tempFaces = self.XtoZ(tempFaces)
        tempFaces = self.xRegTurn(tempFaces,3)
        tempFaces = self.rotateFace(tempFaces,5,False)
        tempFaces = self.ZtoX(tempFaces)
        self.faces = tempFaces

    def move_ua(self):
        tempFaces = self.faces
        tempFaces = self.xAntiTurn(tempFaces,1)
        self.faces = tempFaces

    def move_da(self):
        tempFaces = self.faces
        tempFaces = self.xRegTurn(tempFaces,2)
        self.faces = tempFaces

    def move_la(self):
        tempFaces = self.faces
        tempFaces = self.XtoY(tempFaces)
        tempFaces = self.xAntiTurn(tempFaces,1)
        tempFaces = self.YtoX(tempFaces)
        self.faces = tempFaces

    def move_ra(self):
        tempFaces = self.faces
        tempFaces = self.XtoY(tempFaces)
        tempFaces = self.xRegTurn(tempFaces,2)
        tempFaces = self.YtoX(tempFaces)
        self.faces = tempFaces

    def move_fa(self):
        tempFaces = self.faces
        tempFaces = self.XtoZ(tempFaces)
        tempFaces = self.xAntiTurn(tempFaces,1)
        tempFaces = self.ZtoX(tempFaces)
        self.faces = tempFaces

    def move_ba(self):
        tempFaces = self.faces
        tempFaces = self.XtoZ(tempFaces)
        tempFaces = self.xRegTurn(tempFaces,2)
        tempFaces = self.ZtoX(tempFaces)
        self.faces = tempFaces

    def move_Uua(self):
        tempFaces = self.faces
        tempFaces = self.xAntiTurn(tempFaces,0)
        tempFaces = self.xAntiTurn(tempFaces,1)
        tempFaces = self.rotateFace(tempFaces,4,False)
        self.faces = tempFaces

    def move_Dda(self):
        tempFaces = self.faces
        tempFaces = self.xRegTurn(tempFaces,2)
        tempFaces = self.xRegTurn(tempFaces,3)
        tempFaces = self.rotateFace(tempFaces,5,False)
        self.faces = tempFaces

    def move_Lla(self):
        tempFaces = self.faces
        tempFaces = self.XtoY(tempFaces)
        tempFaces = self.xAntiTurn(tempFaces,0)
        tempFaces = self.xAntiTurn(tempFaces,1)
        tempFaces = self.rotateFace(tempFaces,4,False)
        tempFaces = self.YtoX(tempFaces)
        self.faces = tempFaces

    def move_Rra(self):
        tempFaces = self.faces
        tempFaces = self.XtoY(tempFaces)
        tempFaces = self.xRegTurn(tempFaces,2)
        tempFaces = self.xRegTurn(tempFaces,3)
        tempFaces = self.rotateFace(tempFaces,5,False)
        tempFaces = self.YtoX(tempFaces)
        self.faces = tempFaces

    def move_Ffa(self):
        tempFaces = self.faces
        tempFaces = self.XtoZ(tempFaces)
        tempFaces = self.xAntiTurn(tempFaces,0)
        tempFaces = self.xAntiTurn(tempFaces,1)
        tempFaces = self.rotateFace(tempFaces,4,False)
        tempFaces = self.ZtoX(tempFaces)
        self.faces = tempFaces

    def move_Bba(self):
        tempFaces = self.faces
        tempFaces = self.XtoZ(tempFaces)
        tempFaces = self.xRegTurn(tempFaces,2)
        tempFaces = self.xRegTurn(tempFaces,3)
        tempFaces = self.rotateFace(tempFaces,5,False)
        tempFaces = self.ZtoX(tempFaces)
        self.faces = tempFaces

    def move_U2(self):
        tempFaces = self.faces
        tempFaces = self.xRegTurn(tempFaces,0)
        tempFaces = self.xRegTurn(tempFaces,0)
        tempFaces = self.rotateFace(tempFaces,4,True)
        tempFaces = self.rotateFace(tempFaces,4,True)
        self.faces = tempFaces

    def move_D2(self):
        tempFaces = self.faces
        tempFaces = self.xAntiTurn(tempFaces,3)
        tempFaces = self.xAntiTurn(tempFaces,3)
        tempFaces = self.rotateFace(tempFaces,5,True)
        tempFaces = self.rotateFace(tempFaces,5,True)
        self.faces = tempFaces

    def move_L2(self):
        tempFaces = self.faces
        tempFaces = self.XtoY(tempFaces)
        tempFaces = self.xRegTurn(tempFaces,0)
        tempFaces = self.xRegTurn(tempFaces,0)
        tempFaces = self.rotateFace(tempFaces,4,True)
        tempFaces = self.rotateFace(tempFaces,4,True)
        tempFaces = self.YtoX(tempFaces)
        self.faces = tempFaces

    def move_R2(self):
        tempFaces = self.faces
        tempFaces = self.XtoY(tempFaces)
        tempFaces = self.xAntiTurn(tempFaces,3)
        tempFaces = self.xAntiTurn(tempFaces,3)
        tempFaces = self.rotateFace(tempFaces,5,True)
        tempFaces = self.rotateFace(tempFaces,5,True)
        tempFaces = self.YtoX(tempFaces)
        self.faces = tempFaces

    def move_F2(self):
        tempFaces = self.faces
        tempFaces = self.XtoZ(tempFaces)
        tempFaces = self.xRegTurn(tempFaces,0)
        tempFaces = self.xRegTurn(tempFaces,0)
        tempFaces = self.rotateFace(tempFaces,4,True)
        tempFaces = self.rotateFace(tempFaces,4,True)
        tempFaces = self.ZtoX(tempFaces)
        self.faces = tempFaces

    def move_B2(self):
        tempFaces = self.faces
        tempFaces = self.XtoZ(tempFaces)
        tempFaces = self.xAntiTurn(tempFaces,3)
        tempFaces = self.xAntiTurn(tempFaces,3)
        tempFaces = self.rotateFace(tempFaces,5,True)
        tempFaces = self.rotateFace(tempFaces,5,True)
        tempFaces = self.ZtoX(tempFaces)
        self.faces = tempFaces

    def move_u2(self):
        tempFaces = self.faces
        tempFaces = self.xRegTurn(tempFaces,1)
        tempFaces = self.xRegTurn(tempFaces,1)
        self.faces = tempFaces

    def move_d2(self):
        tempFaces = self.faces
        tempFaces = self.xAntiTurn(tempFaces,2)
        tempFaces = self.xAntiTurn(tempFaces,2)
        self.faces = tempFaces

    def move_l2(self):
        tempFaces = self.faces
        tempFaces = self.XtoY(tempFaces)
        tempFaces = self.xRegTurn(tempFaces,1)
        tempFaces = self.xRegTurn(tempFaces,1)
        tempFaces = self.YtoX(tempFaces)
        self.faces = tempFaces

    def move_r2(self):
        tempFaces = self.faces
        tempFaces = self.XtoY(tempFaces)
        tempFaces = self.xAntiTurn(tempFaces,2)
        tempFaces = self.xAntiTurn(tempFaces,2)
        tempFaces = self.YtoX(tempFaces)
        self.faces = tempFaces

    def move_f2(self):
        tempFaces = self.faces
        tempFaces = self.XtoZ(tempFaces)
        tempFaces = self.xRegTurn(tempFaces,1)
        tempFaces = self.xRegTurn(tempFaces,1)
        tempFaces = self.ZtoX(tempFaces)
        self.faces = tempFaces

    def move_b2(self):
        tempFaces = self.faces
        tempFaces = self.XtoZ(tempFaces)
        tempFaces = self.xAntiTurn(tempFaces,2)
        tempFaces = self.xAntiTurn(tempFaces,2)
        tempFaces = self.ZtoX(tempFaces)
        self.faces = tempFaces

    def move_Uu2(self):
        tempFaces = self.faces
        tempFaces = self.xRegTurn(tempFaces,0)
        tempFaces = self.xRegTurn(tempFaces,1)
        tempFaces = self.xRegTurn(tempFaces,0)
        tempFaces = self.xRegTurn(tempFaces,1)
        tempFaces = self.rotateFace(tempFaces,4,True)
        tempFaces = self.rotateFace(tempFaces,4,True)
        self.faces = tempFaces

    def move_Dd2(self):
        tempFaces = self.faces
        tempFaces = self.xAntiTurn(tempFaces,2)
        tempFaces = self.xAntiTurn(tempFaces,3)
        tempFaces = self.xAntiTurn(tempFaces,2)
        tempFaces = self.xAntiTurn(tempFaces,3)
        tempFaces = self.rotateFace(tempFaces,5,True)
        tempFaces = self.rotateFace(tempFaces,5,True)
        self.faces = tempFaces

    def move_Ll2(self):
        tempFaces = self.faces
        tempFaces = self.XtoY(tempFaces)
        tempFaces = self.xRegTurn(tempFaces,0)
        tempFaces = self.xRegTurn(tempFaces,1)
        tempFaces = self.xRegTurn(tempFaces,0)
        tempFaces = self.xRegTurn(tempFaces,1)
        tempFaces = self.rotateFace(tempFaces,4,True)
        tempFaces = self.rotateFace(tempFaces,4,True)
        tempFaces = self.YtoX(tempFaces)
        self.faces = tempFaces

    def move_Rr2(self):
        tempFaces = self.faces
        tempFaces = self.XtoY(tempFaces)
        tempFaces = self.xAntiTurn(tempFaces,2)
        tempFaces = self.xAntiTurn(tempFaces,3)
        tempFaces = self.xAntiTurn(tempFaces,2)
        tempFaces = self.xAntiTurn(tempFaces,3)
        tempFaces = self.rotateFace(tempFaces,5,True)
        tempFaces = self.rotateFace(tempFaces,5,True)
        tempFaces = self.YtoX(tempFaces)
        self.faces = tempFaces

    def move_Ff2(self):
        tempFaces = self.faces
        tempFaces = self.XtoZ(tempFaces)
        tempFaces = self.xRegTurn(tempFaces,0)
        tempFaces = self.xRegTurn(tempFaces,1)
        tempFaces = self.xRegTurn(tempFaces,0)
        tempFaces = self.xRegTurn(tempFaces,1)
        tempFaces = self.rotateFace(tempFaces,4,True)
        tempFaces = self.rotateFace(tempFaces,4,True)
        tempFaces = self.ZtoX(tempFaces)
        self.faces = tempFaces

    def move_Bb2(self):
        tempFaces = self.faces
        tempFaces = self.XtoZ(tempFaces)
        tempFaces = self.xAntiTurn(tempFaces,2)
        tempFaces = self.xAntiTurn(tempFaces,3)
        tempFaces = self.xAntiTurn(tempFaces,2)
        tempFaces = self.xAntiTurn(tempFaces,3)
        tempFaces = self.rotateFace(tempFaces,5,True)
        tempFaces = self.rotateFace(tempFaces,5,True)
        tempFaces = self.ZtoX(tempFaces)
        self.faces = tempFaces

    def XtoY(self,faces):
        faces = self.rotateFace(faces,0,True)
        faces = self.rotateFace(faces,2,False)
        temp = np.full([4,4], '', dtype=np.str)
        np.copyto(temp, faces[4])
        np.copyto(faces[4], faces[3])
        faces = self.rotateFace(faces,4,True)
        np.copyto(faces[3], faces[5])
        faces = self.rotateFace(faces,3,True)
        np.copyto(faces[5], faces[1])
        faces = self.rotateFace(faces,5,True)
        np.copyto(faces[1], temp)
        faces = self.rotateFace(faces,1,True)
        return faces

    def XtoZ(self,faces):
        faces = self.rotateFace(faces,1,True)
        faces = self.rotateFace(faces,3,False)
        temp = np.full([4,4], '', dtype=np.str)
        np.copyto(temp, faces[0])
        np.copyto(faces[0], faces[5])
        np.copyto(faces[5], faces[2])
        faces = self.rotateFace(faces,5,False)
        faces = self.rotateFace(faces,5,False)
        np.copyto(faces[2], faces[4])
        faces = self.rotateFace(faces,2,False)
        faces = self.rotateFace(faces,2,False)
        np.copyto(faces[4], temp)
        return faces

    def YtoX(self,faces):
        faces = self.rotateFace(faces,0,False)
        faces = self.rotateFace(faces,2,True)
        temp = np.full([4,4], '', dtype=np.str)
        np.copyto(temp, faces[4])
        np.copyto(faces[4], faces[1])
        faces = self.rotateFace(faces,4,False)
        np.copyto(faces[1], faces[5])
        faces = self.rotateFace(faces,1,False)
        np.copyto(faces[5], faces[3])
        faces = self.rotateFace(faces,5,False)
        np.copyto(faces[3], temp)
        faces = self.rotateFace(faces,3,False)
        return faces

    def ZtoX(self,faces):
        faces = self.rotateFace(faces,1,False)
        faces = self.rotateFace(faces,3,True)
        temp = np.full([4,4], '', dtype=np.str)
        np.copyto(temp, faces[0])
        np.copyto(faces[0], faces[4])
        np.copyto(faces[4], faces[2])
        faces = self.rotateFace(faces,4,False)
        faces = self.rotateFace(faces,4,False)
        np.copyto(faces[2], faces[5])
        faces = self.rotateFace(faces,2,False)
        faces = self.rotateFace(faces,2,False)
        np.copyto(faces[5], temp)
        return faces

    def xRegTurn(self,faces,row):
        temp = np.full([6,4,4], '', dtype=np.str)
        tempFace = np.full([4,4], '', dtype=np.str)
        np.copyto(tempFace, faces[0][:])
        for x in range(0,3):
            np.copyto(temp[x][row], faces[x+1][row])
        np.copyto(temp[3][:], tempFace)
        if row == 0:
            for x in range(0,4):
                np.copyto(temp[x][1:], faces[x][1:])
        elif row == 1:
            for x in range(0,4):
                np.copyto(temp[x][0], faces[x][0])
                np.copyto(temp[x][2:], faces[x][2:])
        elif row == 2:
            for x in range(0,4):
                np.copyto(temp[x][:2], faces[x][:2])
                np.copyto(temp[x][3], faces[x][3])
        elif row == 3:
            for x in range(0,4):
                np.copyto(temp[x][:3], faces[x][:3])
        np.copyto(temp[4:], faces[4:])
        np.copyto(faces, temp)
        return faces

    def xAntiTurn(self,faces,row):
        temp = np.full([6,4,4], '', dtype=np.str)
        tempFace = np.full([4,4], '', dtype=np.str)
        np.copyto(tempFace, faces[3][:])
        for x in range(3,0,-1):
            np.copyto(temp[x][row], faces[x-1][row])
        np.copyto(temp[0][:], tempFace)
        if row == 0:
            for x in range(0,4):
                np.copyto(temp[x][1:], faces[x][1:])
        elif row == 1:
            for x in range(0,4):
                np.copyto(temp[x][0], faces[x][0])
                np.copyto(temp[x][2:], faces[x][2:])
        elif row == 2:
            for x in range(0,4):
                np.copyto(temp[x][:2], faces[x][:2])
                np.copyto(temp[x][3], faces[x][3])
        elif row == 3:
            for x in range(0,4):
                np.copyto(temp[x][:3], faces[x][:3])
        np.copyto(temp[4:], faces[4:])
        np.copyto(faces, temp)
        return faces

    def rotateFace(self,faces,face,direction):
        if direction:
            # tempFace = np.rot90(faces[face],3)
            tempFace = np.rot90(faces[face])
            tempFace = np.rot90(tempFace)
            tempFace = np.rot90(tempFace)
        else:
            tempFace = np.rot90(faces[face])
        np.copyto(faces[face],tempFace)
        return faces

    def faceFitness(self,*args):
        if len(args) == 1 and isinstance(args[0], int):
            flatFace = self.faces[args[0]].flatten().tolist()
            faceCounts = {'w': flatFace.count('w'), 'r': flatFace.count('r'), 'y': flatFace.count('y'), 'o': flatFace.count('o'), 'b': flatFace.count('b'), 'g': flatFace.count('g')}
            sortedCounts = sorted(faceCounts.items(), key=op.itemgetter(1), reverse=True)
            return (sortedCounts[0][0],sortedCounts[0][1])
        elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], str):
            flatFace = self.faces[args[0]].flatten().tolist()
            return flatFace.count(args[1])

    def fitness1(self,faces):
        goalFaces = ['w','r','y','o','b','g']
        faceTotals = [sum([faces[x][y].tolist().count(goalFaces[x]) for y in range(0,4)]) for x in range(0,6)]
        return sum(faceTotals)

    def fitness2(self):
        centerOptions = ['w','r','y','o','b','g']
        centers = self.faces[:,1:3,1:3]
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
        faceTotals = [sum([self.faces[x][y].tolist().count(faceColors[x]) for y in range(0,4)]) for x in range(0,6)]
        return sum(faceTotals)
