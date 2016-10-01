from __future__ import print_function
import numpy as np
import random as rand
import operator as op

class Cube:

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

        self.temp = np.full([6,4,4], '', dtype=np.str)

        self.moves = np.array(['U','D','L','R','F','B','u','d','l','r','f','b','Uu','Dd','Ll','Rr','Ff','Bb','Ua','Da','La','Ra','Fa','Ba','ua','da','la','ra','fa','ba','Uua','Dda','Lla','Rra','Ffa','Bba','U2','D2','L2','R2','F2','B2','u2','d2','l2','r2','f2','b2','Uu2','Dd2','Ll2','Rr2','Ff2','Bb2'])

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

    def move(self,moveType):
        tempFaces = self.faces
        self.faces = self.moveTypes(tempFaces,moveType)

    def moveTypes(self,faces,moveType):
        if moveType == 0: #U
            faces = self.xRegTurn(faces,0)
            faces = self.rotateFace(faces,4,True)
        elif moveType == 1: #D
            faces = self.xAntiTurn(faces,3)
            faces = self.rotateFace(faces,5,True)
        elif moveType == 2: #L
            faces = self.XtoY(faces)
            faces = self.xRegTurn(faces,0)
            faces = self.rotateFace(faces,4,True)
            faces = self.YtoX(faces)
        elif moveType == 3: #R
            faces = self.XtoY(faces)
            faces = self.xAntiTurn(faces,3)
            faces = self.rotateFace(faces,5,True)
            faces = self.YtoX(faces)
        elif moveType == 4: #F
            faces = self.XtoZ(faces)
            faces = self.xRegTurn(faces,0)
            faces = self.rotateFace(faces,4,True)
            faces = self.ZtoX(faces)
        elif moveType == 5: #B
            faces = self.XtoZ(faces)
            faces = self.xAntiTurn(faces,3)
            faces = self.rotateFace(faces,5,True)
            faces = self.ZtoX(faces)
        elif moveType == 6: #u
            faces = self.xRegTurn(faces,1)
        elif moveType == 7: #d
            faces = self.xAntiTurn(faces,2)
        elif moveType == 8: #l
            faces = self.XtoY(faces)
            faces = self.xRegTurn(faces,1)
            faces = self.YtoX(faces)
        elif moveType == 9: #r
            faces = self.XtoY(faces)
            faces = self.xAntiTurn(faces,2)
            faces = self.YtoX(faces)
        elif moveType == 10: #f
            faces = self.XtoZ(faces)
            faces = self.xRegTurn(faces,1)
            faces = self.ZtoX(faces)
        elif moveType == 11: #b
            faces = self.XtoZ(faces)
            faces = self.xAntiTurn(faces,2)
            faces = self.ZtoX(faces)
        elif moveType == 12: #Uu
            faces = self.xRegTurn(faces,0)
            faces = self.xRegTurn(faces,1)
            faces = self.rotateFace(faces,4,True)
        elif moveType == 13: #Dd
            faces = self.xAntiTurn(faces,2)
            faces = self.xAntiTurn(faces,3)
            faces = self.rotateFace(faces,5,True)
        elif moveType == 14: #Ll
            faces = self.XtoY(faces)
            faces = self.xRegTurn(faces,0)
            faces = self.xRegTurn(faces,1)
            faces = self.rotateFace(faces,4,True)
            faces = self.YtoX(faces)
        elif moveType == 15: #Rr
            faces = self.XtoY(faces)
            faces = self.xAntiTurn(faces,2)
            faces = self.xAntiTurn(faces,3)
            faces = self.rotateFace(faces,5,True)
            faces = self.YtoX(faces)
        elif moveType == 16: #Ff
            faces = self.XtoZ(faces)
            faces = self.xRegTurn(faces,0)
            faces = self.xRegTurn(faces,1)
            faces = self.rotateFace(faces,4,True)
            faces = self.ZtoX(faces)
        elif moveType == 17: #Bb
            faces = self.XtoZ(faces)
            faces = self.xAntiTurn(faces,2)
            faces = self.xAntiTurn(faces,3)
            faces = self.rotateFace(faces,5,True)
            faces = self.ZtoX(faces)
        elif moveType == 18: #U'
            faces = self.xAntiTurn(faces,0)
            faces = self.rotateFace(faces,4,False)
        elif moveType == 19: #D'
            faces = self.xRegTurn(faces,3)
            faces = self.rotateFace(faces,5,False)
        elif moveType == 20: #L'
            faces = self.XtoY(faces)
            faces = self.xAntiTurn(faces,0)
            faces = self.rotateFace(faces,4,False)
            faces = self.YtoX(faces)
        elif moveType == 21: #R'
            faces = self.XtoY(faces)
            faces = self.xRegTurn(faces,3)
            faces = self.rotateFace(faces,5,False)
            faces = self.YtoX(faces)
        elif moveType == 22: #F'
            faces = self.XtoZ(faces)
            faces = self.xAntiTurn(faces,0)
            faces = self.rotateFace(faces,4,False)
            faces = self.ZtoX(faces)
        elif moveType == 23: #B'
            faces = self.XtoZ(faces)
            faces = self.xRegTurn(faces,3)
            faces = self.rotateFace(faces,5,False)
            faces = self.ZtoX(faces)
        elif moveType == 24: #u'
            faces = self.xAntiTurn(faces,1)
        elif moveType == 25: #d'
            faces = self.xRegTurn(faces,2)
        elif moveType == 26: #l'
            faces = self.XtoY(faces)
            faces = self.xAntiTurn(faces,1)
            faces = self.YtoX(faces)
        elif moveType == 27: #r'
            faces = self.XtoY(faces)
            faces = self.xRegTurn(faces,2)
            faces = self.YtoX(faces)
        elif moveType == 28: #f'
            faces = self.XtoZ(faces)
            faces = self.xAntiTurn(faces,1)
            faces = self.ZtoX(faces)
        elif moveType == 29: #b'
            faces = self.XtoZ(faces)
            faces = self.xRegTurn(faces,2)
            faces = self.ZtoX(faces)
        elif moveType == 30: #Uu'
            faces = self.xAntiTurn(faces,0)
            faces = self.xAntiTurn(faces,1)
            faces = self.rotateFace(faces,4,False)
        elif moveType == 31: #Dd'
            faces = self.xRegTurn(faces,2)
            faces = self.xRegTurn(faces,3)
            faces = self.rotateFace(faces,5,False)
        elif moveType == 32: #Ll'
            faces = self.XtoY(faces)
            faces = self.xAntiTurn(faces,0)
            faces = self.xAntiTurn(faces,1)
            faces = self.rotateFace(faces,4,False)
            faces = self.YtoX(faces)
        elif moveType == 33: #Rr'
            faces = self.XtoY(faces)
            faces = self.xRegTurn(faces,2)
            faces = self.xRegTurn(faces,3)
            faces = self.rotateFace(faces,5,False)
            faces = self.YtoX(faces)
        elif moveType == 34: #Ff'
            faces = self.XtoZ(faces)
            faces = self.xAntiTurn(faces,0)
            faces = self.xAntiTurn(faces,1)
            faces = self.rotateFace(faces,4,False)
            faces = self.ZtoX(faces)
        elif moveType == 35: #Bb'
            faces = self.XtoZ(faces)
            faces = self.xRegTurn(faces,2)
            faces = self.xRegTurn(faces,3)
            faces = self.rotateFace(faces,5,False)
            faces = self.ZtoX(faces)
        elif moveType == 36: #U2
            faces = self.xRegTurn(faces,0)
            faces = self.xRegTurn(faces,0)
            faces = self.rotateFace(faces,4,True)
            faces = self.rotateFace(faces,4,True)
        elif moveType == 37: #D2
            faces = self.xAntiTurn(faces,3)
            faces = self.xAntiTurn(faces,3)
            faces = self.rotateFace(faces,5,True)
            faces = self.rotateFace(faces,5,True)
        elif moveType == 38: #L2
            faces = self.XtoY(faces)
            faces = self.xRegTurn(faces,0)
            faces = self.xRegTurn(faces,0)
            faces = self.rotateFace(faces,4,True)
            faces = self.rotateFace(faces,4,True)
            faces = self.YtoX(faces)
        elif moveType == 39: #R2
            faces = self.XtoY(faces)
            faces = self.xAntiTurn(faces,3)
            faces = self.xAntiTurn(faces,3)
            faces = self.rotateFace(faces,5,True)
            faces = self.rotateFace(faces,5,True)
            faces = self.YtoX(faces)
        elif moveType == 40: #F2
            faces = self.XtoZ(faces)
            faces = self.xRegTurn(faces,0)
            faces = self.xRegTurn(faces,0)
            faces = self.rotateFace(faces,4,True)
            faces = self.rotateFace(faces,4,True)
            faces = self.ZtoX(faces)
        elif moveType == 41: #B2
            faces = self.XtoZ(faces)
            faces = self.xAntiTurn(faces,3)
            faces = self.xAntiTurn(faces,3)
            faces = self.rotateFace(faces,5,True)
            faces = self.rotateFace(faces,5,True)
            faces = self.ZtoX(faces)
        elif moveType == 42: #u2
            faces = self.xRegTurn(faces,1)
            faces = self.xRegTurn(faces,1)
        elif moveType == 43: #d2
            faces = self.xAntiTurn(faces,2)
            faces = self.xAntiTurn(faces,2)
        elif moveType == 44: #l2
            faces = self.XtoY(faces)
            faces = self.xRegTurn(faces,1)
            faces = self.xRegTurn(faces,1)
            faces = self.YtoX(faces)
        elif moveType == 45: #r2
            faces = self.XtoY(faces)
            faces = self.xAntiTurn(faces,2)
            faces = self.xAntiTurn(faces,2)
            faces = self.YtoX(faces)
        elif moveType == 46: #f2
            faces = self.XtoZ(faces)
            faces = self.xRegTurn(faces,1)
            faces = self.xRegTurn(faces,1)
            faces = self.ZtoX(faces)
        elif moveType == 47: #b2
            faces = self.XtoZ(faces)
            faces = self.xAntiTurn(faces,2)
            faces = self.xAntiTurn(faces,2)
            faces = self.ZtoX(faces)
        elif moveType == 48: #Uu2
            faces = self.xRegTurn(faces,0)
            faces = self.xRegTurn(faces,1)
            faces = self.xRegTurn(faces,0)
            faces = self.xRegTurn(faces,1)
            faces = self.rotateFace(faces,4,True)
            faces = self.rotateFace(faces,4,True)
        elif moveType == 49: #Dd2
            faces = self.xAntiTurn(faces,2)
            faces = self.xAntiTurn(faces,3)
            faces = self.xAntiTurn(faces,2)
            faces = self.xAntiTurn(faces,3)
            faces = self.rotateFace(faces,5,True)
            faces = self.rotateFace(faces,5,True)
        elif moveType == 50: #Ll2
            faces = self.XtoY(faces)
            faces = self.xRegTurn(faces,0)
            faces = self.xRegTurn(faces,1)
            faces = self.xRegTurn(faces,0)
            faces = self.xRegTurn(faces,1)
            faces = self.rotateFace(faces,4,True)
            faces = self.rotateFace(faces,4,True)
            faces = self.YtoX(faces)
        elif moveType == 51: #Rr2
            faces = self.XtoY(faces)
            faces = self.xAntiTurn(faces,2)
            faces = self.xAntiTurn(faces,3)
            faces = self.xAntiTurn(faces,2)
            faces = self.xAntiTurn(faces,3)
            faces = self.rotateFace(faces,5,True)
            faces = self.rotateFace(faces,5,True)
            faces = self.YtoX(faces)
        elif moveType == 52: #Ff2
            faces = self.XtoZ(faces)
            faces = self.xRegTurn(faces,0)
            faces = self.xRegTurn(faces,1)
            faces = self.xRegTurn(faces,0)
            faces = self.xRegTurn(faces,1)
            faces = self.rotateFace(faces,4,True)
            faces = self.rotateFace(faces,4,True)
            faces = self.ZtoX(faces)
        elif moveType == 53: #Bb2
            faces = self.XtoZ(faces)
            faces = self.xAntiTurn(faces,2)
            faces = self.xAntiTurn(faces,3)
            faces = self.xAntiTurn(faces,2)
            faces = self.xAntiTurn(faces,3)
            faces = self.rotateFace(faces,5,True)
            faces = self.rotateFace(faces,5,True)
            faces = self.ZtoX(faces)
        return faces

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

    def scramble(self,n):
        for i in range(0,n):
            tNum = rand.randint(0,54)
            print('\n ' + str(tNum) + '|' + self.moves[tNum] + '\n----------------------------------')
            self.move(tNum)

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
        # return zip(faceColors,faceTotals)
