from dataclasses import dataclass
from typing import Any, Optional, Union

from node import TreeNode, NormalNode


@dataclass
class BinarySearchTree:
    root: Optional[TreeNode] = None

    def insert(self, data: Any, **kwargs) -> None:
        """Insert data to binary search tree

        Args:
            data (Any): the data to be inserted
            node (Optional[TreeNode], optional): the node in which the data is to be inserted. Defaults to None.
        """
        if self.root is None:
            self.root = TreeNode(data)
            return None

        node: Optional[TreeNode] = kwargs["node"] if kwargs.get("node") is not None else self.root
        if data < node.data:
            if node.left_node is None:
                node.left_node = TreeNode(data)
            else:
                self.insert(data, node=node.left_node)
        elif data > node.data:
            if node.right_node is None:
                node.right_node = TreeNode(data)
            else:
                self.insert(data, node=node.right_node)
        else:
            return None

    @staticmethod
    def show_current_status(node: Union[TreeNode, NormalNode]) -> None:
        """Print the current status of the linked list

        Args:
            node (Union[TreeNode, NormalNode]): current node
        """
        if node is not None:
            BinarySearchTree.show_current_status(node.left_node)
            print(f"Node with data -> {node.data}")
            BinarySearchTree.show_current_status(node.right_node)
