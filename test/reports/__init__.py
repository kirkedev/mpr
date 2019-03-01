from typing import Iterator
from mpr.api import Attributes
from .. import load_resource as load


def load_resource(name: str) -> Iterator[Attributes]:
    return load(f"reports/{name}")
