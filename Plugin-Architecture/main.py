import json
from dataclasses import dataclass

from game import factory, loader

"""
    Here we define some inbuilt class, Think there are already exits in the code.
"""


@dataclass
class Sorcerer:
    name: str

    def make_a_noise(self) -> None:
        print(f"Im a Sorcerer. My name is: {self.name}")


@dataclass
class Wizard:
    name: str

    def make_a_noise(self) -> None:
        print(f"Im a Wizard, My name is: {self.name}")


@dataclass
class Witcher:
    name: str

    def make_a_noise(self) -> None:
        print(f"Im a Witcher, My name is: {self.name}")


def main() -> None:
    factory.register("sorcerer", Sorcerer)  # type: ignore
    factory.register("wizard", Wizard)  # type: ignore
    factory.register("witcher", Witcher)  # type: ignore

    with open("./level.json") as file:
        data = json.load(file)

        # load the plugins
        loader.load_plugins(data["plugins"])

        # create the characters
        characters = [factory.create_character(item) for item in data["characters"]]

        for character in characters:
            character.make_noise()


if __name__ == "__main__":
    main()



