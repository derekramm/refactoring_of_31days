class Pet:
    # 问题：有的宠物不会游泳
    def swim(self): print(f'{self.__class__.__name__} is swimming')

    # 问题：有的宠物不会飞翔
    def fly(self): print(f'{self.__class__.__name__} is flying')

class Fish(Pet): pass

class Bird(Pet): pass

if __name__ == '__main__':
    Fish().swim()
    Bird().fly()
