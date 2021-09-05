def solution(answers):
    answer = []
    try:
        for i in range(0,9999):
            il2.append(answers[i]-il[i])
            lee2.append(answers[i]-lee[i])
            sam2.append(answers[i]-sam[i])
    except:
        pass
    if il2.count(0)==lee2.count(0)==sam2.count(0):
        answer.append(1)
        answer.append(2)
        answer.append(3)
    elif il2.count(0)>lee2.count(0) and il2.count(0)>sam2.count(0):
        answer.append(1)
    elif il2.count(0)<lee2.count(0) and lee2.count(0)>sam2.count(0):
        answer.append(2)
    elif il2.count(0)<sam2.count(0) and lee2.count(0)<sam2.count(0):
        answer.append(3)
    elif il2.count(0)==lee2.count(0) and il2.count(0)>sam2.count(0):
        answer.append(1)
        answer.append(2)
    elif il2.count(0)<lee2.count(0) and lee2.count(0)==sam2.count(0):
        answer.append(2)
        answer.append(3)
    elif il2.count(0)>lee2.count(0) and il2.count(0)==sam2.count(0):
        answer.append(1)
        answer.append(3)
    print(answer)

    return answer

il = []
il2=[]
lee = []
lee2=[]
sam = []
sam2=[]
for i in range(0,2000):
    il.append(1)
    il.append(2)
    il.append(3)
    il.append(4)
    il.append(5)
for i in range(0,1250):
    lee.append(2)
    lee.append(1)
    lee.append(2)
    lee.append(3)
    lee.append(2)
    lee.append(4)
    lee.append(2)
    lee.append(5)
for i in range(0,1000):
    sam.append(3)
    sam.append(3)
    sam.append(1)
    sam.append(1)
    sam.append(2)
    sam.append(2)
    sam.append(4)
    sam.append(4)
    sam.append(5)
    sam.append(5)

