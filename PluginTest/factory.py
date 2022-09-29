

from typing import Any, Callable
from .characters import GameCharacters


callable_func_dict: dict[str, Callable[..., GameCharacters]] = {}


def register_character(character_type: str, callable: Callable[..., GameCharacters]) -> None:
    callable_func_dict[character_type] = callable


def create_character(character_type: dict[str, Any]) -> GameCharacters:
    args_copy = character_type.copy()
    character_type = args_copy.pop("type")
    try:
        creator_func = callable_func_dict[character_type]
    except Exception as err:
        print(err)
#
    return creator_func(**args_copy)



