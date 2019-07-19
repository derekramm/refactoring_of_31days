class Receipt:
    def __init__(self):
        self.discounts = []
        self.itemtotals = []

    def calculate_grand_total(self):
        # 问题代码
        sub_total = 0
        for item_total in self.itemtotals:
            sub_total += item_total
        for discount in self.discounts:
            sub_total -= discount
        tax = sub_total * 0.065
        sub_total += tax
        return sub_total

if __name__ == '__main__':
    receipt = Receipt()
    receipt.itemtotals = [1000, 2000, 3000]
    receipt.discounts = [100, 200, 300]
    print(receipt.calculate_grand_total())
