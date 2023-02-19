
from SimpleFactory.pizza import Pizza


class CheesePizza(Pizza):
    def __str__(self) -> str:
        return "This is CheesePizza Object!"

    def prepare(self) -> None:
        print("Cheese Pizza is going to Prepare!")

    def bake(self) -> None:
        print("Cheese Pizza is going to Bake!")

    def cut(self) -> None:
        print("Cheese Pizza is going to Cut!")

    def box(self) -> None:
        print("Cheese Pizza is going to Pack to a Box!")

