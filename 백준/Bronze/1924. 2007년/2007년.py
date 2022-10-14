import calendar
weeks = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT','SUN']
month, day = list(map(int,input().split()))
print(weeks[calendar.weekday(2007,month,day)])