
from abc import ABC, abstractmethod
from pizza_ingredients import PizzaIngredientsFactory, CFPizzaIngredientFactory, NYPizzaIngredientFactory


class Pizza(ABC):
    name: str
    sauce: str
    cheese: str
    chicken: str
    pepperoni: str

    @abstractmethod
    def prepare(self) -> None:
        ...

    def bake(self) -> None:
        print(f"{self.name} is now going to bake 25min in 50C")

    def cut(self) -> None:
        print(f"{self.name} is now cutting to 8 pieces")

    def box(self) -> None:
        print(f"{self.name} is Packing to handover!")


class CheesePizza(Pizza):
    ingredient_factory: PizzaIngredientsFactory

    def __init__(self, ingredient_factory: PizzaIngredientsFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print("Preparing " + self.name)
        self.sauce = self.ingredient_factory.create_dough()
        self.cheese = self.ingredient_factory.create_cheese()
        self.chicken = self.ingredient_factory.create_chicken()
        self.pepperoni = self.ingredient_factory.create_pepperoni()


class VeggiePizza(Pizza):
    ingredient_factory: PizzaIngredientsFactory

    def __init__(self, ingredient_factory: PizzaIngredientsFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print("Preparing " + self.name)
        self.sauce = self.ingredient_factory.create_dough()
        self.cheese = self.ingredient_factory.create_cheese()
        self.chicken = self.ingredient_factory.create_chicken()
        self.pepperoni = self.ingredient_factory.create_pepperoni()


class ChickenPizza(Pizza):
    ingredient_factory: PizzaIngredientsFactory

    def __init__(self, ingredient_factory: PizzaIngredientsFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print("Preparing " + self.name)
        self.sauce = self.ingredient_factory.create_dough()
        self.cheese = self.ingredient_factory.create_cheese()
        self.chicken = self.ingredient_factory.create_chicken()
        self.pepperoni = self.ingredient_factory.create_pepperoni()









