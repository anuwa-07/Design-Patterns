
from abc import ABC, abstractmethod
from actions import Light


class ICommand(ABC):

    @abstractmethod
    def execute(self) -> None:
        ...

    @abstractmethod
    def un_execute(self) -> None:
        ...


"""
    Here we make Real Invokers, 
    What invokers do is they calling on some actions of a particular thing. In this example it is a Simple Light
"""


class LightOnCommand(ICommand):
    light: Light  # we need to keep a reference for light

    def __init__(self, light: Light) -> None:
        self.light = light

    def __str__(self) -> str:
        return "For Turn On the Light!"

    def execute(self) -> None:
        self.light.light_turn_on()

    def un_execute(self) -> None:
        self.light.light_turn_off()


class LightOffCommand(ICommand):
    light: Light

    def __init__(self, light: Light) -> None:
        self.light = light

    def __str__(self) -> str:
        return "For Turn Off the Light!"

    def execute(self) -> None:
        self.light.light_turn_off()

    def un_execute(self) -> None:
        self.light.light_turn_on()


class LightDimUpCommand(ICommand):
    light: Light

    def __init__(self, light: Light):
        self.light = light

    def __str__(self) -> str:
        return "For Dim-Up the Light!"

    def execute(self) -> None:
        self.light.list_turn_dim_up()

    def un_execute(self) -> None:
        self.light.light_turn_dim_down()


class LightDimDownCommand(ICommand):
    light: Light

    def __init__(self, light: Light) -> None:
        self.light = light

    def __str__(self) -> str:
        return "For Dim-Down the Light!"

    def execute(self) -> None:
        self.light.light_turn_dim_down()

    def un_execute(self) -> None:
        self.light.list_turn_dim_up()

