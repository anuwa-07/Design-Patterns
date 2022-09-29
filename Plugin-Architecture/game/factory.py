"""
    Factory, Use to create object
"""
from typing import Any, Callable
from charactor import GameCharacter

character_creation_functions: dict[str, Callable[..., GameCharacter]]


def register(character_type: str, creator_func: Callable[..., GameCharacter]) -> None:
    """Register new game character type """
    character_creation_functions[character_type] = creator_func


def un_register(character_type: str) -> None:
    """ Unregister func from the list"""
    character_creation_functions.pop(character_type, None)


def create_character(arguments: dict[str, Any]) -> GameCharacter:
    """ Create a game character from a specific type """
    args_copy = arguments.copy()
    character_type = args_copy.pop("type")
    try:
        creator_func = character_creation_functions[character_type]
    except Exception as err:
        print(err)
    #
    return creator_func(**args_copy)

