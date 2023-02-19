
import json
from Chracters import Human, Hobbit, Elfs
from Chracters import register, create
from Chracters import load_plugins


def main():
    # Register the already having types
    register("human", Human)
    register("hobbit", Hobbit)
    register("elf", Elfs)

    with open("./data.json") as file:
        file_data = json.load(file)

        # Here we need to load the plugins
        load_plugins(file_data["plugins"])
        #
        characters = [create(item) for item in file_data["characters"]]
        for _character in characters:
            _character.make_an_action()


if __name__ == "__main__":
    main()




