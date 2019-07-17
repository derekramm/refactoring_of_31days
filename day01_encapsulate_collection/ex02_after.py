class Employee:
    def __init__(self, salary): self.salary = salary

class Department:
    # 重构：属性私有
    def __init__(self): self.__employees, self.__total = [], 0

    def add(self, employee):
        self.__employees.append(employee)
        self.__total += employee.salary

    def remove(self, employee):
        self.__employees.remove(employee)
        self.__total -= employee.salary

    # 重构：封装列表，只提供只读功能
    @property
    def employees(self): return tuple(self.__employees)

    # 重构：封装属性，只提供只读功能
    @property
    def total(self): return self.__total

if __name__ == '__main__':
    dep = Department()

    dep.add(Employee(10000))
    print(f'员工人数：{len(dep.employees)}，薪资总和：{dep.total}')

    dep.add(Employee(10000))
    print(f'员工人数：{len(dep.employees)}，薪资总和：{dep.total}')
