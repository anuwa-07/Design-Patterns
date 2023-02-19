
import importlib


class PluginInterface:
    @staticmethod
    def initialize() -> None:
        """Initialize the Plugins"""


def import_module(name: str) -> PluginInterface:
    return importlib.import_module(name)  # type: ignore


def load_plugins(plugins: [str]) -> None:
    for plugin_name in plugins:
        plugin = import_module(plugin_name)
        plugin.initialize()

