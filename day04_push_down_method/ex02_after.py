class Pet: pass
class Fish(Pet):
    # 重构：将游泳方法下降到 Fish 类中
    def swim(self): print(self.swim)
class Bird(Pet):
    # 重构：将飞翔方法下降到 Bird 类中
    def fly(self): print(self.fly)

if __name__ == '__main__':
    Fish().swim()
    Bird().fly()
