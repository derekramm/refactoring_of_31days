class Person:
    def __init__(self, name, score, work_exp):
        self.name = name
        # 问题：Teacher 类没有成绩属性
        self.score = score
        # 问题：Student 类没有工作经验属性
        self.work_exp = work_exp

class Teacher(Person): pass

class Student(Person): pass

if __name__ == '__main__':
    t = Teacher('大蜥蜴', None, '3年')
    s = Student('小铭', 1, None)
    print(t.__dict__)
    print(s.__dict__)
