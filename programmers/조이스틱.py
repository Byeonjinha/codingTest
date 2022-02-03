from string import ascii_uppercase
answer_list = []
def left_1(x,score,alpha_list,answer_list,name):
    x0temp1 = x[0].copy()
    for j in range(len(name)):
        if x0temp1[j] != name[j]:
            x2temp1 = x[2]
            count = 0
            while j != x2temp1:
                count += 1
                x2temp1 += 1
                if x2temp1 == len(name):
                    x2temp1 = 0
            x0temp1[j] = name[j]
            sum_1 = x[1] + count + score[alpha_list.index(name[j])]
            return [x0temp1, sum_1, j]

        elif x[0] == list(name):
            answer_list.append(x[1])
            break
def right_1(x,score,alpha_list,answer_list,name):
    x0temp1 = x[0].copy()
    for j in range(len(name),0,-1):
        if x0temp1[j-1] != name[j-1]:
            x2temp1 = x[2]
            count = 0
            while j-1 != x2temp1:
                count += 1
                x2temp1 -= 1
                if x2temp1 == -1:
                    x2temp1 = len(name)-1
            x0temp1[j-1] = name[j-1]
            sum_1 = x[1] + count + score[alpha_list.index(name[j-1])]

            return [x0temp1, sum_1, j-1]

        elif x[0] == list(name):
            answer_list.append(x[1])
            break
def solution(name):
    answer_list=[]
    alpha_list = list(ascii_uppercase)
    global name2
    name2= name
    temp = ["A" for i in range(len(name))]
    current = 0
    name_list= [[temp,0,current]]
    score = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    answer = 0
    while name_list :
        x= name_list.pop()
        k1= right_1(x, score, alpha_list, answer_list,name)
        if k1 is not None:
            name_list.append(k1)
        k2 = left_1(x, score, alpha_list, answer_list,name)
        if k2 is not None:
            name_list.append(k2)

    print(min(answer_list))
    return answer
