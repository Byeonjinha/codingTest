"""
날짜 : 2021/08/12
이름 : 변진하
내용 : 파이썬 캡슐화 실습하기 교재 p161
"""

from Ch06.sub1.Account import Account
kb = Account('국민은행', '', '', 10000)
kb.deposit(40000)
kb.withdraw(5000)
print(kb.balance)
#캡슐화(정보은익)을 적용해서 취약 코드 예방
# kb.__balance -= 1
kb.show()