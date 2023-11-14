from abc import ABC, abstractmethod

class DisplayElement(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def display(self):
        pass
