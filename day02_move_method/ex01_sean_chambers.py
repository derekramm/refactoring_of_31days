#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 迁移方法

"""
The refactoring today is pretty straightforward, 
although often overlooked and ignored as being a worthwhile refactoring. 
Move method does exactly what it sounds like, move a method to a better location. 
Let’s look at the following code before our refactoring
"""


# 今天的重构同样非常简单，以至于人们并不认为这是一个有价值的重构。
# 迁移方法，顾名思义就是将方法迁移到合适的位置。
# 在开始重构前，我们先看一下代码

class BankAccount:
    def __init__(self, account_age, credit_score, account_interest):
        self.__account_age = account_age
        self.__credit_score = credit_score
        self.__account_interest = account_interest

    def calculate_interest_rate(self):
        if self.__credit_score > 800: return 0.02
        if self.__account_age > 10: return 0.03
        return 0.05


class AccountInterest:
    def __init__(self, bank_account):
        self.__bank_account = bank_account

    @property
    def interest_rate(self):
        return self.__bank_account.calculate_interest_rate()

    @property
    def introductory_rate(self):
        return self.__bank_account.calculate_interest_rate() < 0.05


"""
The point of interest here is the BankAccount.CalculateInterest method. 
A hint that you need the Move Method refactoring is when another class is using a method more often then the class in which it lives. 
If this is the case it makes sense to move the method to the class where it is primarily used. 
This doesn’t work in every instance because of dependencies, 
but it is overlooked often as a worthwhile change. 
In the end you would end up with something like this:
"""


# 这里指的注意的是 BankAccount.calculate_interest_rate 方法。
# 当一个方法被其他类使用比在它所在类中的使用还要频繁时，我们需要使用迁移方法重构-将方法迁移到更频繁使用它的类中。
# 由于依赖关系，该重构最终的代码应该是这样的

class BankAccount:
    def __init__(self, account_age, credit_score, account_interest):
        self.__account_age = account_age
        self.__credit_score = credit_score
        self.__account_interest = account_interest

    @property
    def account_age(self): return self.__account_age

    @property
    def credit_score(self): return self.credit_score


class AccountInterest:
    def __init__(self, bank_account):
        self.__bank_account = bank_account

    def calculate_interest_rate(self):
        if self.__bank_account.credit_score > 800: return 0.02
        if self.__bank_account.account_age > 10: return 0.03
        return 0.05

    @property
    def interest_rate(self):
        return self.calculate_interest_rate()

    @property
    def introductory_rate(self):
        return self.calculate_interest_rate() < 0.05
