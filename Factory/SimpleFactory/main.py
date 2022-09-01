
from pizza import Pizza
from simple_pizza_factory import SimplePizzaFactory


class PizzaStore:
    factory: SimplePizzaFactory
    pizza: Pizza

    def __init__(self, factory: SimplePizzaFactory) -> None:
        self.factory = factory

    def order_pizza(self, pizza_type: str) -> Pizza:
        self.pizza = self.factory.create_pizza(pizza_type=pizza_type)
        self.pizza.prepare()
        self.pizza.bake()
        self.pizza.cut()
        self.pizza.box()

        return self.pizza


if __name__ == "__main__":
    pizza_factory = SimplePizzaFactory()
    pz = PizzaStore(factory=pizza_factory)
    my_pizza: Pizza = pz.order_pizza(pizza_type="cheese")

    print(my_pizza)
