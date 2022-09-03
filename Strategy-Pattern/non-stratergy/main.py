from duck import Duck, CityDuck

if __name__ == "__main__":
    duck: Duck = CityDuck(name="Piki")
    duck.fly()
    duck.swim()
    duck.eat()
    print(f"This duck name is: {duck.get_name()}")



