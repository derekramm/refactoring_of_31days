class Task:
    # 问题代码
    def __init__(self): self._resolution = self.__class__.__name__

class BugTask(Task): pass

class FeatureTask(Task): pass

if __name__ == '__main__':
    print(BugTask().__dict__)
    print(FeatureTask().__dict__)
