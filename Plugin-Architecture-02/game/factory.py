
from typing import Callable, Any
from .charactors import Character

character_create_func: dict[str, Callable[..., Character]] = {}


def register(character_type: str, create_func: Callable[..., Character]) -> None:
    character_create_func[character_type] = create_func


def create(arguments: dict[str, Any]) -> Character:
    ...




