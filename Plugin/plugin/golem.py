
from Chracters import MainCharacter
from Chracters import register


class Golem(MainCharacter):
    def __init__(self, name: str) -> None:
        self.name = name

    def make_an_action(self) -> None:
        print(f"Hi Im {self.name} and Im from the Dark Hills")


#
def initialize():
    register("golem", Golem)







