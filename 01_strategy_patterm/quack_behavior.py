from abc import ABC, abstractmethod


class QuackBehavior(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):

    def __init__(self) -> None:
        super().__init__()
    
    def quack(self):
        print("Quack!")


class MuteQuack(QuackBehavior):

    def __init__(self) -> None:
        super().__init__()
    
    def quack(self):
        print("...")
