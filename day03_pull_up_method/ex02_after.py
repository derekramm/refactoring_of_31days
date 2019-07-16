class Pet:
    # 重构：将吃东西的方法提升到父类 Pet 类中
    def eat(self): print(self.eat)
class Cat(Pet): pass
class Dog(Pet): pass
if __name__ == '__main__':
    Cat().eat()
    Dog().eat()
