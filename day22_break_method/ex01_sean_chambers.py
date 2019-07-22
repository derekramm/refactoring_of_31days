#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""


# 分解方法
# 今天的重构没有任何出处。可能已经有其他人使用了相同的重构，只是名称不同罢了。
# 如果你知道谁的名字比 Break Method 更好，请转告我。
# 这个重构是一种元重构(meta-refactoring)，它只是不停地使用提取方法重构，直到将一个大的方法分解成若干个小的方法。
# 下面的例子有点做作，AcceptPayment 方法没有丰富的功能。
# 因此为了使其更接近真实场 景，我们只能假设该方法中包含了其他大量的辅助代码。
# 下面的 AcceptPayment 方法可以被划分为多个单独的方法。

class Customer:
    def deduct_from_account_balance(self, amount): pass


class Product:
    def __init__(self, price, available_discount):
        self.price = price
        self.available_discount = available_discount


class CashRegister:
    def __init__(self, tax=0.06):
        self.tax = tax

    def accept_payment(self, customer, products, payment):
        subtotal = 0
        for product in products:
            subtotal += product.price
        for product in products:
            subtotal -= product.available_discount
        grandtotal = subtotal * self.tax
        customer.deduct_from_account_balance(grandtotal)


# 如您所见，AcceptPayment 方法包含多个功能，可以被分解为多个子方法。因此我们多次使用提取方法重构， 结果如下:

class Customer:
    def deduct_from_account_balance(self, amount): pass


class Product:
    def __init__(self, price, available_discount):
        self.price = price
        self.available_discount = available_discount


class CashRegister:
    def __init__(self, tax=0.06):
        self.tax = tax
        self.products = []

    def accept_payment(self, customer, products, payment):
        subtotal = self.calculate_subtotal()
        subtotal = self.subtract_discount(subtotal)
        grandtotal = self.add_tax(subtotal)
        self.subtract_from_customer_balance(customer, grandtotal)

    def calculate_subtotal(self):
        subtotal = 0
        for product in self.products:
            subtotal += product.price
        return subtotal

    def subtract_discount(self, subtotal):
        for product in self.products:
            subtotal -= product.available_discount
        return subtotal

    def add_tax(self, subtotal):
        return subtotal * self.tax

    def subtract_from_customer_balance(self, customer, grandtotal):
        customer.deduct_from_account_balance(grandtotal)
