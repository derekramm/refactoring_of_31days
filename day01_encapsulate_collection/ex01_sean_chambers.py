#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

"""封装集合

In certain scenarios it is beneficial to not expose a full collection to consumers of a class. 
在某些场景中，向类的使用者隐藏类中的完整集合是一个很好的做法

Some of these circumstances is when there is additional logic associated with adding/removing items from a collection.
比如对集合的 add/remove 操作中包含其他的相关逻辑时
 
Because of this reason, it is a good idea to only expose the collection as something you can iterate over without modifying the collection.
因此，以可迭代但不能直接在集合上进行操作的方式来暴露集合，是个不错的主意。
 
Let’s take a look at some code
我们来看代码
"""


class Order:
    """订单类"""

    def __init__(self):
        self.__ordertotal = 0  # 订单合计
        self.__orderlines = []  # 订单明细列表

    @property
    def orderlines(self):
        """
        只读属性
        :return: 只读订单明细列表
        """
        return tuple(self.__orderlines)  # 重点：将列表转换为元组

    @property
    def ordertotal(self):
        """
        只读属性
        :return: 订单合计
        """
        return self.__ordertotal

    def add_orderline(self, orderline):
        """
        添加订单明细，同时累加订单合计
        :param orderline: 订单明细
        :return:
        """
        self.__orderlines.append(orderline)
        self.__ordertotal += orderline.total

    def remove_orderline(self, orderline):
        """
        移除订单明细，同时扣除订单合计
        :param orderline: 订单明细
        :return:
        """
        if orderline in self.__orderlines:  # 如果订单明细在订单中
            self.__orderlines.remove(orderline)
        self.__ordertotal -= orderline.total


"""
As you can see, we have encapsulated the collection as to not expose the Add/Remove methods to consumers of this class. 
如上述代码，我们对集合进行了封装，没有将 add/remove 方法暴露给类的使用者

There is some other types in the .Net framework that will produce different behavior for encapsulating a collection
.Net框架中的其它一些类型将产生用于封装集合的不同行为
 
such as ReadOnlyCollection but they do have different caveats with each.
例如只读集合 ReadOnlyCollection，但是他们都有不同的注意事项

This is a very straightforward refactoring and one worth noting.
这是一个非常简单但是却极具价值的重构
 
Using this can ensure that consumers do not mis-use your collection and introduce bugs into the code.
可以确保用户不会误用你暴露的集合，避免代码中的一些 bug
"""
