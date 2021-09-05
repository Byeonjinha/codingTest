# import re 모듈공부하기
# 정규식공부하기
# lower ,upper 사용
# while문 좀더이해하기
# list [] 문자열길이에 대해 좀더 이해하기
# join 함수 공부하기
# isdigit, isalpha 함수 공부하기


# def solution(new_id):
#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#     st = re.sub('\.+', '.', st)
#     st = re.sub('^[.]|[.]$', '', st)
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return st

# def solution(new_id):
#     answer = ''
#     # 1
#     new_id = new_id.lower()
#     # 2
#     for c in new_id:
#         if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
#             answer += c
#     # 3
#     while '..' in answer:
#         answer = answer.replace('..', '.')
#     # 4
#     if answer[0] == '.':
#         answer = answer[1:] if len(answer) > 1 else '.'
#     if answer[-1] == '.':
#         answer = answer[:-1]
#     # 5
#     if answer == '':
#         answer = 'a'
#     # 6
#     if len(answer) > 15:
#         answer = answer[:15]
#         if answer[-1] == '.':
#             answer = answer[:-1]
#     # 7
#     while len(answer) < 3:
#         answer += answer[-1]
#     return answer



def solution(new_id):
    new_id2=[]
    new_id3=[]
    #1
    new_id = new_id.lower()
    #2
    for A in new_id:
        if A=='a'or     \
        A=='b'or    \
        A== 'c' or  \
        A== 'd' or \
        A== 'e'or    \
        A== 'f'or\
        A== 'g'or\
        A== 'h'or\
        A== 'i'or\
        A== 'j'or\
        A== 'k'or\
        A== 'l'or\
        A== 'm'or\
        A== 'n'or\
        A== 'o'or\
        A== 'p'or\
        A== 'q'or\
        A== 'r'or\
        A== 's'or\
        A== 'x'or\
        A== 't'or\
        A== 'u'or\
        A== 'v'or\
        A== 'w'or\
        A== 'x'or\
        A== 'y'or\
        A== 'z'or\
        A== '1'or\
        A== '2'or\
        A== '3'or\
        A== '4'or\
        A== '5'or\
        A== '6'or\
        A== '7'or\
        A== '8'or\
        A== '9'or\
        A== '0'or\
        A== '-' or\
        A== '_' or\
        A== '.' :
            new_id2.append(A)

    #3
    if len(new_id2) >= 2 :
        for A in range(0,len(new_id2)-1):
            if new_id2[A]=="." and new_id2[A+1]==".":
                new_id2=new_id2
            else:
                new_id3.append(new_id2[A])
        new_id3.append(new_id2[-1])
    elif len(new_id2) == 1 :
        new_id3.append(new_id2[0])
    else:
        new_id3==0
    #41
    if len(new_id3)==0:
        new_id3=new_id3
    elif len(new_id3)==1:
        if new_id3[0] ==".":
            del new_id3[0]
        else:
            new_id3
    else:
        if new_id3[0] ==".":
            del new_id3[0]
        if new_id3[-1]==".":
            del new_id3[-1]

    #5
    if len(new_id3)==0 :
        new_id3.append("a")
    #6
    if len(new_id3)>= 16:
        for A in range(0,len(new_id3)-15):
            del new_id3[15]
        if new_id3[0] ==".":
                del new_id3[0]
        if new_id3[-1]==".":
                del new_id3[-1]
    #7
    while len(new_id3) <=2:
        new_id3.append(new_id3[-1])

    result = str("")
    #8
    for A in new_id3:
        result = result + A
    answer = result
    return answer