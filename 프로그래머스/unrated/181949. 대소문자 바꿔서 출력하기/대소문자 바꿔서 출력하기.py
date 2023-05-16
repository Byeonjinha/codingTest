from string import ascii_lowercase
str = input()
answer = ""
for i in str:
    if i in ascii_lowercase:
        answer += i.upper()
    else:
        answer += i.lower()
print(answer)
