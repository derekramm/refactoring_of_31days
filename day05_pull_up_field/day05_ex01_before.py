class Account: pass

class CheckingAccount(Account):
    # 问题代码
    def __init__(self): self.__minimum_checking_balance = 5.0

class SavingAccount(Account):
    # 问题代码
    def __init__(self): self.__minimum_checking_balance = 5.0

if __name__ == '__main__':
    print(CheckingAccount().__dict__)
    print(SavingAccount().__dict__)
