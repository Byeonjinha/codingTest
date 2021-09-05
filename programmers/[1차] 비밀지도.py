import copy
bimil = []
bimil2 = []
bimil3 = []
bimil4 = []
def solution(n, arr1, arr2):
    for i in arr1:
        if len(bin(i).split('b')[1])<n:
            bimil.append(str(0)*(n-len(bin(i).split('b')[1]))+str(bin(i).split('b')[1]))
        else:
            bimil.append(str(bin(i).split('b')[1]))
    for i in arr2:
        if len(bin(i).split('b')[1])<n:
            bimil2.append(str(0)*(n-len(bin(i).split('b')[1]))+str(bin(i).split('b')[1]))
        else:
            bimil2.append(str(bin(i).split('b')[1]))

    for i in range(n):
        for i2 in range(n):
            if  int(list(bimil[i])[i2])+int(list(bimil2[i])[i2]) >0 :
                bimil3.append('#')
            else:
                bimil3.append(' ')
        bimil4.append(''.join(copy.deepcopy(bimil3)))
        bimil3.clear()
    answer = bimil4
    return answer


