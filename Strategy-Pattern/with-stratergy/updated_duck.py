
from behaviours import FlyBehavior, SwimBehavior, EatBehavior
from behaviours import NoEat, NoFly, NoSwim, CanSwim, CanEat, MaxFly, MediumFly


class Duck:
    fb: FlyBehavior
    sw: SwimBehavior
    eb: EatBehavior

    def __init__(self, fb: FlyBehavior, sw: SwimBehavior, eb: EatBehavior):
        self.fb = fb
        self.sw = sw
        self.eb = eb

    def fly(self) -> None:
        self.fb.fly()

    def eat(self) -> None:
        self.eb.eat()

    def swim(self) -> None:
        self.sw.swim()


if __name__ == "__main__":
    rubber_duck: Duck = Duck(fb=NoFly(), sw=NoSwim(), eb=NoEat())
    rubber_duck.fly()
    rubber_duck.eat()
    rubber_duck.swim()



