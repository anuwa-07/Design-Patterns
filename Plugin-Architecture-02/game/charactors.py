
'''
    Here we define the main character class
'''

from abc import ABC, abstractmethod


class Character(ABC):
    @abstractmethod
    def make_an_action(self) -> None:
        ...


# Sub class will implement here
class Human(Character):
    def __init__(self, name: str):
        self.name = name

    def make_an_action(self) -> None:
        print(f"Im {self.name}, We are from Gondor !!")


class Elv(Character):
    def __init__(self, name: str) -> None:
        self.name = name

    def make_an_action(self) -> None:
        print(f"Im {self.name}, We are from Revendal !!")


class Wizard(Character):
    def __init__(self, name: str) -> None:
        self.name = name

    def make_an_action(self) -> None:
        print(f"Im {self.name}, We are from Izangard !!")




