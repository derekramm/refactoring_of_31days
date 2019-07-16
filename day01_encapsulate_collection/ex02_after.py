class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Company:
    def __init__(self):
        self.__employees = []
        self.__total = 0
    def add(self, employee):
        self.__employees.append(employee)
        self.__total += employee.salary
    def remove(self, employee):
        self.__employees.remove(employee)
        self.__total -= employee.salary
    @property
    def total(self): return self.__total
    @property
    def employees(self): return tuple(self.__employees)
if __name__ == '__main__':
    company = Company()
    company.add(Employee('小铭', 10000.))
    company.add(Employee('大蜥蜴', 10000.))
    print(f'总支出：{company.total}')

    try:
        # 问题：用户绕过 add() 函数，直接利用 employees 属性添加员工
        # 重构：元组不允许修改，避免了从外部无规则添加员工的操作
        company.employees.append(Employee('米沙', 20000.))
    except Exception as ex:
        print(ex)
    print(f'总支出：{company.total}')

    # 问题：总支出属性不应该被外部直接修改，而是通过计算获取
    # 重构：将 total 属性私有，提供只读属性
    company.__total = 0  # 此时的属性和私有属性不是一个，不影响
    print(f'总支出：{company.total}')
