class Receipt:
    def __init__(self):
        self.discounts = []
        self.itemtotals = []

    def calculate_grand_total(self):
        # 重构
        sub_total = self.calculate_item_total()
        sub_total = self.calculate_discount(sub_total)
        sub_total = self.calculate_tax(sub_total)
        return sub_total

    @staticmethod
    def calculate_tax(sub_total):
        tax = sub_total * 0.065
        sub_total += tax
        return sub_total

    def calculate_discount(self, sub_total):
        for discount in self.discounts:
            sub_total -= discount
        return sub_total

    def calculate_item_total(self):
        sub_total = 0
        for item_total in self.itemtotals:
            sub_total += item_total
        return sub_total

if __name__ == '__main__':
    receipt = Receipt()
    receipt.itemtotals = [1000, 2000, 3000]
    receipt.discounts = [100, 200, 300]
    print(receipt.calculate_grand_total())
