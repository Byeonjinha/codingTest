A= input()
list=[]
count=int(0)
temp=int(0)
for i in A:
    list.append(i)
list.append("*")
list.append("*")
for i in range(2,len(A)+2):
    if temp>0:
        temp=temp-1
        continue

    if list[i-2]=="c" and list[i-1]== "=":
        count+=1
        temp+=1

    elif list[i-2]=="c" and list[i-1]=="-":
        count+=1
        temp += 1

    elif list[i - 2] == "d" and list[i - 1] == "z" and list[i]=="=":
        count += 1
        temp += 2

    elif list[i - 2] == "d" and list[i - 1] == "-":
        count += 1
        temp += 1

    elif list[i - 2] == "l" and list[i - 1] == "j":
        count += 1
        temp += 1

    elif list[i - 2] == "n" and list[i - 1] == "j":
        count += 1
        temp += 1

    elif list[i - 2] == "s" and list[i - 1] == "=":
        count += 1
        temp += 1

    elif list[i - 2] == "z" and list[i - 1] == "=" and list[i-3]!="d":
        count += 1
        temp += 1

    else:

        count+=1



print(count)
