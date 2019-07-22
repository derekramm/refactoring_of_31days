#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""


# 合并继承
# 今天的重构来自于 Martin Fowler 的模式目录。你可以在他的目录中找到该重构。
# 昨天，我们通过提取子类来下放职责。
# 而今天，当我们意识到不再需要某个子类时，可以使用 Collapse Hierarchy 重构。
# 如果某个子类的属性(以及其他成员)可以被合并到基类中，这时再保留这个子类已经没有任何意义了。

class Website:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.pages = []


class StudentWebsite(Website):
    def __init__(self, is_active, title, description):
        super().__init__(title, description)
        self.is_active = is_active


# 这里的子类并没有过多的功能，只是表示站点是否激活。
# 这时我们会意识到判断站点是否激活的功能应该是通用的。
# 因此可以将子类的功能放回到 Website 中，并删除 StudentWebsite 类型。

class Website:
    def __init__(self, title, description, is_active):
        self.title = title
        self.description = description
        self.pages = []
        self.is_active = is_active
