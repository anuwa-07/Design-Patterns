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

