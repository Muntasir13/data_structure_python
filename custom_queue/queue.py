from dataclasses import dataclass
from typing import Any, Optional, Union

from node import NormalNode, TreeNode


@dataclass
class Queue:
    head_node: Optional[NormalNode] = None
    tail_node: Optional[NormalNode] = None

    def insert(self, data: Any, **kwargs):
        """Insert data to queue

        Args:
            data (Any): the data to be inserted
        """
        if self.tail_node is None and self.head_node is None:
            self.tail_node = self.head_node = NormalNode(data)
            return None

        self.tail_node.next_node = NormalNode(data)
        self.tail_node = self.tail_node.next_node
        return None

    def pop(self):
        """Remove last element from queue"""
        if self.head_node is None:
            return None
        removed = self.head_node
        self.head_node = self.head_node.next_node
        if self.head_node is None:
            self.tail_node = None
        return removed

    @staticmethod
    def show_current_status(node: Union[TreeNode, NormalNode]) -> None:
        """Print the current status of the linked list

        Args:
            node (Union[TreeNode, NormalNode]): current node
        """
        if node is not None:
            print(f"Node with data -> {node.data}")
            Queue.show_current_status(node.next_node)
