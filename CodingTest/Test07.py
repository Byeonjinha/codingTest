# import sys
# n = sys.stdin.readline()
#
# list = []
# list1 = [0]*2
# list2 = [0]*2
# list3 = [0]*2
# list4 = [0]*2
# list5 = [0]*2
# list6 = [0]*2
# list7 = [0]*2
# list8 = [0]*2
# count = 0
# for xy in n:
#     if xy == "a":
#         xy = 1
#     if xy == "b":
#         xy = 2
#     if xy == "c":
#         xy = 3
#     if xy == "d":
#         xy = 4
#     if xy == "e":
#         xy = 5
#     if xy == "f":
#         xy = 6
#     if xy == "g":
#         xy = 7
#     if xy == "h":
#         xy = 8
#     if xy == "1":
#         xy = 1
#     if xy == "2":
#         xy = 2
#     if xy == "3":
#         xy = 3
#     if xy == "4":
#         xy = 4
#     if xy == "5":
#         xy = 5
#     if xy == "6":
#         xy = 6
#     if xy == "7":
#         xy = 7
#     if xy == "8":
#         xy = 8
#     list.append(xy)
# list1[0] = list[0]-2
# list1[1] = list[1]-1
# list2[0] = list[0]-1
# list2[1] = list[1]-2
# list3[0] = list[0]+1
# list3[1] = list[1]-2
# list4[0] = list[0]+2
# list4[1] = list[1]-1
# list5[0] = list[0]+2
# list5[1] = list[1]+1
# list6[0] = list[0]+1
# list6[1] = list[1]+2
# list7[0] = list[0]-1
# list7[1] = list[1]+2
# list8[0] = list[0]-2
# list8[1] = list[1]+1
# if 0<list1[0]<9 and 0<list1[1]<9:
#     count+=1
# if 0<list2[0]<9 and 0<list2[1]<9:
#     count+=1
# if 0<list3[0]<9 and 0<list3[1]<9:
#     count+=1
# if 0<list4[0]<9 and 0<list4[1]<9:
#     count+=1
# if 0<list5[0]<9 and 0<list5[1]<9:
#     count+=1
# if 0<list6[0]<9 and 0<list6[1]<9:
#     count+=1
# if 0<list7[0]<9 and 0<list7[1]<9:
#     count+=1
# if 0<list8[0]<9 and 0<list8[1]<9:
#     count+=1
# print(count)
#
#
#
input_data = input()
row = int(input_data[1]) # 1
# 아스키코드로 표현 ord
column = int(ord(input_data[0])) - int(ord('a')) + 1   # 1

cnt = 0
dx = [2,2,-2,-2,-1,1,-1,1]
dy = [1,-1,1,-1,2,2,-2,-2]
for num in range(8):
    temp_row = row
    temp_column = column
    temp_row += dy[num]
    temp_column += dx[num]
    if 8>=temp_row >= 1 and 8>=temp_column >= 1:
       cnt += 1
print(cnt)