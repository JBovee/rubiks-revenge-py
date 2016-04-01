import numpy as np

def moveTypes(faces,moveType):
    if moveType == 0: #U
        faces = xRegTurn(faces,0)
        faces = rotateFace(faces,4,True)
    elif moveType == 1: #D
        faces = xAntiTurn(faces,3)
        faces = rotateFace(faces,5,True)
    elif moveType == 2: #L
        faces = XtoY(faces)
        faces = xRegTurn(faces,0)
        faces = rotateFace(faces,4,True)
        faces = YtoX(faces)
    elif moveType == 3: #R
        faces = XtoY(faces)
        faces = xAntiTurn(faces,3)
        faces = rotateFace(faces,5,True)
        faces = YtoX(faces)
    elif moveType == 4: #F
        faces = XtoZ(faces)
        faces = xRegTurn(faces,0)
        faces = rotateFace(faces,4,True)
        faces = ZtoX(faces)
    elif moveType == 5: #B
        faces = XtoZ(faces)
        faces = xAntiTurn(faces,3)
        faces = rotateFace(faces,5,True)
        faces = ZtoX(faces)
    elif moveType == 6: #u
        faces = xRegTurn(faces,1)
    elif moveType == 7: #d
        faces = xAntiTurn(faces,2)
    elif moveType == 8: #l
        faces = XtoY(faces)
        faces = xRegTurn(faces,1)
        faces = YtoX(faces)
    elif moveType == 9: #r
        faces = XtoY(faces)
        faces = xAntiTurn(faces,2)
        faces = YtoX(faces)
    elif moveType == 10: #f
        faces = XtoZ(faces)
        faces = xRegTurn(faces,1)
        faces = ZtoX(faces)
    elif moveType == 11: #b
        faces = XtoZ(faces)
        faces = xAntiTurn(faces,2)
        faces = ZtoX(faces)
    elif moveType == 12: #Uu
        faces = xRegTurn(faces,0)
        faces = xRegTurn(faces,1)
        faces = rotateFace(faces,4,True)
    elif moveType == 13: #Dd
        faces = xAntiTurn(faces,2)
        faces = xAntiTurn(faces,3)
        faces = rotateFace(faces,5,True)
    elif moveType == 14: #Ll
        faces = XtoY(faces)
        faces = xRegTurn(faces,0)
        faces = xRegTurn(faces,1)
        faces = rotateFace(faces,4,True)
        faces = YtoX(faces)
    elif moveType == 15: #Rr
        faces = XtoY(faces)
        faces = xAntiTurn(faces,2)
        faces = xAntiTurn(faces,3)
        faces = rotateFace(faces,5,True)
        faces = YtoX(faces)
    elif moveType == 16: #Ff
        faces = XtoZ(faces)
        faces = xRegTurn(faces,0)
        faces = xRegTurn(faces,1)
        faces = rotateFace(faces,4,True)
        faces = ZtoX(faces)
    elif moveType == 17: #Bb
        faces = XtoZ(faces)
        faces = xAntiTurn(faces,2)
        faces = xAntiTurn(faces,3)
        faces = rotateFace(faces,5,True)
        faces = ZtoX(faces)
    elif moveType == 18: #U'
        faces = xAntiTurn(faces,0)
        faces = rotateFace(faces,4,False)
    elif moveType == 19: #D'
        faces = xRegTurn(faces,3)
        faces = rotateFace(faces,5,False)
    elif moveType == 20: #L'
        faces = XtoY(faces)
        faces = xAntiTurn(faces,0)
        faces = rotateFace(faces,4,False)
        faces = YtoX(faces)
    elif moveType == 21: #R'
        faces = XtoY(faces)
        faces = xRegTurn(faces,3)
        faces = rotateFace(faces,5,False)
        faces = YtoX(faces)
    elif moveType == 22: #F'
        faces = XtoZ(faces)
        faces = xAntiTurn(faces,0)
        faces = rotateFace(faces,4,False)
        faces = ZtoX(faces)
    elif moveType == 23: #B'
        faces = XtoZ(faces)
        faces = xRegTurn(faces,3)
        faces = rotateFace(faces,5,False)
        faces = ZtoX(faces)
    elif moveType == 24: #u'
        faces = xAntiTurn(faces,1)
    elif moveType == 25: #d'
        faces = xRegTurn(faces,2)
    elif moveType == 26: #l'
        faces = XtoY(faces)
        faces = xAntiTurn(faces,1)
        faces = YtoX(faces)
    elif moveType == 27: #r'
        faces = XtoY(faces)
        faces = xRegTurn(faces,2)
        faces = YtoX(faces)
    elif moveType == 28: #f'
        faces = XtoZ(faces)
        faces = xAntiTurn(faces,1)
        faces = ZtoX(faces)
    elif moveType == 29: #b'
        faces = XtoZ(faces)
        faces = xRegTurn(faces,2)
        faces = ZtoX(faces)
    elif moveType == 30: #Uu'
        faces = xAntiTurn(faces,0)
        faces = xAntiTurn(faces,1)
        faces = rotateFace(faces,4,False)
    elif moveType == 31: #Dd'
        faces = xRegTurn(faces,2)
        faces = xRegTurn(faces,3)
        faces = rotateFace(faces,5,False)
    elif moveType == 32: #Ll'
        faces = XtoY(faces)
        faces = xAntiTurn(faces,0)
        faces = xAntiTurn(faces,1)
        faces = rotateFace(faces,4,False)
        faces = YtoX(faces)
    elif moveType == 33: #Rr'
        faces = XtoY(faces)
        faces = xRegTurn(faces,2)
        faces = xRegTurn(faces,3)
        faces = rotateFace(faces,5,False)
        faces = YtoX(faces)
    elif moveType == 34: #Ff'
        faces = XtoZ(faces)
        faces = xAntiTurn(faces,0)
        faces = xAntiTurn(faces,1)
        faces = rotateFace(faces,4,False)
        faces = ZtoX(faces)
    elif moveType == 35: #Bb'
        faces = XtoZ(faces)
        faces = xRegTurn(faces,2)
        faces = xRegTurn(faces,3)
        faces = rotateFace(faces,5,False)
        faces = ZtoX(faces)
    elif moveType == 36: #U2
        faces = xRegTurn(faces,0)
        faces = xRegTurn(faces,0)
        faces = rotateFace(faces,4,True)
        faces = rotateFace(faces,4,True)
    elif moveType == 37: #D2
        faces = xAntiTurn(faces,3)
        faces = xAntiTurn(faces,3)
        faces = rotateFace(faces,5,True)
        faces = rotateFace(faces,5,True)
    elif moveType == 38: #L2
        faces = XtoY(faces)
        faces = xRegTurn(faces,0)
        faces = xRegTurn(faces,0)
        faces = rotateFace(faces,4,True)
        faces = rotateFace(faces,4,True)
        faces = YtoX(faces)
    elif moveType == 39: #R2
        faces = XtoY(faces)
        faces = xAntiTurn(faces,3)
        faces = xAntiTurn(faces,3)
        faces = rotateFace(faces,5,True)
        faces = rotateFace(faces,5,True)
        faces = YtoX(faces)
    elif moveType == 40: #F2
        faces = XtoZ(faces)
        faces = xRegTurn(faces,0)
        faces = xRegTurn(faces,0)
        faces = rotateFace(faces,4,True)
        faces = rotateFace(faces,4,True)
        faces = ZtoX(faces)
    elif moveType == 41: #B2
        faces = XtoZ(faces)
        faces = xAntiTurn(faces,3)
        faces = xAntiTurn(faces,3)
        faces = rotateFace(faces,5,True)
        faces = rotateFace(faces,5,True)
        faces = ZtoX(faces)
    elif moveType == 42: #u2
        faces = xRegTurn(faces,1)
        faces = xRegTurn(faces,1)
    elif moveType == 43: #d2
        faces = xAntiTurn(faces,2)
        faces = xAntiTurn(faces,2)
    elif moveType == 44: #l2
        faces = XtoY(faces)
        faces = xRegTurn(faces,1)
        faces = xRegTurn(faces,1)
        faces = YtoX(faces)
    elif moveType == 45: #r2
        faces = XtoY(faces)
        faces = xAntiTurn(faces,2)
        faces = xAntiTurn(faces,2)
        faces = YtoX(faces)
    elif moveType == 46: #f2
        faces = XtoZ(faces)
        faces = xRegTurn(faces,1)
        faces = xRegTurn(faces,1)
        faces = ZtoX(faces)
    elif moveType == 47: #b2
        faces = XtoZ(faces)
        faces = xAntiTurn(faces,2)
        faces = xAntiTurn(faces,2)
        faces = ZtoX(faces)
    elif moveType == 48: #Uu2
        faces = xRegTurn(faces,0)
        faces = xRegTurn(faces,1)
        faces = xRegTurn(faces,0)
        faces = xRegTurn(faces,1)
        faces = rotateFace(faces,4,True)
        faces = rotateFace(faces,4,True)
    elif moveType == 49: #Dd2
        faces = xAntiTurn(faces,2)
        faces = xAntiTurn(faces,3)
        faces = xAntiTurn(faces,2)
        faces = xAntiTurn(faces,3)
        faces = rotateFace(faces,5,True)
        faces = rotateFace(faces,5,True)
    elif moveType == 50: #Ll2
        faces = XtoY(faces)
        faces = xRegTurn(faces,0)
        faces = xRegTurn(faces,1)
        faces = xRegTurn(faces,0)
        faces = xRegTurn(faces,1)
        faces = rotateFace(faces,4,True)
        faces = rotateFace(faces,4,True)
        faces = YtoX(faces)
    elif moveType == 51: #Rr2
        faces = XtoY(faces)
        faces = xAntiTurn(faces,2)
        faces = xAntiTurn(faces,3)
        faces = xAntiTurn(faces,2)
        faces = xAntiTurn(faces,3)
        faces = rotateFace(faces,5,True)
        faces = rotateFace(faces,5,True)
        faces = YtoX(faces)
    elif moveType == 52: #Ff2
        faces = XtoZ(faces)
        faces = xRegTurn(faces,0)
        faces = xRegTurn(faces,1)
        faces = xRegTurn(faces,0)
        faces = xRegTurn(faces,1)
        faces = rotateFace(faces,4,True)
        faces = rotateFace(faces,4,True)
        faces = ZtoX(faces)
    elif moveType == 53: #Bb2
        faces = XtoZ(faces)
        faces = xAntiTurn(faces,2)
        faces = xAntiTurn(faces,3)
        faces = xAntiTurn(faces,2)
        faces = xAntiTurn(faces,3)
        faces = rotateFace(faces,5,True)
        faces = rotateFace(faces,5,True)
        faces = ZtoX(faces)
    return faces

