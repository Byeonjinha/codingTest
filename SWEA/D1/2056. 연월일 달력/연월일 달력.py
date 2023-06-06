T = int(input())

def validation(M, D):
    if M in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= D <= 31
    elif M in [4, 6, 9, 11]:
        return 1 <= D <= 30
    elif M in [2]:
        return 1 <= D <= 28
    else:
        return False

for tc_idx in range(1, T+1):
    date = input()
    Y = date[0:4]
    M = date[4:6]
    D = date[6:8]
    if (validation(int(M), int(D))):
        print("#{} {}/{}/{}".format(tc_idx, Y, M, D))
    else:
        print("#{} -1".format(tc_idx))