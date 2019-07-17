# 重构：为类、方法、参数等取名要求见名知意
class Person:
    # 重构：为类、方法、参数等取名要求见名知意
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self): return f'{self.first_name} {self.last_name}'

if __name__ == '__main__':
    print(Person('小', '铭').get_full_name())
