from string import ascii_lowercase
somunja = list(ascii_lowercase)
sujja = ['0','1','2','3','4','5','6','7','8','9']
def solution(registered_list, new_id):
    sujjaindex=9999
    temp=new_id
    for i in range(len(new_id)):
        if new_id[i] in sujja:
            sujjaindex=min(i,sujjaindex)

    if sujjaindex==9999:
        sujjaindex = len(new_id)
        if temp in registered_list:
            new_id=new_id+'1'
        else:
            new_id=new_id+'0'

    count=0
    while new_id in registered_list:
        new_id= new_id[0:sujjaindex] + str((int(new_id[sujjaindex:])+1))
        count+=1
        if count==9000:
            break

    if new_id[sujjaindex]=='0':

        return temp

    return new_id



registered_list =["card", "ace13", "ace16", "banker", "ace17", "ace14"]
new_id = "ace15"
solution(registered_list, new_id)