class Person:pass
class Student(Person):
    # 问题：子类的姓名属性重复声明
    def __init__(self, name): self.name = name
class Teacher(Person):
    def __init__(self, name): self.name = name
if __name__ == '__main__':
    print(Student('小铭').__dict__)
    print(Teacher('大蜥蜴').__dict__)