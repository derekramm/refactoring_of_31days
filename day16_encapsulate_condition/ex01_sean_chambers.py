#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

import datetime


# 封装条件
# 当代码中充斥着若干条件判断时，代码的真正意图会迷失于这些条件判断之中。
# 这时我喜欢将条件判断提取到一个易于读取的属性或方法(如果有参数)中。
# 重构之前的代码如下:


class RemoteControl:
    def __init__(self, name, created_year):
        self.name = name
        self.created_year = created_year
        self.functions = []

    def perform_cool_function(self, button_pressed):
        if all([len(self.functions), self.name == 'RCA', self.created_year > (datetime.date.today().year - 2)]):
            return 'do something'


# 重构之后，代码的可读性更强，意图更明显


class RemoteControl:
    def __init__(self, name, created_year):
        self.name = name
        self.created_year = created_year
        self.functions = []

    @property
    def has_extra_functions(self):
        return len(self.functions) and self.name == 'RCA' and self.created_year > (datetime.date.today().year - 2)

    def perform_cool_function(self, button_pressed):
        if self.has_extra_functions:
            return 'do something'
