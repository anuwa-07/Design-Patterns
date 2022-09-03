
from abc import ABC, abstractmethod


class Duck(ABC):
    name: str

    @abstractmethod
    def fly(self) -> None:
        ...

    @abstractmethod
    def eat(self) -> None:
        ...

    @abstractmethod
    def swim(self) -> None:
        ...

    def get_name(self) -> str:
        return self.name


# Define Wild Duck
class WildDuck(Duck):
    def __init__(self, name: str) -> None:
        self.name = name

    def fly(self) -> None:
        print("Wild duck can fly very far away!")
        print("Can fly speed of 60Kmh")

    def eat(self) -> None:
        print("Wild duck eat really lot in Summer!")

    def swim(self) -> None:
        print("Wild duck a swim very fast in any lake!")


# Define City Duck
class CityDuck(Duck):
    def __init__(self, name: str) -> None:
        self.name = name

    def fly(self) -> None:
        print("CityDuck can fly, But not far away!")

    def eat(self) -> None:
        print("City duck will eat only duck food in Supper Market!")

    def swim(self) -> None:
        print("City duck can swim in only swim pool!")


class RubberDuck(Duck):
    def __init__(self, name: str) -> None:
        self.name = name

    def fly(self) -> None:
        print("Rubber Duck will not able to Fly!")

    def eat(self) -> None:
        print("Rubber Duck is never Eat!")

    def swim(self) -> None:
        print("Rubber Duck can't Swim!")


class WoodDuck(Duck):
    def __init__(self, name: str) -> None:
        self.name = name

    def fly(self) -> None:
        print("Wood Duck will not able to Fly!")

    def eat(self) -> None:
        print("Wood Duck is never Eat!")

    def swim(self) -> None:
        print("Wood Duck can't Swim!")


class MountainDuck(Duck):
    def __init__(self, name: str) -> None:
        self.name = name

    def fly(self) -> None:
        print("Mountain duck can fly very far away!")
        print("Can fly speed of 60Kmh")

    def eat(self) -> None:
        print("Mountain duck eat really lot in Summer!")

    def swim(self) -> None:
        print("Mountain duck a swim very fast in any lake!")











