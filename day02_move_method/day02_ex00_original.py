class A: pass


class B:
    def request(self): return self.request

    def handle(self): print(self.request())


if __name__ == '__main__':
    B().handle()
