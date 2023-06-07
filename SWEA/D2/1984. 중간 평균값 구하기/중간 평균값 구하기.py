T = int(input())
for i in range(1, T + 1):
    nums = list(map(int, input().split()))
    nums.remove(max(nums))
    nums.remove(min(nums))
    print("#"+str(i), round(sum(nums)/len(nums)))