class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    # 重构：将工作经验属性下降到老师类
    def __init__(self, name, work_exp):
        super().__init__(name)
        self.work_exp = work_exp

class Student(Person):
    # 重构：将成绩属性下降到学生类
    def __init__(self, name, score):
        super().__init__(name)
        self.score = score

if __name__ == '__main__':
    t = Teacher('大蜥蜴', '3年')
    s = Student('小铭', 100)
    print(t.__dict__)
    print(s.__dict__)
