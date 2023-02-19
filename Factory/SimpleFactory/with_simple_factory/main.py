
from SimpleFactory.pizza import Pizza
from SimpleFactory.with_simple_factory.simple_pizza_factory import SimplePizzaFactory


class PizzaStore:
    """
    Here in this new PizzaStore Class,
    In "order_pizza()"
        - We encapsulate code which are going to change time to time and which are not.

    By doing that,
    - When a modification required we do not need to open this class for a modification.
    - With decoupling codes, We can avoid more bugs on modifications,
    """

    factory: SimplePizzaFactory
    pizza: Pizza

    def __init__(self, factory: SimplePizzaFactory) -> None:
        # Here we initialize the factory instance which we are going to use for make pizza.
        self.factory = factory

    def order_pizza(self, pizza_type: str) -> Pizza:
        # Update order_pizza()
        self.pizza = self.factory.create_pizza(pizza_type=pizza_type)
        self.pizza.prepare()
        self.pizza.bake()
        self.pizza.cut()
        self.pizza.box()
        #
        return self.pizza


if __name__ == "__main__":
    pizza_factory = SimplePizzaFactory()
    pz = PizzaStore(factory=pizza_factory)
    my_pizza: Pizza = pz.order_pizza(pizza_type="cheese")

    print(my_pizza)
