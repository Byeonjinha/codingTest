n = int(input())
a = list(map(int, input().split()))
sum = [a[0]]
for i in range(len(a) - 1):
    print(a[i],a[i+1],i,sum)
    sum.append(max(sum[i] + a[i + 1], a[i + 1]))
print(sum)
print(max(sum))