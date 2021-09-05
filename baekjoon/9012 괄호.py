def check_VPS(data):
    result = []
    for i in data:
        if i == '(':
            result.append(i)
        else:
            if len(result) == 0:
                print('NO')
                return
            else:
                result.pop()

    if len(result) == 0:
        print('YES')
    else:
        print('NO')


n = int(input())
for i in range(n):
    parenthesis = input()
    check_VPS(parenthesis)
