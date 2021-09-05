def solution(price, money, count):
    sum=0
    for i in range(1,count+1):
        sum+= price*i
    if money-sum>=0:
        return 0
    else:
        return sum-money




price=  3
money=	20
count=  4
solution(price, money, count)