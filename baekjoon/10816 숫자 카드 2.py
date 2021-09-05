input_num = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = sorted(numbers)
input_num2 = int(input())
numbers2 = list(map(int, input().split()))
sorted_numbers2 = sorted(numbers2)
cnt_dict = dict()
idx = 0
for num in sorted_numbers2:
    cnt = 0
    if num not in cnt_dict.keys():
        while idx < len(numbers):
            if num == sorted_numbers[idx]:
                cnt += 1
                idx += 1
            elif num > sorted_numbers[idx]:
                idx += 1
            else:
                break
        cnt_dict[num] = cnt
answer = [str(cnt_dict[num])for num in numbers2]
print(" ".join(answer))

