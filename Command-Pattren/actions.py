
from dataclasses import dataclass


@dataclass
class Light:
    name: str

    def light_turn_on(self) -> None:
        print(f"{self.name} Light is Turn On!")

    def light_turn_off(self) -> None:
        print(f"{self.name} Light is Turn Off!")

    def light_turn_dim_down(self) -> None:
        print(f"{self.name} Light is Turn to Dim-Down")

    def list_turn_dim_up(self) -> None:
        print(f"{self.name} Light is Turn Dim-Up")




