
from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def prepare(self) -> None:
        ...

    @abstractmethod
    def bake(self) -> None:
        ...

    @abstractmethod
    def cut(self) -> None:
        ...

    @abstractmethod
    def box(self) -> None:
        ...



