"""Decorate functions."""
from typing import Callable


def singleton(cls: Callable) -> Callable:
    """Override all instantiations to return one instance per class."""
    instances = dict()

    def _singleton(*args: Tuple[Any], **kwargs: Dict[str, Callable]) -> Callable:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton
