class Account:
    # 重构
    def __init__(self): self.__minimum_checking_balance = 5.0

class CheckingAccount(Account): pass

class SavingAccount(Account): pass

if __name__ == '__main__':
    print(CheckingAccount().__dict__)
    print(SavingAccount().__dict__)
