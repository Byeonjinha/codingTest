import sys

T = map(int,sys.stdin.readline().split())
A = set(map(int,sys.stdin.readline().split()))
B = set(map(int,sys.stdin.readline().split()))
C = set.intersection(A, B)
print(len(set.union(A,B)-C))