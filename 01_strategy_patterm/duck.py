from abc import ABC
from fly_behavior import FlyBehavior, FlyWithWings, FlyNoWay
from quack_behavior import QuackBehavior, MuteQuack, Quack

class Duck(ABC):

    def __init__(
        self, 
        fly_behavior: FlyBehavior, 
        quack_behavior: QuackBehavior
    ) -> None:
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def perform_fly(self):
        self.fly_behavior.fly()
    
    def perform_quack(self):
        self.quack_behavior.quack()
    
    def set_fly_behavior(self, fly_behavior: FlyBehavior):
        self.fly_behavior = fly_behavior
    
    def set_quack_behavior(self, quack_behavior: QuackBehavior):
        self.quack_behavior = quack_behavior


class MallardDuck(Duck):

    def __init__(self) -> None:
        super().__init__(fly_behavior=FlyWithWings(), quack_behavior=Quack())


class RubberDuck(Duck):

    def __init__(self) -> None:
        super().__init__(fly_behavior=FlyNoWay(), quack_behavior=MuteQuack())
