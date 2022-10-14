str = input()
strLength = len(str)
start = 0
end = 10
while strLength > 0 :

    print(str[start:end])
    strLength -= 10
    start += 10
    end += 10