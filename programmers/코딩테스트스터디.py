while True:
    t = input()
    if t == '0':
        break
    b = list(t)
    print(b.reverse())
    print(sorted(t))
    print(t.sort())
    if list(t) == b :
        print("yes")
    else:
        print("no")
