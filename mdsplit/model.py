from dataclasses import dataclass
from typing import Type


@dataclass
class Section:
    title: str
    content: str
    children: list[Type["Section"]]
