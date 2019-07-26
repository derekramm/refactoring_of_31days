#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex00_original_before.py"""


class Foo:

    def __init__(self):
        """定义了一个列表属性"""
        self.items = []

    def add(self, item):
        """
        定义了 add() 函数用来向列表中添加新的元素
        :param item: 要添加的元素
        :return:
        """
        self.items.append(item)


# 客户端
foo = Foo()
foo.add('a')  # 希望客户端的操作方式
print(foo.items)  # 输出列表中所有的元素

foo.items.append('b')  # 有安全隐患的操作方式，绕过自定义的 add() 函数
print(foo.items)  # 输出列表中所有的元素
