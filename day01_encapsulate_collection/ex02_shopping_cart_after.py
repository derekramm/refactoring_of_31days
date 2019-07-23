class OrderLine:
    def __init__(self, name, price, count):
        self.__name = name
        self.__price = price
        self.__count = count
        self.__subtotal = self.__price * self.__count

    def print_orderline(self):
        print(f'{self.__name}: {self.__price} * {self.__count} = {self.__subtotal}')

    @property
    def subtotal(self):
        return self.__subtotal


class Order:
    def __init__(self):
        self.__orderlines = []
        self.__grandtotal = 0

    @property
    def orderlines(self):
        return tuple(self.__orderlines)

    @property
    def grandtotal(self):
        return self.__grandtotal

    def add_orderline(self, orderline):
        self.__orderlines.append(orderline)
        self.__grandtotal += orderline.subtotal
        return self

    def remove_orderline(self, orderline):
        if orderline in self.__orderlines:
            self.__orderlines.remove(orderline)
            self.__grandtotal -= orderline.subtotal
        return self

    def print_orderlines(self):
        for orderline in self.__orderlines:
            orderline.print_orderline()
        print(f'商品总数：{len(self.__orderlines)}，订单合计：{self.__grandtotal}')
        print()


if __name__ == '__main__':
    order = Order()
    order.add_orderline(OrderLine('苹果', 10, 5))
    order.add_orderline(OrderLine('香蕉', 5, 4))
    order.add_orderline(OrderLine('橘子', 15, 10))
    order.print_orderlines()
    # 重构
    try:
        order.__orderlines.append(OrderLine('西瓜', 20, 5))  # 抛出异常：元组不允许修改
    except Exception as ex:
        print(ex)
    order.print_orderlines()
    # 重构
    order.__grandtotal = 0  # 修改无效
    order.print_orderlines()
