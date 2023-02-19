from typing import Callable, Any

from .character import GameCharacter

character_crate_func: dict[str, Callable[..., GameCharacter]] = {}


def register(character_type: str, creation_func: Callable[..., GameCharacter]):
    """ Register a new game character type"""
    character_crate_func[character_type] = creation_func


def un_register(character_type: str):
    character_crate_func.pop(character_type, None)


def create(arguments: dict[str, Any]) -> GameCharacter:
    args_copy = arguments.copy()
    character_type = args_copy.pop("type")

    try:
        creation_func = character_crate_func[character_type]
        return creation_func(**args_copy)
    except KeyError as err:
        raise ValueError("Invalid character type!")







