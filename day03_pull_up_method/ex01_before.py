class Pet: pass
class Cat(Pet):
    # 问题：宠物都具备吃东西的方法，应该提升到父类 Pet 类中
    def eat(self): print(self.eat)
class Dog(Pet):
    def eat(self): print(self.eat)
if __name__ == '__main__':
    Cat().eat()
    Dog().eat()
