class OrderLine:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        self.subtotal = self.price * self.count

class Order:
    def __init__(self):
        self.orderlines = []
        self.grandtotal = 0
    def add_orderline(self, orderline):
        self.orderlines.append(orderline)
        self.grandtotal += orderline.subtotal
    def order_info(self):
        for orderline in self.orderlines: print(orderline.__dict__)
        print(f'商品记录：【{len(self.orderlines)}】条，价格合计：【{self.grandtotal}】')

if __name__ == '__main__':
    order = Order()
    order.add_orderline(OrderLine('苹果', 10, 5))
    order.add_orderline(OrderLine('西瓜', 25, 2))
    order.add_orderline(OrderLine('香蕉', 15, 6))
    order.order_info()
    # 问题
    order.orderlines.append(OrderLine('葡萄', 50, 5))
    order.order_info()
    # 问题
    order.grandtotal = -100
    order.order_info()
