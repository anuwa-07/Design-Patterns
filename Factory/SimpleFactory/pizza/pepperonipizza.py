from SimpleFactory.pizza import Pizza


class PepperoniPizza(Pizza):
    def prepare(self) -> None:
        print("Pepperoni Pizza is going to Prepare!")

    def bake(self) -> None:
        print("Pepperoni Pizza is going to Bake!")

    def cut(self) -> None:
        print("Pepperoni Pizza is going to Cut!")

    def box(self) -> None:
        print("Pepperoni Pizza is going to Pack to a Box!")

