class BankAccount:
    def __init__(self, account_age, credit_score):
        self.__account_age = account_age
        self.__credit_score = credit_score

    @property
    def account_age(self):
        return self.__account_age

    @property
    def credit_score(self):
        return self.__credit_score

    # 问题代码
    def calculate_interest_rate(self):
        if self.credit_score > 800: return 0.02
        if self.account_age > 10: return 0.03
        return 0.05

class AccountInterest:
    def __init__(self, bank_account):
        self.__bank_account = bank_account

    def interest_rate(self):
        return self.__bank_account.calculate_interest_rate()

    def introductory_rate(self):
        return self.__bank_account.calculate_interest_rate() < 0.05

if __name__ == '__main__':
    account = BankAccount(12, 800)
    account_interest = AccountInterest(account)
    print(account_interest.interest_rate())
    print(account_interest.introductory_rate())
