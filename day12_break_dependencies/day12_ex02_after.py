from abc import ABCMeta, abstractmethod

class Feeder:
    @staticmethod
    def replenish_food(): print('fill up bowl')

# 重构
class IFeederService(metaclass=ABCMeta):
    @abstractmethod
    def replenish_food(self): raise NotImplementedError()

# 重构
class FeederService(IFeederService):
    def replenish_food(self): Feeder.replenish_food()

class AnimalFeedingService:
    def __init__(self, foodbow_empty, i_feeder_service):
        self.i_feeder_service = i_feeder_service
        self.foodbow_empty = foodbow_empty

    def feed(self):
        if self.foodbow_empty:
            self.i_feeder_service.replenish_food()

if __name__ == '__main__':
    AnimalFeedingService(True, FeederService()).feed()
