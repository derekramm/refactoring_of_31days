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
        # 重构
        return OrderCalculator(self).calculate()

class OrderCalculator:
    def __init__(self, order):
        self.sub_total = 0
        self.orderline_items = order.orderline_items
        self.discounts = order.discounts
        self.tax = order.tax

    def calculate(self):
        self.calculate_sub_total()
        self.calculate_discounts()
        self.calculate_tax()
        return self.sub_total

    def calculate_sub_total(self):
        for item in self.orderline_items:
            self.sub_total += item.price

    def calculate_discounts(self):
        for discount in self.discounts:
            self.sub_total -= discount

    def calculate_tax(self):
        self.sub_total += self.sub_total * self.tax

if __name__ == '__main__':
    order = Order(0.05)
    order.orderline_items.append(OrderLineItem(100))
    order.orderline_items.append(OrderLineItem(200))
    order.orderline_items.append(OrderLineItem(300))
    order.discounts.extend([10, 20, 300])
    print(order.calculate())
