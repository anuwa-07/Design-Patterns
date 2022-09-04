
from abc import ABC, abstractmethod

"""

    Coffee class have two concrete subclasses,
        IceCoffee
        HotCoffee
    
    Here we need to add some favors to the coffee we make for customers, also with that we need to add extra cost.
    For that modifying already existing class will not be the solution. Because every time we need to change favors
    we have to change these concrete classes, that can introduce lot of bugs. 
    And also it break the: "Open-Close Design Principle".
    
    To do that we going to apply "THE DECORATOR" pattern.

"""


# Main class
class Coffee(ABC):
    @abstractmethod
    def get_description(self) -> str:
        ...

    @abstractmethod
    def get_cost(self) -> float:
        ...


# Concreate class 01
class IceCoffee(Coffee):
    def get_description(self) -> str:
        return f"Greate coffee for Hot day!"

    def get_cost(self) -> float:
        return 50.80


# Concreate class 02
class HotCoffee(Coffee):
    def get_description(self) -> str:
        return f"Good coffee for Cold morning!"

    def get_cost(self) -> float:
        return 30.09


