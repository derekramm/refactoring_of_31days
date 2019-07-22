#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 封装集合

"""
In certain scenarios it is beneficial to not expose a full collection to consumers of a class. 
Some of these circumstances is when there is additional logic associated with adding/removing items from a collection. 
Because of this reason, 
it is a good idea to only expose the collection as something you can iterate over without modifying the collection. 
Let’s take a look at some code
"""


# 在某些场景中，向类的使用者隐藏类中的完整集合是一个很好的做法，比如对集合的 add/remove 操作中包含其他的相关逻辑时。
# 因此，以可迭代但不直接在集合上进行操作的方式来暴露集合，是个不错的注意。
# 我们来看代码

class Order:
    def __init__(self):
        self.__ordertotal = 0
        self.__orderlines = []

    @property
    def orderlines(self):
        return tuple(self.__orderlines)

    @property
    def ordertotal(self):
        return self.__ordertotal

    def add_orderline(self, orderline):
        self.__orderlines.append(orderline)
        self.__ordertotal += orderline.total

    def remove_orderline(self, orderline):
        if orderline in self.__orderlines:
            self.__orderlines.remove(orderline)
        self.__orderlines.remove(orderline)
        self.__ordertotal -= orderline.total


"""
As you can see, we have encapsulated the collection as to not expose the Add/Remove methods to consumers of this class. 
There is some other types in the .Net framework that will produce different behavior for encapsulating a collection 
such as ReadOnlyCollection but they do have different caveats with each. 
This is a very straightforward refactoring and one worth noting. 
Using this can ensure that consumers do not mis-use your collection and introduce bugs into the code.
"""

# 如上述代码，我们对集合进行了封装，没有将 add/remove 方法暴露给类的使用者。
# 有些类，会由于封装集合而产生不同的行为，但他们各自都有防止误解的说明。
# 这是一个非常简单但是却极具价值的重构，可以确保用户不会误用你暴露的集合，避免代码中的一些 bug。
