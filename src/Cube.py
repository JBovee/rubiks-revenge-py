import numpy as np

class Cube:

    def __init__(self):
        self.faces = np.array([[['w','x','x','w'],
                                ['w','w','w','w'],
                                ['w','w','w','w'],
                                ['w','w','w','w']],
                                [['r','x','x','r'],
                                ['r','r','r','r'],
                                ['r','r','r','r'],
                                ['r','r','r','r']],
                                [['y','x','x','y'],
                                ['y','y','y','y'],
                                ['y','y','y','y'],
                                ['y','y','y','y']],
                                [['o','x','x','o'],
                                ['o','o','o','o'],
                                ['o','o','o','o'],
                                ['o','o','o','o']],
                                [['b','x','x','b'],
                                ['b','b','b','b'],
                                ['b','b','b','b'],
                                ['b','b','b','b']],
                                [['g','x','x','g'],
                                ['g','g','g','g'],
                                ['g','g','g','g'],
                                ['g','g','g','g']]])

    def printCube(self):
        print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in self.faces[4]]))
        [print('\n'.join([''.join(['{:3}'.format(self.faces[x][y][z]) for x in range(0,4) for z in range(0,4)])])) for y in range(0,4)]
        print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in self.faces[5]]))

    def quarterTurn(self, moveType):
        def rotateFace(self,face, direction):
            if direction:
                self.faces[face] = np.rot90(self.faces[face],3)
            else:
                self.faces[face] = np.rot90(self.faces[face])
            print("rot")
        def xRegTurn(self,row):
            np.copyto(tempFace, self.faces[0][:])
            for x in range(0,3):
                np.copyto(temp[x][row], self.faces[x+1][row])
            np.copyto(temp[3][:], tempFace)
            if row == 0:
                for x in range(0,4):
                    np.copyto(temp[x][1:], self.faces[x][1:])
            elif row == 1:
                for x in range(0,4):
                    np.copyto(temp[x][0], self.faces[x][0])
                    np.copyto(temp[x][2:], self.faces[x][2:])
            elif row == 2:
                for x in range(0,4):
                    np.copyto(temp[x][:1], self.faces[x][:1])
                    np.copyto(temp[x][3], self.faces[x][3])
            elif row == 3:
                for x in range(0,4):
                    np.copyto(temp[x][:2], self.faces[x][:2])
            np.copyto(temp[4:], self.faces[4:])
            np.copyto(self.faces, temp)
        def yRegTurn(self,column):
            faces = np.array([4,0,5,2])
            cols = np.array([[0,0,0,3],[1,1,1,2],[2,2,2,1],[3,3,3,0]])
            np.copyto(tempFace, self.faces[faces[3]][:])
            for x in range(0,3):
                for y in range(0,4):
                    np.copyto(temp[faces[x]][y][cols[column][x]], self.faces[faces[x+1]][y][cols[column][x+1]])
            np.copyto(temp[faces[0]][:], tempFace)
            if column == 0:
                for x in range(0,3):
                    for y in range(0,4):
                        if cols[column][x] == 0: np.copyto(temp[faces[x]][y][cols[column][x]], self.faces[faces[x+1]][y][cols[column][x+1]])
                np.copyto(temp[faces[0]][:], tempFace)
                for x in range(0,4):
                    for y in range(0,4):
                        np.copyto(temp[faces[x]][y][:3], self.faces[faces[x]][y][:3])
            elif column == 1:
                for x in range(0,4):
                    for y in range(0,4):
                        np.copyto(temp[faces[x]][y][0], self.faces[faces[x]][y][0])
                        np.copyto(temp[faces[x]][y][2:], self.faces[faces[x]][y][2:])
            elif column == 2:
                for x in range(0,4):
                    for y in range(0,4):
                        np.copyto(temp[faces[x]][y][:2], self.faces[faces[x]][y][:2])
                        np.copyto(temp[faces[x]][y][3], self.faces[faces[x]][y][3])
            elif column == 3:
                for x in range(0,4):
                    for y in range(0,4):
                        np.copyto(temp[faces[x]][y][1:], self.faces[faces[x]][y][1:])
            np.copyto(temp[1], self.faces[1])
            np.copyto(temp[3], self.faces[3])
            np.copyto(self.faces, temp)
            print(temp)
            print(self.faces)
        def zRegTurn():
            print()
        def xAntiTurn(self,row):
            np.copyto(tempFace, self.faces[3][:])
            for x in range(3,0,-1):
                np.copyto(temp[x][row], self.faces[x-1][row])
            np.copyto(temp[0][:], tempFace)
            if row == 0:
                for x in range(0,4):
                    np.copyto(temp[x][1:], self.faces[x][1:])
            elif row == 1:
                for x in range(0,4):
                    np.copyto(temp[x][0], self.faces[x][0])
                    np.copyto(temp[x][2:], self.faces[x][2:])
            elif row == 2:
                for x in range(0,4):
                    np.copyto(temp[x][:2], self.faces[x][:2])
                    np.copyto(temp[x][3], self.faces[x][3])
            elif row == 3:
                for x in range(0,4):
                    np.copyto(temp[x][:2], self.faces[x][:2])
            np.copyto(temp[4:], self.faces[4:])
            np.copyto(self.faces, temp)
        def yAntiTurn():
            print()
        def zAntiTurn():
            print()

        temp = np.full([6,4,4], '', dtype=np.str)
        tempFace = np.full([4, 4], '', dtype=np.str)
        if moveType == 0:
            xRegTurn(self,0)
            rotateFace(self,4,True)
        elif moveType == 1:
            xAntiTurn(self,3)
            rotateFace(self,5,True)
        elif moveType == 2:
            yRegTurn(self,0)
            rotateFace(self,3,True)
        elif moveType == 3:
            print()
        elif moveType == 4:
            print()
        elif moveType == 5:
            print()
        elif moveType == 6:
            xRegTurn(self,1)
        elif moveType == 7:
            xAntiTurn(self,2)
        elif moveType == 8:
            yRegTurn(self,1)
        elif moveType == 9:
            print()
        elif moveType == 10:
            print()
        elif moveType == 11:
            print()
        elif moveType == 12:
            print()
        elif moveType == 13:
            print()
        elif moveType == 14:
            print()
        elif moveType == 15:
            print()
        elif moveType == 16:
            print()
        elif moveType == 17:
            print()
        print("turn")

    def XtoY(self):
        self.rotateFace(0,True)
        self.rotateFace(2,False)
        temp = np.full([4,4], '', dtype=np.str)
        np.copyto(temp, self.faces[4])
        np.copyto(self.faces[4], self.faces[3])
        self.rotateFace(4,True)
        np.copyto(self.faces[3], self.faces[5])
        self.rotateFace(3,True)
        np.copyto(self.faces[5], self.faces[1])
        self.rotateFace(5,True)
        np.copyto(self.faces[1], temp)
        self.rotateFace(1,True)

    def XtoZ(self):
        self.rotateFace(1,True)
        self.rotateFace(3,False)
        temp = np.full([4,4], '', dtype=np.str)
        np.copyto(temp, self.faces[0])
        np.copyto(self.faces[0], self.faces[5])
        np.copyto(self.faces[5], self.faces[2])
        self.rotateFace(5,False)
        self.rotateFace(5,False)
        np.copyto(self.faces[2], self.faces[4])
        self.rotateFace(2,False)
        self.rotateFace(2,False)
        np.copyto(self.faces[4], temp)

    def YtoX(self):
        self.rotateFace(0,False)
        self.rotateFace(2,True)
        temp = np.full([4,4], '', dtype=np.str)
        np.copyto(temp, self.faces[4])
        np.copyto(self.faces[4], self.faces[1])
        self.rotateFace(4,False)
        np.copyto(self.faces[1], self.faces[5])
        self.rotateFace(1,False)
        np.copyto(self.faces[5], self.faces[3])
        self.rotateFace(5,False)
        np.copyto(self.faces[3], temp)
        self.rotateFace(3,False)

    def ZtoX(self):
        self.rotateFace(1,False)
        self.rotateFace(3,True)
        temp = np.full([4,4], '', dtype=np.str)
        np.copyto(temp, self.faces[0])
        np.copyto(self.faces[0], self.faces[4])
        np.copyto(self.faces[4], self.faces[2])
        self.rotateFace(4,False)
        self.rotateFace(4,False)
        np.copyto(self.faces[2], self.faces[5])
        self.rotateFace(2,False)
        self.rotateFace(2,False)
        np.copyto(self.faces[5], temp)

    def rotateFace(self,face, direction):
        if direction:
            self.faces[face] = np.rot90(self.faces[face],3)
        else:
            self.faces[face] = np.rot90(self.faces[face])
        print("rot")

    def fitness():
        print("fit")
