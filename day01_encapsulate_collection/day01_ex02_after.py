class OrderLine:
    def __init__(self, name, price, count):
        self.__name = name
        self.__price = price
        self.__count = count
        self.__subtotal = self.__price * self.__count
    @property
    def subtotal(self): return self.__subtotal

class Order:
    def __init__(self):
        self.__orderlines = []
        self.__grandtotal = 0
    @property
    def orderlines(self): return tuple(self.__orderlines)
    @property
    def grandtotal(self): return self.__grandtotal
    def add_orderline(self, orderline):
        self.__orderlines.append(orderline)
        self.__grandtotal += orderline.subtotal
    def order_info(self):
        for orderline in self.orderlines: print(orderline.__dict__)
        print(f'商品记录：【{len(self.orderlines)}】条，价格合计：【{self.grandtotal}】')

if __name__ == '__main__':
    order = Order()
    order.add_orderline(OrderLine('苹果', 10, 5))
    order.add_orderline(OrderLine('西瓜', 25, 2))
    order.add_orderline(OrderLine('香蕉', 15, 6))
    order.order_info()
