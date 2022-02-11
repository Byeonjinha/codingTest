def solution(x):
    y=sum(list(map(int , (list(str(x))))))
    return True if int(x)%y==0 else  False
x=12
solution(x)