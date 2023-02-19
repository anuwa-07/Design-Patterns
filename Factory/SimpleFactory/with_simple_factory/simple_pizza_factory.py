
from SimpleFactory.pizza import Pizza, CheesePizza, PepperoniPizza, ChickenPizza


class SimplePizzaFactory:
    @staticmethod
    def create_pizza(pizza_type: str) -> Pizza:
        """
        This Static method will work as a factory for generating pizza by checking required type.
        Even this will change time to time, This class will not directly use for client.

        :param pizza_type: Type of the pizza
        :return: Pizza type object.
        """
        pizza: Pizza | None = None
        match pizza_type:
            case "cheese":
                pizza = CheesePizza()
            case "pepperoni":
                pizza = PepperoniPizza()
            case _:
                pizza = ChickenPizza()
        #
        return pizza
