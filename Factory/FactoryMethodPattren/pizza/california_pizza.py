
from pizza import Pizza


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