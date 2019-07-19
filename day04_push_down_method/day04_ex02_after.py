class Animal: pass

class Dog(Animal):
    # 重构
    def bark(self): print(f'{self.__class__.__name__} is barking')

class Cat(Animal): pass

if __name__ == '__main__':
    Dog().bark()
