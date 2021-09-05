n= 8
k= 2
cmd= ["D 12","C","U 3","C","D 4","C","U 2","Z","Z"]

def solution(n, k, cmd):
    name = [0] * n
    wichil = k

    for i in cmd:

        if i[0]=='U':
            wichil=U_X(wichil,i)
        if i[0]=='D':
            wichil=D_X(wichil,i)
        if i[0]=='C':
            name, wichil=C(name,wichil)
        if i[0]=='Z':
            Z(name)

    monhaemuckgetnae = ['O']*n
    for i in sackjae:
        monhaemuckgetnae[i]='X'
    answer = ''.join(monhaemuckgetnae)
    return answer



def U_X(wichi,cmd):
    p=cmd.split(" ")
    wichi-=int(p[1])
    return wichi
def D_X(wichi,cmd):

    p=cmd.split(" ")

    wichi += int(p[1])
    return wichi
def C(name, wichi):
    if wichi==len(name):
        sackjae.append(wichi)
        name.remove(name[wichi])
        wichi-=1
    else:
        sackjae.append(wichi)
        name.remove(name[wichi])
    return name, wichi

def Z(name):
    name.insert(sackjae[-1],0)
    sackjae.pop()
    return name
sackjae =[]





solution(n, k, cmd)
