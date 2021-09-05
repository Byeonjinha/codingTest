slist=[]
byeonhwanlist =[]
def solution(s):
    for i in s:
        slist.append(i)
    for i in range(1,len(slist)):
        if slist[i-1]=='z':
            byeonhwanlist.append('0')
        if slist[i-1]=='o' and slist[i]=='n':
            byeonhwanlist.append('1')
        if slist[i-1]=='t' and slist[i]=='w':
            byeonhwanlist.append('2')
        if slist[i-1]=='t' and slist[i]=='h':
            byeonhwanlist.append('3')
        if slist[i-1]=='f' and slist[i]=='o':
            byeonhwanlist.append('4')
        if slist[i-1]=='f' and slist[i]=='i':
            byeonhwanlist.append('5')
        if slist[i-1]=='s' and slist[i]=='i':
            byeonhwanlist.append('6')
        if slist[i-1]=='s' and slist[i]=='e':
            byeonhwanlist.append('7')
        if slist[i-1]=='e' and slist[i]=='i':
            byeonhwanlist.append('8')
        if slist[i-1]=='n' and slist[i]=='i':
            byeonhwanlist.append('9')
        if slist[i-1]=='0':
            byeonhwanlist.append('0')
        if slist[i-1]=='1':
            byeonhwanlist.append('1')
        if slist[i-1]=='2':
            byeonhwanlist.append('2')
        if slist[i-1]=='3':
            byeonhwanlist.append('3')
        if slist[i-1]=='4':
            byeonhwanlist.append('4')
        if slist[i-1]=='5':
            byeonhwanlist.append('5')
        if slist[i-1]=='6':
            byeonhwanlist.append('6')
        if slist[i-1]=='7':
            byeonhwanlist.append('7')
        if slist[i-1]=='8':
            byeonhwanlist.append('8')
        if slist[i-1]=='9':
            byeonhwanlist.append('9')
    if slist[- 1] == '0':
        byeonhwanlist.append('0')
    if slist[- 1] == '1':
        byeonhwanlist.append('1')
    if slist[- 1] == '2':
        byeonhwanlist.append('2')
    if slist[- 1] == '3':
        byeonhwanlist.append('3')
    if slist[- 1] == '4':
        byeonhwanlist.append('4')
    if slist[- 1] == '5':
        byeonhwanlist.append('5')
    if slist[- 1] == '6':
        byeonhwanlist.append('6')
    if slist[- 1] == '7':
        byeonhwanlist.append('7')
    if slist[- 1] == '8':
        byeonhwanlist.append('8')
    if slist[- 1] == '9':
        byeonhwanlist.append('9')
    answer =  int("".join(byeonhwanlist))
    return answer
