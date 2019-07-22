#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 使用策略类
# 今天的重构没有固定的形式，多年来我使用过不同的版本，并且我敢打赌不同的人也会有不同的版本。
# 该重构适用于这样的场景：switch 语句块很大，并且会随时引入新的判断条件。
# 这时，最好使用策略模式将每个条件封装到单独的类中。
# 实现策略模式的方式是很多的。
# 我在这里介绍的策略重构使用的是字典策略， 这么做的好处是调用者不必修改原来的代码。
from abc import ABCMeta, abstractmethod
from enum import Enum


class State(Enum):
    Alaska = 1
    NewYork = 2
    Florida = 3


class ShippingInfo:
    def calculate_shipping_amount(self, state):
        if state == State.Alaska:
            return self.get_alaska_shipping_amount()
        if state == State.NewYork:
            return self.get_newyork_shipping_amount()
        else:
            return self.get_florida_shipping_amount()

    @staticmethod
    def get_alaska_shipping_amount():
        return 15.0

    @staticmethod
    def get_newyork_shipping_amount():
        return 10.0

    @staticmethod
    def get_florida_shipping_amount():
        return 3.0


class ClientCode:
    @staticmethod
    def calculate_shipping():
        shipping_info = ShippingInfo()
        return shipping_info.calculate_shipping_amount(State.Alaska)


# 要应用该重构，需将每个测试条件至于单独的类中，这些类实现了一个共同的接口。
# 然后将枚举作为字典的键，这样就可以获取正确的实现，并执行其代码了。
# 以后如果希望添加新的条件，只需添加新的实现类， 并将其添加至 ShippingCalculations 字典中。
# 正如前面说过的，这不是实现策略模式的唯一方式。
# 我在这里将字体加粗显示，是因为肯定会有人在评论里指出这点，用你觉得好用的方法。
# 我用这种方式实现重构的好处是，不用修改客户端代码。
# 所有的修改都在 ShippingInfo 类内部。
# Jayme Davis 指出这种重构由于仍然需要在构造函数中进行绑定，所以只不过是增加了一些类而已，
# 但如果绑定 IShippingCalculation 的策略可以置于 IoC 中，带来的好处还是很多的，它可以使你更灵活地捆绑策略。

class State(Enum):
    Alaska = 1
    NewYork = 2
    Florida = 3


class ShippingInfo:
    def __init__(self):
        self.shipping_calculations = {
            State.Alaska: AlaskShippingCalculation(),
            State.NewYork: NewYorkShippingCalculation(),
            State.Florida: FloridaShippingCalculation(),
        }

    def calculate_shipping_amount(self, state):
        return self.shipping_calculations[state].calculate()


class IShippingCalculation(metaclass=ABCMeta):
    @abstractmethod
    def calculate(self): raise NotImplementedError()


class AlaskShippingCalculation(IShippingCalculation):
    def calculate(self): return 15.0


class NewYorkShippingCalculation(IShippingCalculation):
    def calculate(self): return 10.0


class FloridaShippingCalculation(IShippingCalculation):
    def calculate(self): return 5.0


class ClientCode:
    @staticmethod
    def calculate_shipping():
        shipping_info = ShippingInfo()
        return shipping_info.calculate_shipping_amount(State.Alaska)


# 为了使这个示例圆满，我们来看看在 ShippingInfo 构造函数中使用 Ninject 为 IoC 容器时如何进行绑定。
# 需要更改的地方很多，主要是将 state 的枚举放在策略内部，以及 Ninject 向构造函数传递一个 IShippingInfo 的 IEnumerable 泛型。
# 接下来我们使用策略类中的 state 属性创建字典，其余部分保持不变。

class State(Enum):
    Alaska = 1
    NewYork = 2
    Florida = 3


class IShippingInfo(metaclass=ABCMeta):
    @abstractmethod
    def calculate_shipping_amount(self, state): raise NotImplementedError()


class ShippingInfo(IShippingInfo):
    def __init__(self):
        self.shipping_calculations = {
            State.Alaska: AlaskShippingCalculation(),
            State.NewYork: NewYorkShippingCalculation(),
            State.Florida: FloridaShippingCalculation(),
        }

    def calculate_shipping_amount(self, state):
        return self.shipping_calculations[state].calculate()


class IShippingCalculation(metaclass=ABCMeta):
    @abstractmethod
    def calculate(self): raise NotImplementedError()


class AlaskShippingCalculation(IShippingCalculation):
    def calculate(self): return 15.0


class NewYorkShippingCalculation(IShippingCalculation):
    def calculate(self): return 10.0


class FloridaShippingCalculation(IShippingCalculation):
    def calculate(self): return 5.0


class ClientCode:
    def __init__(self, i_shippint_info):
        self.shipping_info = i_shippint_info

    def calculate_shipping(self, state):
        return self.shipping_info.calculate_shipping_amount(state)


if __name__ == '__main__':
    print(ClientCode(ShippingInfo()).calculate_shipping(State.Alaska))
    print(ClientCode(ShippingInfo()).calculate_shipping(State.NewYork))
    print(ClientCode(ShippingInfo()).calculate_shipping(State.Florida))
