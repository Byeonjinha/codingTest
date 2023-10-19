import heapq

n = int(input())
presents = []

for _ in range(n):
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        if len(presents) == 0:
            print(-1)
        else:
            print(-heapq.heappop(presents))
    else:
        presents_count, *present_array = nums
        for present in present_array:
            heapq.heappush(presents, -present)
