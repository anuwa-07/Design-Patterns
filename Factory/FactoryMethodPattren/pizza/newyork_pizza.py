
from .pizza import Pizza


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