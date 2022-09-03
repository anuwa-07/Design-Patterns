from abc import ABC, abstractmethod


# FlyBehavior ---------------------------------
class FlyBehavior(ABC):
    @abstractmethod
    def fly(self) -> None:
        ...


class NoFly(FlyBehavior):
    def fly(self) -> None:
        print("Will not able to Fly!")


class MaxFly(FlyBehavior):
    def fly(self) -> None:
        print("Will able to Fly Really fast: 70Kmh")


class MediumFly(FlyBehavior):
    def fly(self) -> None:
        print("Will able to fly in low speed: 20Kmh")


# SwimBehavior ---------------------------------
class SwimBehavior(ABC):
    @abstractmethod
    def swim(self) -> None:
        ...


class NoSwim(SwimBehavior):
    def swim(self) -> None:
        print("Will not able to swim!")


class CanSwim(SwimBehavior):
    def swim(self) -> None:
        print("Will able to swim in any place")


# EatBehavior ---------------------------------
class EatBehavior(ABC):
    @abstractmethod
    def eat(self) -> None:
        ...


class NoEat(EatBehavior):
    def eat(self) -> None:
        print("Will not able to eat any kind of a food!")


class CanEat(EatBehavior):
    def eat(self) -> None:
        print("Will able to any kind of a Food!")
