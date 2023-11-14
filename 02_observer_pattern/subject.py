from abc import ABC, abstractmethod
from observer import Observer

class Subject(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass
