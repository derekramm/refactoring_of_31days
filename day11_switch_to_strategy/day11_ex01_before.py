from enum import Enum, unique

class ShippingInfo:
    # 问题代码
    def calculate_shipping_amount(self, state):
        if state == State.Alaska: return self.get_alaska_shipping_amount()
        if state == State.NewYork: return self.get_newyork_shipping_amount()
        if state == State.Florida: return self.get_florida_shipping_amount()
        return 0.0

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
