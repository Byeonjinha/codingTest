import sys

n= sys.stdin.readline().strip()
suzza = []
for i in n:
    suzza.append(i)
suzza.sort(reverse=True)
print(''.join(suzza))