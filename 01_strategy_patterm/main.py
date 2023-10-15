from duck import MallardDuck, RubberDuck
from fly_behavior import FlyNoWay

if __name__ == "__main__":
    print("======= mallard duck =======")
    mallard_duck = MallardDuck()
    mallard_duck.perform_fly()
    mallard_duck.perform_quack()
    mallard_duck.set_fly_behavior(fly_behavior=FlyNoWay())
    mallard_duck.perform_fly()

    print("======= rubber duck =======")
    rubber_duck = RubberDuck()
    rubber_duck.perform_fly()
    rubber_duck.perform_quack()