def XtoY(faces):
    faces = rotateFace(faces,0,True)
    faces = rotateFace(faces,2,False)
    temp = np.full([4,4], '', dtype=np.str)
    np.copyto(temp, faces[4])
    np.copyto(faces[4], faces[3])
    faces = rotateFace(faces,4,True)
    np.copyto(faces[3], faces[5])
    faces = rotateFace(faces,3,True)
    np.copyto(faces[5], faces[1])
    faces = rotateFace(faces,5,True)
    np.copyto(faces[1], temp)
    faces = rotateFace(faces,1,True)
    return faces

def XtoZ(faces):
    faces = rotateFace(faces,1,True)
    faces = rotateFace(faces,3,False)
    temp = np.full([4,4], '', dtype=np.str)
    np.copyto(temp, faces[0])
    np.copyto(faces[0], faces[5])
    np.copyto(faces[5], faces[2])
    faces = rotateFace(faces,5,False)
    faces = rotateFace(faces,5,False)
    np.copyto(faces[2], faces[4])
    faces = rotateFace(faces,2,False)
    faces = rotateFace(faces,2,False)
    np.copyto(faces[4], temp)
    return faces

def YtoX(faces):
    faces = rotateFace(faces,0,False)
    faces = rotateFace(faces,2,True)
    temp = np.full([4,4], '', dtype=np.str)
    np.copyto(temp, faces[4])
    np.copyto(faces[4], faces[1])
    faces = rotateFace(faces,4,False)
    np.copyto(faces[1], faces[5])
    faces = rotateFace(faces,1,False)
    np.copyto(faces[5], faces[3])
    faces = rotateFace(faces,5,False)
    np.copyto(faces[3], temp)
    faces = rotateFace(faces,3,False)
    return faces

def ZtoX(faces):
    faces = rotateFace(faces,1,False)
    faces = rotateFace(faces,3,True)
    temp = np.full([4,4], '', dtype=np.str)
    np.copyto(temp, faces[0])
    np.copyto(faces[0], faces[4])
    np.copyto(faces[4], faces[2])
    faces = rotateFace(faces,4,False)
    faces = rotateFace(faces,4,False)
    np.copyto(faces[2], faces[5])
    faces = rotateFace(faces,2,False)
    faces = rotateFace(faces,2,False)
    np.copyto(faces[5], temp)
    return faces

def xRegTurn(faces,row):
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

def xAntiTurn(faces,row):
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

def rotateFace(faces,face,direction):
    if direction:
        tempFace = np.rot90(faces[face])
        tempFace = np.rot90(faces[face])
        tempFace = np.rot90(faces[face])
    else:
        tempFace = np.rot90(faces[face])
    np.copyto(faces[face],tempFace)
    return faces

