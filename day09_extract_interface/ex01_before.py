class Swim:
    # 注意：多个类用到了swim函数，可以考虑提取到接口
    @staticmethod
    def swim(): return 'is swimming'

class Person:
    def __init__(self): self.swim = Swim()

    def play(self): print(self.__class__.__name__, self.swim.swim())

class Dog:
    def __init__(self): self.swim = Swim()

    def play(self): print(self.__class__.__name__, self.swim.swim())

if __name__ == '__main__':
    Person().play()
    Dog().play()
