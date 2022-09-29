import sys

def transtime(hour, minute, addTime):
    hour = hour*60
    totalTime = hour + minute + addTime
    if totalTime >= 1440:
        totalTime -= 1440
    transHour = totalTime //60
    transMinute = totalTime - (transHour*60)
    return str(transHour) + " " +  str(transMinute)
time = sys.stdin.readline().split()
hour = time[0]
minute = time[1]
addTime = int(sys.stdin.readline())

print(transtime(int(hour),int(minute),int(addTime)))