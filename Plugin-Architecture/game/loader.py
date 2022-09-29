"""
    Loader will use to Load plugin from json and register with Factory class
"""
import importlib


# First we need to make an Interface for our plugins
class ModuleInterface:
    @staticmethod
    def register() -> None:
        """ Register needed item to the game character factory """


# Import the module using importlib
def import_modules(name: str) -> ModuleInterface:
    return importlib.import_module(name)  # type: ignore


# Load plugin and call the each plugins' register method, Which to the register with relevant factory
def load_plugins(plugins: list[str]) -> None:
    """ load the plugin define in plugin list """
    for plugin_file in plugins:
        plugin = import_modules(plugin_file)
        plugin.register()
