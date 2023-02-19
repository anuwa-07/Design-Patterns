

from pizza import Pizza
from FactoryMethodPattren.with_factory_method.with_factory_method import PizzaStore, NYPizzaStore, CaliforniaPizzaStore

if __name__ == "__main__":
    ny_pizza: PizzaStore = NYPizzaStore()
    cl_pizza: PizzaStore = CaliforniaPizzaStore()

    pizza: Pizza = ny_pizza.order_pizza("cheese")
    print(f"Jone ordering: {pizza.get_name()}")

    pizza: Pizza = cl_pizza.order_pizza("veggie")
    print(f"Jenny ordering: {pizza.get_name()}")












