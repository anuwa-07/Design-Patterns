"""
    Here we define the Object for making req on Particular task or kind of actions.
"""
from command import ICommand, LightOnCommand, LightOffCommand, LightDimUpCommand, LightDimDownCommand
from actions import Light


class Remote:
    turn_on: ICommand
    turn_off: ICommand
    dim_up: ICommand
    dim_down: ICommand

    def __init__(self, turn_on: ICommand, turn_off: ICommand, dim_up: ICommand, dim_down: ICommand) -> None:
        self.turn_on = turn_on
        self.turn_off = turn_off
        self.dim_down = dim_down
        self.dim_up = dim_up

    def press_light_on(self) -> None:
        self.turn_on.execute()

    def press_undo_light_on(self) -> None:
        """
            Even this method doing the same thing by "self.press_light_off()" method. But it Not.
            In Our example it seems the same job. But this will use on Undo operations on prv tasks.
        :return: None
        """
        self.turn_on.un_execute()

    def press_light_off(self) -> None:
        self.turn_off.execute()

    def press_undo_light_off(self) -> None:
        """
            Even this method doing the same thing by "self.press_light_on()" method. But it Not.
            In Our example it seems the same job. But this will use on Undo operations on prv tasks.
        :return: None
        """
        self.turn_off.un_execute()

    def press_dim_down(self) -> None:
        self.dim_down.execute()

    def press_undo_dim_down(self) -> None:
        """
            Even this method doing the same thing by "self.press_dim_up()" method. But it Not.
            In Our example it seems the same job. But this will use on Undo operations on prv tasks.
        :return: None
        """
        self.dim_down.un_execute()

    def press_dim_up(self) -> None:
        self.dim_up.execute()

    def press_undo_dim_up(self) -> None:
        """
            Even this method doing the same thing by "self.press_dim_down()" method. But it Not.
            In Our example it seems the same job. But this will use on Undo operations on prv tasks.
        :return: None
        """
        self.dim_up.un_execute()


class MobilePhoneApp:
    def __str__(self) -> str:
        return "This will also use to handle req on actions ( Light ) on, off, dim-up & dim-down"


if __name__ == "__main__":
    light_01 = Light("Philips Hue Light")
    home_remote = Remote(
        turn_on=LightOnCommand(light=light_01),
        turn_off=LightOffCommand(light=light_01),
        dim_down=LightDimDownCommand(light=light_01),
        dim_up=LightDimUpCommand(light=light_01)
    )
    #
    home_remote.press_light_on()
    home_remote.press_light_off()
    home_remote.press_undo_dim_down()
    home_remote.press_dim_up()
