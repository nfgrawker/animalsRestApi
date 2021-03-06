from dataclasses import dataclass

import yaml

from utils.decorators import singleton

_CONFIG_FILE_LOCATION = "config.yaml"


@dataclass
class ConfigData:
    """Internal representation of the Config YAML that the delegate uses."""
    secret: str


@singleton
class Config:
    """Singleton that represents the Config YAML at runtime, with utility methods."""

    def __init__(self) -> None:
        """Ensure only one instance of this class will exist at a time."""
        pass

    @property
    def data(self) -> ConfigData:
        """Interprets the Config.yaml file for runtime reference."""

        with open(_CONFIG_FILE_LOCATION) as data:
            config = yaml.full_load(data)

        return ConfigData(**config)
