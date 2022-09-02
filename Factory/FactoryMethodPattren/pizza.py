
from abc import ABC


class Pizza(ABC):
    name: str
    dough: str
    sauce: str
    toppings: list = []

    def prepare(self) -> None:
        print(f"Preparing: {self.name}")
        print(f"Tossing dough...")
        print(f"Adding sauce....")
        print(f"Adding toppings...")
        for toppings in self.toppings:
            print(f"--- {toppings}")

    @staticmethod
    def bake() -> None:
        print("Bake for 25 minutes at 350")

    @staticmethod
    def cut() -> None:
        print("Cutting the Pizza in to 8 pieces")

    @staticmethod
    def box() -> None:
        print("Place pizza in official PizzaStore box")

    def get_name(self) -> str:
        return self.name


# Adding some concrete subclasses
class NYStyleCheesePizza(Pizza):
    def __init__(self) -> None:
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings = ["Grated Norwegian Cheese", "Honey", "Green Apple"]


class NYStyleVeggiePizza(Pizza):
    def __init__(self) -> None:
        self.name = "NY Style Vegetable Pizza!"
        self.dough = "Thick Crush Dough"
        self.sauce = "Tomato Sauce"
        self.toppings = ["Green chenille", "Banana with Honey", "Contents Milk"]

    @staticmethod
    def cut() -> None:
        print("Cutting the Veggie Pizza in to 4 pieces")


class NYStyleChickenPizza(Pizza):
    def __init__(self) -> None:
        self.name = "NY Style Chicken Pizza!"
        self.dough = "Fat Oil thick Crush Dough"
        self.sauce = "Garlic Sauce"
        self.toppings = ["Che-lee sauce", "Pumping", "Potatoes chips"]


class CLStyleCheesePizza(Pizza):
    def __init__(self) -> None:
        self.name = "California Style Sauce and Cheese Pizza"
        self.dough = "California Thin Crust Dough"
        self.sauce = "California Marinara Sauce"
        self.toppings = ["CL Grated Norwegian Cheese", "CL Honey", "CL Green Apple"]


class CLStyleVeggiePizza(Pizza):
    def __init__(self) -> None:
        self.name = "California Style Vegetable Pizza!"
        self.dough = "California Thick Crush Dough"
        self.sauce = "California Tomato Sauce"
        self.toppings = ["CL Green chenille", "CL Banana with Honey", "CL Contents Milk"]

    @staticmethod
    def cut() -> None:
        print("Cutting the California Veggie Pizza in to 6 pieces")


class CLStyleChickenPizza(Pizza):
    def __init__(self) -> None:
        self.name = "California Style Chicken Pizza!"
        self.dough = "California Fat Oil thick Crush Dough"
        self.sauce = "California Garlic Sauce"
        self.toppings = ["CL Che-lee sauce", "CL Pumping", "CL Potatoes chips"]



