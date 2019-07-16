class Pet:
    # 问题：有的宠物不会游泳
    def swim(self): print(self.swim)
    # 问题：有的宠物不会飞翔
    def fly(self): print(self.fly)
class Fish(Pet): pass
class Bird(Pet): pass

if __name__ == '__main__':
    Fish().swim()
    Bird().fly()
