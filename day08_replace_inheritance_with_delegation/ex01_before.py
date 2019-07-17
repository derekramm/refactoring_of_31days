class Mobile:
    @staticmethod
    def play_music(): return '使用手机播放音乐'

# 注意：Person类继承Mobile类不合理
class Person(Mobile):
    def __init__(self, name): self.name = name

    def listen_music(self): print(f'{self.name} {super().play_music()}')

if __name__ == '__main__':
    Person('大蜥蜴').listen_music()
