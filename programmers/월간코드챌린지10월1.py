import copy
import sys
ungdaptime=[]
churitime=[]
countlist=[]
countlist2=[]
trafficlist=[]
def solution(lines):
    n = lines
    for i in n:
        cheehwan(i.split(" "))
    start = min(ungdaptime)
    end = max(ungdaptime)+ churitime[ungdaptime.index(max(ungdaptime))]
    countlist=check(start, end, trafficlist)
    countlist2= copy.deepcopy(countlist)
    maxlog = 0
    for i2 in range(2,len(countlist)):
        countlist2[i2]+=countlist2[i2-1]
    while(countlist.count(-1)!=0):
        countlist[countlist.index(-1)]=0
    for i3 in range(2,len(countlist)):
        templog = countlist2[i3]+sum(countlist[i3:i3+1200])
        if templog > maxlog :
            maxlog = templog
    return maxlog



def check(start, end ,trafficlist):
    countlist=[0 for _ in range(start,end+2)]
    for i in range(0,len(trafficlist)):
        startpoint =trafficlist[i][0]-start
        endpoint = trafficlist[i][1]-start
        countlist[startpoint+1]+=1
        countlist[endpoint+1]-=1
    return countlist


def cheehwan(i2):
    i3 =i2[1].split(":")
    ungdaptime.append(int((float(i3[0])*3600+float(i3[1])*60+float(i3[2]))*1000))
    i4 = i2[2].split("s")
    churitime.append(int(float(i4[0])*1000))
    trafficlist.append([int((float(i3[0])*3600+float(i3[1])*60+float(i3[2]))*1000), int((float(i3[0])*3600+float(i3[1])*60+float(i3[2]))*1000)+int(float(i4[0])*1000)])
    return


print(ungdaptime)
print(churitime)