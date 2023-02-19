import json
from game import Human, Elv, Wizard



def main():
    with open("./data.json") as file:
        data = json.load(file)

        for _character in data["characters"]:
            if _character["type"] == "Human":
                Human(name=_character["name"]).make_an_action()
            elif _character["type"] == "Els":
                Elv(name=_character["name"]).make_an_action()
            elif _character["type"] == "Wizard":
                Wizard(name=_character["name"]).make_an_action()


if __name__ == "__main__":
    main()


