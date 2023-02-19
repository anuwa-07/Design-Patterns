
from dataclasses import dataclass
from ..game import factory


@dataclass
class Bard:
    name: str

    def make_a_noice(self) -> None:
        print("Calling Bard!")

def initilize() -> None:
    factory.register("bard", Bard)  # type ignore


