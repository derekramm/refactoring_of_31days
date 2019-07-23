class Target:
    def show(self): return 'target'

class Proxy:
    def __init__(self):
        self.target = Target()
    def show(self):
        return self.target.show()

if __name__ == '__main__':
    print(Proxy().show())
