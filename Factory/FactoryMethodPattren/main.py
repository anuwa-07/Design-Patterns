

from pizza import Pizza
from pizzastore import PizzaStore, NYPizzaStore, CaliforniaPizzaStore

if __name__ == "__main__":
    ny_pizza: Pizza = NYPizzaStore()
    cl_pizza: Pizza = CaliforniaPizzaStore()

    pizza: Pizza = ny_pizza.order_pizza("cheese")
    print(f"Jone ordering: {pizza.get_name()}")

    pizza: Pizza = cl_pizza.order_pizza("veggie")
    print(f"Jenny ordering: {pizza.get_name()}")












