class Account:
    def __init__(self, bank, id, name, balance):
        # 속성
        self._bank = bank
        self._id = id
        self._name = name
        self._balance = balance
    #기능
    def deposit(self, balance):
        self.balance = balance
    def withdraw(self, balance):
        self.balance = balance
    def show(self):
        print('---------------------------')
        print('은행명 : ', self._bank )
        print('계좌번호', self._id)
        print('입금주 : ', self._name )
        print('현재잔액 : ', self._balance)