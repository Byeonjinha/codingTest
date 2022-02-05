
def Njinbub(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return list(rev_base[::-1])

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        if numbers[i]%2==0:
            answer.append(numbers[i]+1)
        else:
            if Njinbub(numbers[i],2)[-2:] == ['0','1']:

                answer.append(numbers[i]+1)
            else:
                count = 0
                k = Njinbub(numbers[i],2)
                for j in range(len(k)-1,-1,-1):
                    print(k[j])
                    if int(k[j])%2==1:
                        count+=1
                    else:
                        break
                print(count,numbers[i])
                answer.append(numbers[i]+(2**(count-1)))

    return answer
numbers= [2,7]
solution(numbers)