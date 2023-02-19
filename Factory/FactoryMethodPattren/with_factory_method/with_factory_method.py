from abc import ABC, abstractmethod

# Import PRODUCTS
from FactoryMethodPattren.pizza import Pizza, NYStyleCheesePizza, NYStyleChickenPizza, NYStyleVeggiePizza, \
    CLStyleVeggiePizza, CLStyleCheesePizza, CLStyleChickenPizza


class PizzaStore(ABC):
    pizza: Pizza

    def order_pizza(self, pizza_type: str):
        self.pizza = self.create_pizza(pizza_type)

        self.pizza.prepare()
        self.pizza.bake()
        self.pizza.cut()
        self.pizza.box()

        return self.pizza

    # Factory method
    @abstractmethod
    def create_pizza(self, pizza_type) -> Pizza:
        ...


class NYPizzaStore(PizzaStore):
    # Implement the factory method
    def create_pizza(self, pizza_type) -> Pizza:
        if pizza_type == "cheese":
            return NYStyleCheesePizza()
        elif pizza_type == "veggie":
            return NYStyleVeggiePizza()
        else:
            return NYStyleChickenPizza()


class CaliforniaPizzaStore(PizzaStore):
    # Implement the factory method
    def create_pizza(self, pizza_type) -> Pizza:
        if pizza_type == "cheese":
            return CLStyleCheesePizza()
        elif pizza_type == "veggie":
            return CLStyleVeggiePizza()
        else:
            return CLStyleChickenPizza()
