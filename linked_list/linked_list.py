from dataclasses import dataclass
from typing import Any, Optional, Union

from node import NormalNode, TreeNode

from linked_list.linked_list_enum import LinkedListEnum


@dataclass
class LinkedList:
    head_node: Optional[NormalNode] = None
    last_node: Optional[NormalNode] = None  # * in order to keep track of the last node of linked list

    def insert(self, data: Any, **kwargs) -> None:
        """Insert data to linked list.

        Args:
            data (Any): the data to be inserted
            placement (LinkedListEnum, optional): the position where the node is to be created. placement can either be in
            head_node or last_node. Defaults to LinkedListEnum.HEAD_NODE.
        """
        if self.head_node is None:
            self.head_node = NormalNode(data, next_node=None)
            self.last_node = self.head_node
            return

        placement: LinkedListEnum = kwargs["placement"] if kwargs.get("placement") is not None else LinkedListEnum.HEAD_NODE
        if placement is LinkedListEnum.HEAD_NODE:
            self.head_node = NormalNode(data, self.head_node)
        elif placement is LinkedListEnum.LAST_NODE:
            self.last_node.next_node = NormalNode(data, None)
            self.last_node = self.last_node.next_node

    @staticmethod
    def show_current_status(node: Union[TreeNode, NormalNode]) -> None:
        """Print the current status of the linked list

        Args:
            node (Union[TreeNode, NormalNode]): current node
        """
        if node is not None:
            print(f"Node with data -> {node.data}")
            LinkedList.show_current_status(node=node.next_node)

    # * get_data is not implemented, as different use cases may have different types of data
