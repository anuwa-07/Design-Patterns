
from abc import ABC, abstractmethod


class PizzaIngredientsFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Douch:
        ...

    @abstractmethod
    def create_cheese(self) -> Cheese:
        ...

    @abstractmethod
    def create_pepperoni(self) -> Pepperoni:
        ...

    @abstractmethod
    def create_chicken(self) -> Chicken:
        ...


class NYPizzaIngredientFactory(PizzaIngredientsFactory):
    def create_cheese(self) -> Cheese:
        return ReggianoCheese()

    def create_dough(self) -> Douch:
        return ThinCrushDouch()

    def create_chicken(self) -> Chicken:
        return RosedChicken()

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()


class CFPizzaIngredientFactory(PizzaIngredientsFactory):
    def create_cheese(self) -> Cheese:
        return CFReggianoCheese()

    def create_dough(self) -> Douch:
        return CFThinCrushDouch()

    def create_chicken(self) -> Chicken:
        return CFRosedChicken()

    def create_pepperoni(self) -> Pepperoni:
        return CFSlicedPepperoni()


