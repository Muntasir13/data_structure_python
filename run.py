from binary_search_tree.binary_search_tree import BinarySearchTree
from linked_list import LinkedList
from linked_list.linked_list_enum import LinkedListEnum


x = ["a", "b", "c", "d", "e", "f"]
ll = LinkedList()
tree = BinarySearchTree()

for char in x:
    # ll.insert(char, placement=LinkedListEnum.LAST_NODE)
    tree.insert(char)
# ll.show_current_status(ll.head_node)
tree.show_current_status(tree.root)
