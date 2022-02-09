def solution(s):
    count=0
    sum=0
    while s != "1":
        count+=1
        p2 = "1"*list(s).count("1")
        p3  = len(s)-len(p2)
        sum+=p3
        print(p3,"p3")
        print(bin(len(p2))[2:])
        s=bin(len(p2))[2:]
    print(count,sum)
    return [count , sum  ]
s = "1111111"
solution(s)