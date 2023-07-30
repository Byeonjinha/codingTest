table = [1 for _ in range(491)]
for i in range(len(table)):
    if i == 0 or i == 1: table[i] = 1
    else: table[i] = table[i - 1] + table[i - 2]

while True:
    n = int(input())
    if n == -1: exit(0)
    print("Hour {}: {} cow(s) affected".format(n, table[n - 1]))