"""
날짜 : 2021/08/12
이름 : 변진하
내용 : 파이썬 캡슐화 실습하기 교재 p217
"""

#파일 읽기
file1 = open('./Test1.txt','r')
line = file1.readline()

print(line)
file1.close()

file2 = open('./Test1.txt','r')
while True:
    line=file2.read()
    if not line:
        break
    print(line)
file2.close()

#파일 쓰기
file3 = open('./Test1.txt','w')
file3.write('안녕하세요.\n')
file3.write('반갑습니다.\n')
file3.write('감사합니다.\n')
file3.close()