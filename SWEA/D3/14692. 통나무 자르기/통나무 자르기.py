T = int(input())
for tc_idx in range(T):
    num = int(input())
    if num%2 == 0 :
        print("#"+str(tc_idx + 1), "Alice")
    else:
        print("#"+str(tc_idx + 1), "Bob")