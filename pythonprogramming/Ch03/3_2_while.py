"""
날짜 : 2021/08/10
이름 : 변진하
내용 : 파이썬 while문 실습하기 교재 p64
"""

# while
num = 1

while num < 5:
    print('%d회 반복' % num)
    num += 1

# 1부터 10까지 합
tot, k = 0, 1

while k <= 10:

    tot += k
    k += 1

print('1부터 10까지 합 :', tot)

# 1부터 10까지 짝수합
total, j = 0, 1

while j <= 10:

    if j % 2 == 0:
        total += j

    j += 1

print('1부터 10까지 짝수합 :', total)

# break
i = 1

while True:

    if i % 5 == 0 and i % 7 == 0:
        #반복문 종료
        break

    i += 1

print('5와 7의 최소공배수 :', i)

# continue
sum, n = 0, 1

while n <= 10:

    n += 1

    if n % 2 == 1:
        # 반복문 처음으로 이동
        continue

    sum += n

print('1부터 10까지 짝수합 :', sum)