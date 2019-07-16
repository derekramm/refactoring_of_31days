class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Company:
    def __init__(self):
        self.employees = []
        self.total = 0
    def add(self, employee):
        self.employees.append(employee)
        self.total += employee.salary
    def remove(self, employee):
        self.employees.remove(employee)
        self.total -= employee.salary
if __name__ == '__main__':
    company = Company()
    company.add(Employee('小铭', 10000.))
    company.add(Employee('大蜥蜴', 10000.))
    print(f'总支出：{company.total}')
    # 问题：用户绕过 add() 函数，直接利用 employees 属性添加员工
    company.employees.append(Employee('米沙', 20000.))
    print(f'总支出：{company.total}')
    # 问题：总支出属性不应该被外部直接修改，而是通过计算获取
    company.total = 0
    print(f'总支出：{company.total}')
