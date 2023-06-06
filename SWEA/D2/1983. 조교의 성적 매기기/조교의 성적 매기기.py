T = int(input())

grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

for tc_idx in range(1, T+1):
    N, K = map(int, input().split())
    grade_num = N // 10
    score = []
    for num in range(N):
        middle, last, task = map(int,input().split())
        score.append( [middle * 0.35 + last * 0.45 + task * 0.2 , num + 1])
    score.sort(key = lambda x: -x[0])
    for i in range(len(score)):
        if score[i][1] == K:
            answer = grades[score.index(score[i]) // grade_num]
        	
    print("#{} {}".format(tc_idx, answer))