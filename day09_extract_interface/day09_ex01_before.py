class ClassRegistration:
    def create(self): print(f'{self.__class__.__name__} create')

    def transfer(self): pass

    def __init__(self, t): self.__total = t

    @property
    def total(self): return self.__total

class RegistrationProcessor:
    # 问题代码
    @staticmethod
    def process_registration(class_registration):
        class_registration.create()
        return class_registration.total

if __name__ == '__main__':
    total = RegistrationProcessor().process_registration(ClassRegistration(10))
    print(total)
