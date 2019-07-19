# 重构
from abc import ABCMeta, abstractmethod

class IClassRegistration(metaclass=ABCMeta):
    @abstractmethod
    def create(self): raise NotImplementedError()

    def __init__(self, t): self._total = t

    @property
    def total(self): return self._total

class ClassRegistration(IClassRegistration):
    def create(self): print(f'{self.__class__.__name__} create')

    def transfer(self): pass

    @property
    def total(self): return self._total

class RegistrationProcessor:
    # 重构
    @staticmethod
    def process_registration(i_class_registration):
        i_class_registration.create()
        return i_class_registration.total

if __name__ == '__main__':
    total = RegistrationProcessor().process_registration(ClassRegistration(10))
    print(total)
