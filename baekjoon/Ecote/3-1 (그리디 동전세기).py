import sys
n = int(sys.stdin.readline())
count = 0
coin_types = list(map(int,sys.stdin.readline().split()))

for coin in coin_types:
    count += n // coin # 해당화폐ㅗㄹ 거슬로 줄 수 있는 동전의 개수 세기
    n %= coin
print(count)