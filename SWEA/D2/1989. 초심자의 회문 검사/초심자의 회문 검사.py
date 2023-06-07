T = int(input())
for i in range(1, T + 1):
    sentence = list(input().strip())
    if sentence == list(reversed(sentence)):
        a = 1
    else:
        a = 0
    print("#{} {}".format(i, a))
