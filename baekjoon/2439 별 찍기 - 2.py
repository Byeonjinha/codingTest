a = int(input())
for b in range(a,0,-1):

    print(" "*(b-1),end="")
    print("*"*(a-b+1))