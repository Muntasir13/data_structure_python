from dataclasses import dataclass
from typing import Any, Optional
from typing_extensions import Self


@dataclass
class Node:
    """The General Node Class"""
    data: Optional[Any] = None


@dataclass
class TreeNode(Node):
    left_node: Optional[Self] = None
    right_node: Optional[Self] = None


@dataclass
class NormalNode(Node):
    next_node: Optional[Self] = None
