from enum import Enum, unique
from abc import ABCMeta, abstractmethod

class IShippingInfo(metaclass=ABCMeta):
    @abstractmethod
    def calculate_shipping_amount(self, state): raise NotImplementedError()

class ShippingInfo(IShippingInfo):
    # 重构
    def __init__(self):
        self.shipping_calculations = {
            State.Alaska: ShippingInfo.get_alaska_shipping_amount,
            State.NewYork: ShippingInfo.get_newyork_shipping_amount,
            State.Florida: ShippingInfo.get_florida_shipping_amount
        }

    def calculate_shipping_amount(self, state):
        return self.shipping_calculations[state]()

    @staticmethod
    def get_alaska_shipping_amount():
        return 15.0

    @staticmethod
    def get_newyork_shipping_amount():
        return 10.0

    @staticmethod
    def get_florida_shipping_amount():
        return 5.0

@unique
class State(Enum):
    Alaska = 1,
    NewYork = 2,
    Florida = 3

class ClientCode:
    @staticmethod
    def calculate_shipping(state):
        shipping_info = ShippingInfo()
        return shipping_info.calculate_shipping_amount(state)

if __name__ == '__main__':
    print(ClientCode.calculate_shipping(State.Alaska))
    print(ClientCode.calculate_shipping(State.NewYork))
    print(ClientCode.calculate_shipping(State.Florida))
