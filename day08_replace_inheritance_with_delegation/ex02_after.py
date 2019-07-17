class Mobile:
    @staticmethod
    def play_music(): return '使用手机播放音乐'

# 重构：使用关联关系代替继承
class Person:
    def __init__(self, name, mobile): self.mobile, self.name = mobile, name

    def listen_music(self): print(f'{self.name} {self.mobile.play_music()}')

if __name__ == '__main__':
    Person('大蜥蜴', Mobile()).listen_music()
