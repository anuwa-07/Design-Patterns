
"""
    We simply use a factory method pattern for better code
"""
from typing import Callable, Any
from .characters import MainCharacter

dict_of_character_funcs: [str, Callable[..., MainCharacter]] = {}


def register(arg_key: str, callable_func: Callable[..., MainCharacter]) -> None:
    """ Here we store the relevant func """
    dict_of_character_funcs[arg_key] = callable_func


def unregister(arg_key: str) -> None:
    ...


def create(arg_dict: dict[str, Any]):
    args_copy = arg_dict.copy()
    character_type = args_copy.pop("type")

    try:
        creation_func = dict_of_character_funcs[character_type]
        return creation_func(**args_copy)
    except KeyError as err:
        raise ValueError(f"Invalid Character Type! {args_copy} ")







