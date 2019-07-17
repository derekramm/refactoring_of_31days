class Pet: pass

class Cat(Pet):
    # 问题：宠物都具备吃东西的方法，应该提升到父类 Pet 类中
    def eat(self): print(f'{self.__class__.__name__} is eating')

class Dog(Pet):
    # 问题：宠物都具备吃东西的方法，应该提升到父类 Pet 类中
    def eat(self): print(f'{self.__class__.__name__} is eating')

if __name__ == '__main__':
    Cat().eat()
    Dog().eat()
