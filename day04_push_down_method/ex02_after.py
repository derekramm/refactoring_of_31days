class Pet: pass

class Fish(Pet):
    # 重构：将swim方法下降到Fish子类
    def swim(self): print(f'{self.__class__.__name__} is swimming')

class Bird(Pet):
    # 重构：将fly方法下降到Bird子类
    def fly(self): print(f'{self.__class__.__name__} is flying')

if __name__ == '__main__':
    Fish().swim()
    Bird().fly()
