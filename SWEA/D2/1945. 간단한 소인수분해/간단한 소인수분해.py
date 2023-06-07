def factorize(n):
    factors = [0, 0, 0, 0, 0]  # 소수 지수를 저장할 리스트 [a, b, c, d, e]

    prime_factors = [2, 3, 5, 7, 11]  # 소수들
    idx = 0  # prime_factors 리스트의 인덱스

    while n > 1:
        if n % prime_factors[idx] == 0:  # n이 현재 소수로 나누어떨어질 경우
            n = n // prime_factors[idx]  # n을 현재 소수로 나눈 몫으로 갱신
            factors[idx] += 1  # 소수 지수 증가
        else:
            idx += 1  # 다음 소수로 넘어감

    return factors


T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 주어진 숫자 N

    prime_exponents = factorize(N)  # 소인수분해하여 소수 지수를 구함

    result = ' '.join(str(exponent) for exponent in prime_exponents)  # 소수 지수들을 문자열로 변환하여 공백으로 구분하여 합침

    print(f"#{tc} {result}")
