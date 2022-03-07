from custom_queue import Queue

from binary_search_tree.binary_search_tree import BinarySearchTree
from linked_list import LinkedList
from linked_list.linked_list_enum import LinkedListEnum

x = ["a", "b", "c", "d", "e", "f"]
# ll = LinkedList()
# tree = BinarySearchTree()
queue = Queue()

for char in x:
    # ll.insert(char, placement=LinkedListEnum.LAST_NODE)
    # tree.insert(char)
    queue.insert(char)
# ll.show_current_status(ll.head_node)
# tree.show_current_status(tree.root)
queue.show_current_status(queue.head_node)
