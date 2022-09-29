
from characters import Human, Elf
import json


def main():
    with open("data.json") as file:
        data = json.load(file)
        print(data)


if __name__ == "__main__":
    main()





