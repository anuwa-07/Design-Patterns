from SimpleFactory.pizza import Pizza


class ChickenPizza(Pizza):
    def __str__(self) -> str:
        return "This is Chicken Object!"

    def prepare(self) -> None:
        print("Chicken Pizza is going to Prepare!")

    def bake(self) -> None:
        print("Chicken Pizza is going to Bake!")

    def cut(self) -> None:
        print("Chicken Pizza is going to Cut!")

    def box(self) -> None:
        print("Chicken Pizza is going to Pack to a Box!")

