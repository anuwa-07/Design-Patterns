from abc import ABC, abstractmethod
from coffee import Coffee


class CoffeeDecorator(Coffee):
    @abstractmethod
    def get_description(self) -> str:
        ...

    @abstractmethod
    def get_cost(self) -> float:
        ...


# Here we define the flavors for coffee.
class Chocolate(CoffeeDecorator):
    coffee: Coffee

    def __init__(self, coffee: Coffee) -> None:
        self.coffee = coffee

    def get_description(self) -> str:
        return f"{self.coffee.get_description()} with adding Chocolate!"

    def get_cost(self) -> float:
        return self.coffee.get_cost() + 25.60


class Honey(CoffeeDecorator):
    coffee: Coffee

    def __init__(self, coffee: Coffee) -> None:
        self.coffee = coffee

    def get_description(self) -> str:
        return f"{self.coffee.get_description()} with adding Honey"

    def get_cost(self) -> float:
        return self.coffee.get_cost() + 30.09

