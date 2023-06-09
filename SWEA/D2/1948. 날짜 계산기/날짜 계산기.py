dates = ["1 / 31", "2 / 28", "3 / 31", "4 / 30", "5 / 31", "6 / 30", "7 / 31", "8 / 31", "9 / 30", "10 / 31", "11 / 30", "12 / 31"]
transDates = {}
for yd in dates:
    y, d = map(int, yd.split("/"))
    transDates[y] = d

T = int(input())
for tc in range(1, T + 1):
    s_flag = True
    tds = 0
    tde = 0
    ms, ds, me, de = map(int, input().split())
    for m in transDates:
        if ms == m:
            tds += ds
            s_flag = False
        elif ms != m and s_flag:
            tds += transDates[m]
        if me == m:
            tde += de
            break
        elif me != m:
            tde += transDates[m]
    print("#{} {}".format(tc, tde - tds + 1))