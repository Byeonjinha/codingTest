import copy
def nanum(files):
    num1 = []
    checknum1=[]
    text1 =[]
    suzza1 =[]
    text2= []
    for i in range(len(files)):
        for i2 in range(len(files[i])):
            if files[i][i2] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                v=files[i][i2]
                checknum1.append(i2)
                while True:

                    if files[i].index(files[i][i2])+1 == len(files[i]):
                        num1.append(copy.deepcopy([v,len(files[i])]))
                        break
                    if i2+1==len(files[i]):
                        num1.append(copy.deepcopy([v, len(files[i])]))
                        break
                    if files[i][i2+1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                        v+=files[i][i2+1]
                        i2+=1
                    else:

                        num1.append(copy.deepcopy([v,i2+1]))
                        break
                break
        text1.append(files[i][:checknum1[i]])
        if len(files[i])==num1[i][1]:
            text2.append('')
        else:
            text2.append(files[i][-(len(files[i])-num1[i][1]):])
        suzza1.append(num1[i][0])

    return list(zip(text1,suzza1,text2))
    # 숫자에포함되면
def daesomoonja(nanugi):
    temp = []
    temp2 = []
    for i in range(len(nanugi)):
        temp.append([nanugi[i][0].lower(),int(nanugi[i][1]),i])
    temp.sort(key=lambda x:(x[0],x[1]))
    for i in range(len(temp)):
        temp2.append(nanugi[temp[i][2]])
    return temp2


def solution(files):
    answer = []
    nanugi = nanum(files)

    jung10 = daesomoonja(nanugi)
    for i in jung10:
        answer.append(''.join(i))

    return answer
files =  ["img000012345", "img1.png","img00000","IMG02"]
solution(files)