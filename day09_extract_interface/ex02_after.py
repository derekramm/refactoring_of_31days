from abc import ABCMeta, abstractmethod

# 重构：提取接口
class ISwim(metaclass=ABCMeta):
    @abstractmethod
    def swim(self): raise NotImplementedError()

# 重构：实现接口的子类Swim发生变化，不会影响Person类和Dog类
class Swim(ISwim):
    def swim(self): return 'is swimming'

class Person:
    def __init__(self, iswim): self.sport = iswim

    def play(self): print(self.__class__.__name__, self.sport.swim())

class Dog:
    def __init__(self, iswim): self.sport = iswim

    def play(self): print(self.__class__.__name__, self.sport.swim())

if __name__ == '__main__':
    Person(Swim()).play()
    Dog(Swim()).play()
