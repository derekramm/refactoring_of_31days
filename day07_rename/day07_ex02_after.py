class Person:
    # 重构
    def __init__(self, first_name):
        self.first_name = first_name

    # 重构
    @staticmethod
    def calculate_hourly_pay(): return 0.0

if __name__ == '__main__':
    print(Person('小铭').first_name, Person.calculate_hourly_pay())
