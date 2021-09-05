"""
날짜 : 2021/08/09
이름 : 변진하
내용 : 파이썬 프로그래밍 47p
"""

#(6) 외부 상수 인수
name = "홍길동"
age = 35
price = 125.456
print("이름:{},나이:{},data{}".format(name, age, price))
print("이름:{1},나이:{0},data={2}".format(age,name,price))

#(7) format 축양형(SQL문 작성)
uid = input ("id input:")
query = f"select*from member whyere uid = {uid}"
print(query) #member  테이블에서 uid가 hong인 레코드 검색