num = input()
cham = {}
for i in num:
    if i not in cham:
        cham[i]=1
    else:
        cham[i]=cham[i]+14

print(cham)