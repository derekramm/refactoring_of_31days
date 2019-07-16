class Person:
    # 重构：将公共属性提升到父类
    def __init__(self, name): self.name = name
class Student(Person): pass
class Teacher(Person): pass
if __name__ == '__main__':
    print(Student('小铭').__dict__)
    print(Teacher('大蜥蜴').__dict__)
