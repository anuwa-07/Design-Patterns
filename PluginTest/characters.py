

from abc import ABC, abstractmethod


class GameCharacters(ABC):
    @abstractmethod
    def make_noise(self) -> None:
        ...


class Human(GameCharacters):
    def __init__(self, name: str) -> None:
        self.name = name

    def make_noise(self) -> None:
        print(f"Hi Im {self.name} and Im a good fighter!")


class Elf(GameCharacters):
    def __init__(self, name: str) -> None:
        self.name = name

    def make_noise(self) -> None:
        print(f"Hy! Im {self.name}, and Im an Elf!")



