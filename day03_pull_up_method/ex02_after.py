class Pet:
    # 重构：将子类公共的方法提取到父类
    def eat(self): print(f'{self.__class__.__name__} is eating')

class Cat(Pet): pass

class Dog(Pet): pass

if __name__ == '__main__':
    Cat().eat()
    Dog().eat()
