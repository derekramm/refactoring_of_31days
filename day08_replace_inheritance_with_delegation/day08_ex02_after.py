class Sanitation:
    @staticmethod
    def wash_hands(): return 'hands cleaned'

# 重构
class Child:
    def __init__(self):
        self.sanitation = Sanitation()

    def wash_hands(self):
        print(self.sanitation.wash_hands())

if __name__ == '__main__':
    Child().wash_hands()
