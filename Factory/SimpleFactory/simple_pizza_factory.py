
from pizza import Pizza, CheesePizza, PepperoniPizza


class SimplePizzaFactory:
    @staticmethod
    def create_pizza(pizza_type: str) -> Pizza:
        pizza: Pizza = None
        if pizza_type == "cheese":
            pizza = CheesePizza()
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza()

        return pizza

