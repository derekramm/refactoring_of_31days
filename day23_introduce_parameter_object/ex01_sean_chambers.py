#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""


# 引入参数对象
# 该重构来自于 Fowler 的重构目录，参见这里。
# 有时当使用一个包含多个参数的方法时，由于参数过多会导致可读性严重下降，如:

def create(amount, student, courses, credits): pass


# 这时有必要新建一个类，负责携带方法的参数。
# 如果要增加更多的参数，只需为对参数对象增加其他的字段就可以了，代码显得更加灵活。
# 要注意，仅仅在方法的参数确实过多时才使用该重构，否则会使类的数量暴增，而这本应该越少越好。

class RegistrationContext:
    def __init__(self, amount, student, courses, credits):
        self.amount = amount
        self.student = student
        self.courses = courses
        self.credits = credits


class Registration:
    def create(self, registration_context): pass
