Array = list(map(int,input().split()))
num = 0
for i in Array:
    num += i**2
print(num%10)