from abc import ABC, abstractmethod


class FlyBehavior(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):

    def __init__(self) -> None:
        super().__init__()

    def fly(self):
        print("fly by wings!")


class FlyNoWay(FlyBehavior):

    def __init__(self) -> None:
        super().__init__()
    
    def fly(self):
        print("Can't fly...")
