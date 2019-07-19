class OrderLineItem:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self): return self.__price

class Order:
    def __init__(self, tax):
        self.orderline_items = []
        self.discounts = []
        self.tax = tax

    def calculate(self):
        # 问题代码
        sub_total = 0
        for item in self.orderline_items:
            sub_total += item.price
        for discount in self.discounts:
            sub_total -= discount
        tax = sub_total * self.tax
        grand_total = sub_total + tax
        return grand_total

if __name__ == '__main__':
    order = Order(0.05)
    order.orderline_items.append(OrderLineItem(100))
    order.orderline_items.append(OrderLineItem(200))
    order.orderline_items.append(OrderLineItem(300))
    order.discounts.extend([10, 20, 300])
    print(order.calculate())
