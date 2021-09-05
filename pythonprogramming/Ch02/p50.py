"""
날짜 : 2021/08/09
이름 : 변진하
내용 : 파이썬 프로그래밍 50p
"""
oneLine = "this is one line string"
#(1) 왼쪽 기준
print(oneLine)
print("문자열 길이 : " , len(oneLine))
print(oneLine[0:4])
print(oneLine[:4])
print(oneLine[:])
print(oneLine[::2])

#(2) 오른쪽 기준
print(oneLine[0:-1:2])
print(oneLine[-6:-1])
print(oneLine[-6:])

#(3) 부분 문자열 생성
subString = oneLine[-11:]
print(subString)

