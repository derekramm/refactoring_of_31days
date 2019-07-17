class Person:
    def __init__(self, age): self.age = age

class Park:
    def __init__(self, person): self.person = person

    # 重构：将get_discount函数移动到Park类中
    def sell_ticket(self): return 0.5 if any([self.person.age <= 6, self.person.age >= 60]) else 1

    # 重构：方法移动到Park类中，就可以直接调用内部的方法了
    def get_money(self, money): return self.sell_ticket() * money

if __name__ == '__main__':
    p1 = Person(18)
    p2 = Person(70)
    print(Park(p1).get_money(100))
    print(Park(p2).get_money(100))
