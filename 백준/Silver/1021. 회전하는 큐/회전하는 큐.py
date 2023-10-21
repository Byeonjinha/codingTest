from collections import deque

n, m = map(int, input().split())

num_array = deque([i for i in range(1, n + 1)])

answer = 0

def pop():
    global num_array
    num_array.popleft()

def move_left():
    global num_array, answer
    num_array.append(num_array.popleft())
    answer += 1

def move_right():
    global num_array, answer
    num_array.appendleft(num_array.pop())
    answer += 1

to_find_number_list = list(map(int, input().split()))

for num in to_find_number_list:
    front = num_array.index(num)
    back = list(reversed(num_array)).index(num)
    if front <= back:
        for _ in range(front):
            move_left()
    else:
        for _ in range(back + 1):
            move_right()
    pop()

print(answer)