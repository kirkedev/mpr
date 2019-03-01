from typing import Iterator
from .. import load_resource as load
from mpr.api import Attributes


def load_resource(name: str) -> Iterator[Attributes]:
    return load(f"api/{name}")
