import enum
import re
from typing import Iterable

HEADING_REGEX = r"^(?P<level>[#]+)\ (?P<text>.+)"


def split(lines: Iterable[str], depth: int=1, dir_leaves: bool=False) -> None:
    heading_pattern = re.compile(HEADING_REGEX)

    for line in lines:
        try:
            results = heading_pattern.match(line)
            level = len(results.group("level"))
            text = results.group("text")
            # print(f"{level = }")
            print("\t"*level, f"{text = }")
        
        except AttributeError:
            print("\t"*level, f"{line = }")
