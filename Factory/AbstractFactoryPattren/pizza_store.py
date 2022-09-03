

from abc import ABC, abstractmethod
from pizza import PizzaIngredientsFactory, NYPizzaIngredientFactory, CFPizzaIngredientFactory, CheesePizza, ChickenPizza


class Pizza:
    ...


class PizzaStore(ABC):
    pizza: Pizza

    def order_pizza(self, pizza_type: str) -> Pizza:
        self.pizza = self.create_pizza(pizza_type=pizza_type)
        self.pizza.prepare()
        self.pizza.bake()
        self.pizza.cut()
        self.pizza.box()

        return self.pizza

    @abstractmethod
    def create_pizza(self, pizza_type: str) -> Pizza:
        ...


class NYStylePizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Pizza:
        pizza: Pizza
        ingredient_factory: PizzaIngredientsFactory = NYPizzaIngredientFactory()
        if pizza_type == "cheese":
            self.pizza = CheesePizza(ingredient_factory=ingredient_factory)
        elif pizza_type == "veggie":
            self.pizza = NYStyleVeggie()  # TODO implement one
        else:
            self.pizza = ChickenPizza(ingredient_factory=ingredient_factory)
        #
        return self.pizza


class CaliforniaPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Pizza:
        pizza: Pizza
        ingredient_factory: PizzaIngredientsFactory = CFPizzaIngredientFactory()
        if pizza_type == "cheese":
            self.pizza = CheesePizza(ingredient_factory=ingredient_factory)
        elif pizza_type == "veggie":
            self.pizza = NYStyleVeggie()  # TODO implement one
        else:
            self.pizza = ChickenPizza(ingredient_factory=ingredient_factory)
        #
        return self.pizza




