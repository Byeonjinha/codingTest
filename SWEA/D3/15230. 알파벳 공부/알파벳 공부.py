T = int(input())
alpha = "abcdefghijklmnopqrstuvwxyz"
for tc_idx in range(T):
    answer  = 0 
    ex = input()
    for i in range(len(ex)):
        if alpha[i] == ex[i]:
            answer += 1
        else:
            break
    print("#"+str(tc_idx + 1), answer)