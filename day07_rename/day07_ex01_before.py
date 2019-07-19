class Person:
    # 问题代码
    def __init__(self, fn):
        self.fn = fn

    # 问题代码
    @staticmethod
    def clchrlypr(): return 0.0

if __name__ == '__main__':
    print(Person('小铭').fn, Person.clchrlypr())
