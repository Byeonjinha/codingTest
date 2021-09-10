music=[]
def time1(info):
    start=  int(info[0].split(':')[0])*60+int(info[0].split(':')[1])
    end= int(info[1].split(':')[0])*60+int(info[1].split(':')[1])
    return end-start
def code(code):
    codelist = (list(code))
    while codelist.count('#')!=0:
        if codelist[codelist.index('#')-1]=='C':
            codelist[codelist.index('#')-1]='H'
            codelist.remove('#')
        elif codelist[codelist.index('#')-1]=='D':
            codelist[codelist.index('#')-1]='I'
            codelist.remove('#')
        elif codelist[codelist.index('#')-1]=='E':
            codelist[codelist.index('#')-1]='J'
            codelist.remove('#')
        elif codelist[codelist.index('#')-1]=='F':
            codelist[codelist.index('#')-1]='K'
            codelist.remove('#')
        elif codelist[codelist.index('#')-1]=='G':
            codelist[codelist.index('#')-1]='L'
            codelist.remove('#')
        elif codelist[codelist.index('#')-1]=='A':
            codelist[codelist.index('#')-1]='M'
            codelist.remove('#')
        elif codelist[codelist.index('#')-1]=='B':
            codelist[codelist.index('#')-1]='N'
            codelist.remove('#')


    return codelist
def playcodelist(jaesengsigan,codelist):
    playcodelist=[]

    for i in range(jaesengsigan):
        playcodelist.append(codelist[i%len(codelist)])
    return playcodelist

def solution(m, musicinfos):
    m=list(m)
    for i in range(len(musicinfos)):
        info = (musicinfos[i].split(','))
        jaesengsigan = time1(info)
        codelist = code(info[3])
        m = code(m)

        playcode = ''.join(playcodelist(jaesengsigan,codelist))
        m = ''.join(m)
        if m in playcode :
            music.append([info[2],playcode,jaesengsigan,i])
    if len(music)==0:
        return '(None)'


    music.sort(key=lambda x: (-x[2],x[3]))
    answer = music[0][0]

    return answer

m= "CCB"
musicinfos=["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]
solution(m, musicinfos)