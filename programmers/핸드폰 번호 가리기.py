list=[]
def solution(phone_number):
    for i in phone_number:
        list.append(i)
    for i in range(len(phone_number)-4):
        list[i]='*'
    phone_number=''.join(list)

    answer = phone_number
    print(answer)
    return answer
