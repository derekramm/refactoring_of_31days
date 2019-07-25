#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex00_original_before.py"""

class Foo:
    def __init__(self): self.__items = []
    def get_items(self): return self.__items
    def add(self, item): self.__items.append(item)

# 客户端
foo = Foo()
foo.add('a')  # 希望客户端的操作方式
print(foo.get_items())
foo.get_items().append('b')  # 有安全隐患的操作方式
print(foo.get_items())
