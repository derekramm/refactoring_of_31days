class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Discount:
    def __init__(self, person): self.__person = person
    def get_money(self, money): return self.get_discount() * money

    # 问题：该方法 Discount 类使用的更多，应该移动到 Discount 类中
    # 重构：将方法移动到 Discount 类中
    def get_discount(self):
        return 0.5 if any([self.__person.age <= 6, self.__person.age >= 60]) else 1

if __name__ == '__main__':
    p1 = Person('小铭', 18)
    p2 = Person('大蜥蜴', 70)
    print(Discount(p1).get_money(1000))
    print(Discount(p2).get_money(1000))
