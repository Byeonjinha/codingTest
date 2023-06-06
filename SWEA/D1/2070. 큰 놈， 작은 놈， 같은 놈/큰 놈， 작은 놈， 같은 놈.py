T = int(input())
for tc_idx in range(1, T+1):
    a, b = map(int, input().split())
    if a < b:
        answer = "<"
    elif a == b:
        answer = "="
    elif a > b:
        answer = ">"
    print("#{} {}".format(tc_idx, answer))