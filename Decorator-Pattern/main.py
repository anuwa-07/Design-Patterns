
from coffee import Coffee, IceCoffee
from coffee_decorator import Chocolate

if __name__ == "__main__":
    ice_coffee: Coffee = IceCoffee()
    print(f"Ice coffee is: {ice_coffee.get_cost()} cost")
    print(f"Description: {ice_coffee.get_description()} \n")

    # Now we are adding flavors to coffee we order
    chocolate_ice_coffee = Chocolate(coffee=ice_coffee)
    print(f"Description: {chocolate_ice_coffee.get_description()}")
    print(f"Ice coffee is: {chocolate_ice_coffee.get_cost()} cost")


