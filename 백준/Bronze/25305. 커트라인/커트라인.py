import sys
award = sys.stdin.readline().split()
peoples = list(map(int, list(sys.stdin.readline().split())))
peoples.sort(reverse=True)
print(peoples[int(award[1])-1])