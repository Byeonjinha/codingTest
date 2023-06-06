from string import ascii_uppercase

a = list(ascii_uppercase)
al = input()
for i in al:
    print(a.index(i) + 1, end=" ")
