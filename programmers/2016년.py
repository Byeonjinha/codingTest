import datetime
def solution(a, b):
    days=['MON','TUE','WED','THU','FRI','SAT','SUN']
    return (days[datetime.datetime(2016, a, b).weekday()])

a=5
b=24
solution(a, b)