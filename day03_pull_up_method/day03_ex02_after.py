from enum import Enum, unique

class Vehicle:
    # 重构
    @classmethod
    def turn(cls, direction):
        print(f'{cls.__name__} turn {direction.name}')

class Car(Vehicle): pass

class Motocycle(Vehicle): pass

@unique
class Direction(Enum):
    LEFT = 1
    RIGHT = 2

if __name__ == '__main__':
    Car.turn(Direction.LEFT)
    Motocycle.turn(Direction.RIGHT)
