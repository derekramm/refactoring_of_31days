class Sanitation:
    @staticmethod
    def wash_hands(): return 'hands cleaned'

# 问题代码
class Child(Sanitation): pass

if __name__ == '__main__':
    print(Child.wash_hands())
