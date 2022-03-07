from dataclasses import dataclass
from typing import Any, Optional, Union

from node import NormalNode, TreeNode


@dataclass
class Stack:
    top: Optional[NormalNode] = None

    def insert(self, data: Any, **kwargs) -> None:
        """Insert data to stack

        Args:
            data (Any): data to be inserted
        """
        self.top = NormalNode(data, next_node=self.top)

    def pop(self) -> NormalNode:
        """Remove top element from stack

        Returns:
            NormalNode: the top node of stack
        """
        if self.top is None:
            return None
        removed = self.top
        self.top = self.top.next_node
        return removed

    @staticmethod
    def show_current_status(node: Union[TreeNode, NormalNode]) -> None:
        """Print the current status of the stack

        Args:
            node (Union[TreeNode, NormalNode]): current node
        """
        if node is not None:
            print(f"Node with data -> {node.data}")
            Stack.show_current_status(node.next_node)
