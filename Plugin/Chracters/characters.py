
from abc import ABC, abstractmethod


class MainCharacter(ABC):
    @abstractmethod
    def make_an_action(self) -> None:
        ...


# Here we define the subclass
class Human(MainCharacter):
    def __init__(self, name: str) -> None:
        self.name = name

    def make_an_action(self) -> None:
        print(f"Hello! Im {self.name} and Im from Gondor")


class Elfs(MainCharacter):
    def __init__(self, name: str) -> None:
        self.name = name

    def make_an_action(self) -> None:
        print(f"Hello! Im {self.name} and Im from Revendal!")


class Hobbit(MainCharacter):
    def __init__(self, name: str) -> None:
        self.name = name

    def make_an_action(self) -> None:
        print(f"Hello! Im {self.name} and Im from Shaya!")