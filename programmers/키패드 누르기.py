leftson=[4,0]
rightson=[4,0]
sonlist=[]
def solution(numbers, hand):
    leftson = [4, 1]
    rightson = [4, 3]
    for i in numbers:
        if i in [1,4,7]:
            leftson=lbutton(i)
        if i in [3,6,9]:
            rightson=rbutton(i)
        if i in [2,5,8,0]:
            middlebutton(i,leftson,rightson,hand)
    answer = ''.join(sonlist)
    print(answer)
    return answer

def lbutton(i):
    leftson=[]
    if i ==1:
        leftson=[1,1]
        sonlist.append("L")
    elif i ==4:
        leftson=[2,1]
        sonlist.append("L")
    elif i== 7:
        leftson=[3,1]
        sonlist.append("L")

    return leftson
def rbutton(i):
    rightson=[]
    if i ==3:
        rightson=[1,3]
        sonlist.append("R")
    elif i ==6:
        rightson=[2,3]
        sonlist.append("R")
    elif i== 9:
        rightson=[3,3]
        sonlist.append("R")
    return rightson

def middlebutton(i,leftson,rightson,hand):
    leftsonguri=0
    rightsonguri=0
    zwapyo=[]
    if i == 2:
        zwapyo = [1,2]
    elif i == 5:
        zwapyo = [2,2]
    elif i == 8:
        zwapyo = [3,2]
    elif i == 0:
        zwapyo = [4,2]
    leftsonguri = abs(zwapyo[0]-leftson[0])+abs(zwapyo[1]-leftson[1])
    rightsonguri = abs(zwapyo[0]-rightson[0])+abs(zwapyo[1]-rightson[1])
    if leftsonguri>rightsonguri:
        sonlist.append("R")
        if len(rightson)!=0:
            rightson.pop()
            rightson.pop()
        rightson.append(zwapyo[0])
        rightson.append(zwapyo[1])
    elif leftsonguri<rightsonguri:
        sonlist.append("L")
        if len(leftson)!=0:
            leftson.pop()
            leftson.pop()
        leftson.append(zwapyo[0])
        leftson.append(zwapyo[1])
    elif leftsonguri==rightsonguri and hand=='right':
        sonlist.append('R')
        if len(rightson)!=0:
            rightson.pop()
            rightson.pop()
        rightson.append(zwapyo[0])
        rightson.append(zwapyo[1])
    elif leftsonguri==rightsonguri and hand=='left':
        sonlist.append('L')
        if len(leftson)!=0:
            leftson.pop()
            leftson.pop()
        leftson.append(zwapyo[0])
        leftson.append(zwapyo[1])




numbers= [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand=	"left"
result=	"LRLLLRLLRRL"
solution(numbers, hand)