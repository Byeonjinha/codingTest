import math

car=[]
car2=[]
def time1(time,car,car2):
    for i in range(len(time)-1):
        if time[i][2]=='IN' and time[i+1][2]=='OUT':       #in out 쌍일경우
            intime=(int(time[i][0].split(':')[0])*60+int(time[i][0].split(':')[1]))
            outtime=(int(time[i+1][0].split(':')[0])*60+int(time[i+1][0].split(':')[1]))
            car2[car.index(time[i][1])]+=(outtime-intime)
        elif time[i][2]=='IN' and time[i+1][2]!='OUT':
            intime = (int(time[i][0].split(':')[0]) * 60 + int(time[i][0].split(':')[1]))
            outtime = 1439
            car2[car.index(time[i][1])] += (outtime - intime)
    if time[-1][2]=='IN':
        intime = (int(time[-1   ][0].split(':')[0]) * 60 + int(time[-1  ][0].split(':')[1]))
        outtime = 1439
        car2[car.index(time[-1  ][1])] += (outtime - intime)
def gyesan(car2,fees):

    car3=[]
    # fees = [120, 0, 60, 591]
    for i in range(len(car2)):               #기본시간보다 작으면 기본요금
        if car2[i]<=fees[0]:
            car3.append(fees[1])
        elif car2[i]>fees[0]:                #기본시간보다 크면
            car3.append( (math.ceil((car2[i]-fees[0])/fees[2]))*fees[3] +fees[1]    )

    return(car3)



def solution(fees, records):
    ipchul=[]
    car = []

    for i in records:
        ipchul.append(i.split(' '))
        car.append(i.split(' ')[1])
    ipchul.sort(key=lambda x:(x[1])) #차량번호순으로 정렬
    car = (sorted(list(set(car))))
    car2=[0]*len(car)

    time1(ipchul,car,car2)

    answer = gyesan(car2,fees)

    return answer

fees=[120, 0, 60, 591]
records=["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
solution(fees, records)