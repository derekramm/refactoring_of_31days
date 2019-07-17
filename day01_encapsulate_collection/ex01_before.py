class Employee:
    def __init__(self, salary): self.salary = salary

class Department:
    def __init__(self): self.employees, self.total = [], 0

    def add(self, employee):
        self.employees.append(employee)
        self.total += employee.salary

    def remove(self, employee):
        self.employees.remove(employee)
        self.total -= employee.salary

if __name__ == '__main__':
    dep = Department()
    dep.add(Employee(10000))
    dep.add(Employee(10000))
    print(f'员工人数：{len(dep.employees)}，薪资总和：{dep.total}')

    # 问题：用户绕过 add() 函数，直接利用 employees 属性添加员工
    dep.employees.append(Employee(20000))
    print(f'员工人数：{len(dep.employees)}，薪资总和：{dep.total}')

    # 问题：总支出属性不应该被外部直接修改，而是通过计算获取
    dep.total = 0
    print(f'员工人数：{len(dep.employees)}，薪资总和：{dep.total}')
