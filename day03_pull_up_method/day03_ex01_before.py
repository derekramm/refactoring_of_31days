from enum import Enum, unique

class Vehicle: pass

class Car(Vehicle):
    # 问题代码
    @staticmethod
    def turn(direction):
        print(f'Car turn {direction.name}')

class Motocycle(Vehicle):
    # 问题代码
    @staticmethod
    def turn(direction):
        print(f'Motocycle turn {direction.name}')

@unique
class Direction(Enum):
    LEFT = 1
    RIGHT = 2

if __name__ == '__main__':
    Car.turn(Direction.LEFT)
    Motocycle.turn(Direction.RIGHT)
