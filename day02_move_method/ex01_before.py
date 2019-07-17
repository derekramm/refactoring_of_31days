class Person:
    def __init__(self, age): self.age = age

    # 问题：该方法 Discount 类使用的更多，应该移动到 Discount 类中
    def get_discount(self): return 0.5 if any([self.age <= 6, self.age >= 60]) else 1

class Park:
    def __init__(self, person): self.person = person
    def sell_ticket(self, money): return self.person.sell_ticket() * money

if __name__ == '__main__':
    p1 = Person(18)
    p2 = Person(70)
    print(Park(p1).sell_ticket(100))
    print(Park(p2).sell_ticket(100))
