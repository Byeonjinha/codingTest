def solution(id_list, k):
    cus_dic = {}
    answer = 0
    for i in range(len(id_list)):
        kk= list(set(id_list[i].split(" ")))
        for i2 in range(len(kk)):
            cus_dic[kk[i2]] = 0

    for i in range(len(id_list)):
        kk = list(set(id_list[i].split(" ")))
        for i3 in range(len(kk)):
            if cus_dic[kk[i3]] < k:
                cus_dic[kk[i3]] = cus_dic[kk[i3]] +1
    for i in cus_dic:
        answer+=(cus_dic[i])

    return answer


id_list= ["A B C D", "A D", "A B D", "B D"]
k =  2

solution(id_list, k)