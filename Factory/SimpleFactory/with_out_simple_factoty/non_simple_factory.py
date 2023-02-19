
from SimpleFactory.pizza import CheesePizza, ChickenPizza, PepperoniPizza, Pizza


class PizzaStore:
    def __init__(self) -> None:
        pass

    '''
        Here in this "order_pizza" method,
            - we create pizza instance by checking pizza type.
            - then we do the common operations on a pizza, ( prepare, bake etc ... )
        
        Issue is when a new pizza type need to add, 
            # We have to modify the PizzaStore class, which is going to expose to client side. 
            # Also here we keep codes which are going to change time to time and not required changes. 
                To avoid this: 
                We decouple logic and encapsulate those, So we can make changes on logics which are required 
                modifications time to time without affecting on solid code logics. 
    '''
    @staticmethod
    def order_pizza(pizza_type: str) -> Pizza:
        pizza: Pizza | None = None
        match pizza_type:
            case "cheese":
                pizza = CheesePizza()
            case "pepperoni":
                pizza = PepperoniPizza()
            case _:
                pizza = ChickenPizza()

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        #
        return pizza


if __name__ == "__main__":
    pizza_st = PizzaStore()
    cheese_pizza: Pizza = pizza_st.order_pizza("cheese")
    #
    print()
    print(cheese_pizza)


