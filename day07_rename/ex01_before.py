# 注意：下面的代码取名很难理解，后期不利于程序的维护
class P:
    # 注意：下面的代码取名很难理解，后期不利于程序的维护
    def __init__(self, f, l): self.f, self.l = f, l

    # 注意：下面的代码取名很难理解，后期不利于程序的维护
    def gfn(self): return f'{self.f} {self.l}'

if __name__ == '__main__':
    print(P('大', '蜥蜴').gfn())
