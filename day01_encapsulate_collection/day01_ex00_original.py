class Product:
    def __init__(self, name):
        self.__name = name
        self.__items = []

    @property
    def name(self): return self.__name

    @property
    def items(self): return tuple(self.__items)

    def add(self, *item):
        self.__items.extend(item)
        return self


if __name__ == '__main__':
    p = Product('p').add(*'abc')
    print(p.name, p.items)
