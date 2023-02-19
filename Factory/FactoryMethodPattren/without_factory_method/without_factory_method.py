
# Import the Products
from FactoryMethodPattren.pizza import Pizza, CLStyleChickenPizza, CLStyleCheesePizza, CLStyleVeggiePizza, \
    NYStyleVeggiePizza, NYStyleCheesePizza, NYStyleChickenPizza


# Define the ProductStore Class.
class BadPizzaStore:
    def __init__(self) -> None:
        ...

    def __str__(self) -> str:
        return 'Badly Implemented Pizza Store Class'

    @staticmethod
    def create_pizza(style: str, pz_type: str) -> Pizza:
        pizza: Pizza | None = None
        # Logics which are required time to time changes
        if style == "newyork":
            match pz_type:
                case "cheese":
                    pizza = NYStyleCheesePizza()  # depend on other classes
                case "chicken":
                    pizza = NYStyleChickenPizza()  # depend on other classes
                case _:
                    pizza = NYStyleVeggiePizza()  # depend on other classes
        elif style == "california":
            match pz_type:
                case "cheese":
                    pizza = CLStyleCheesePizza()  # depend on other classes
                case "chicken":
                    pizza = CLStyleChickenPizza()  # depend on other classes
                case _:
                    pizza = CLStyleVeggiePizza()  # depend on other classes
        else:
            raise Exception("Invalid Pizza Type Defined!")

        # Code logics, not required time to time changes.
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        #
        return pizza
