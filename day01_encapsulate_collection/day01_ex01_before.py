class OrderLine:
    def __init__(self, total):
        self.__total = total

    @property
    def total(self): return self.__total

class Order:
    def __init__(self):
        self.__orderlines = []
        self.__ordertotal = 0

    @property
    def orderlines(self): return self.__orderlines

    @property
    def ordertotal(self): return self.__ordertotal

    def add_orderline(self, orderline):
        self.__orderlines.append(orderline)
        self.__ordertotal += orderline.total

    def remove_orderline(self, orderline):
        self.__orderlines.remove(orderline)
        self.__ordertotal -= orderline.total

if __name__ == '__main__':
    order = Order()
    order.add_orderline(OrderLine(100))
    order.add_orderline(OrderLine(100))
    print(order.ordertotal)

    # 问题代码
    order.orderlines.append(OrderLine(100))
    print(order.ordertotal)
