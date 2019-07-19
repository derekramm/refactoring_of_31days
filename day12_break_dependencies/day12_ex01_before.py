class Feeder:
    # 问题代码
    @staticmethod
    def replenish_food(): print('fill up bowl')

class AnimalFeedingService:
    def __init__(self, foodbow_empty):
        self.foodbow_empty = foodbow_empty

    def feed(self):
        if self.foodbow_empty:
            Feeder.replenish_food()

if __name__ == '__main__':
    AnimalFeedingService(True).feed()
