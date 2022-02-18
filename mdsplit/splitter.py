from dataclasses import dataclass, field
import re
from typing import Iterable

HEADING_REGEX = r"^(?P<level>[#]+)\ (?P<text>.+)"


@dataclass(order=True)
class Node:
    """Node of document structure tree"""

    value: int
    text: str = field(compare=False)
    children: list["Node"] = field(compare=False, init=False,
                                   default_factory=list)

    def __str__(self) -> str:
        return self.text


def split(lines: Iterable[str], depth: int=1, dir_leaves: bool=False) -> None:
    """Create a tree structure from `lines` up to `depth`."""

    heading_pattern = re.compile(HEADING_REGEX)
    
    # Lexing
    nodes = []
    for line in lines:
        try:
            results = heading_pattern.match(line)
            level = len(results.group("level"))
            text = results.group("text")
            nodes.append(Node(level, text))
        
        except AttributeError:
            pass
            # tokens.append(("content", 0, line))

    # Parsing
    root = Node(0, "root")
    stack = [root]
    for node in nodes:
        while node <= stack[-1]:
            stack.pop()
        
        stack[-1].children.append(node)

        if node > stack[-1]:
            stack.append(node)

    print_tree(root)
    

def print_tree(root: Node, depth=0):
    """Given the `root` of a linked tree, prints the document structure tree"""

    if not root.children:
        return

    for child in root.children:
        print("  "*depth, child)
        print_tree(child, depth+1)
