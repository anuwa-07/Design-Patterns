"""
    Represent the Basic Game Character.
"""

from typing import Protocol


class GameCharacter(Protocol):
    def make_noise(self) -> None:
        """ let character to make noice """
        ...


