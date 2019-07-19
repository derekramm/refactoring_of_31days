class Animal:
    def bark(self): print(f'{self.__class__.__name__} is barking')

class Dog(Animal): pass

class Cat(Animal): pass

if __name__ == '__main__':
    Dog().bark()
    # 问题代码
    Cat().bark()
