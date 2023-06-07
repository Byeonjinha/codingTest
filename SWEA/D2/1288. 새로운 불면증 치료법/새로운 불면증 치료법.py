def count_digits(N):
    digits = set()
    i = 1
    while len(digits) < 10:
        num = N * i
        digits = digits.union(set(list(map(int,list(str(num))))))
        i += 1
    return num

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = count_digits(N)
    print(f"#{tc} {result}")
