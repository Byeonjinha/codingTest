import sys


def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


x, y, = map(int, sys.stdin.readline().strip().split())
gcd = gcd(x, y)
print(gcd)
print(x * y // gcd)
