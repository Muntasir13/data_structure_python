from binary_search_tree import BinarySearchTree
from custom_queue import Queue
from linked_list import LinkedList, LinkedListEnum
from stack import Stack

x = ["a", "b", "c", "d", "e", "f"]
# ll = LinkedList()
# tree = BinarySearchTree()
# queue = Queue()
stack = Stack()

for char in x:
    # ll.insert(char, placement=LinkedListEnum.LAST_NODE)
    # tree.insert(char)
    # queue.insert(char)
    stack.insert(char)

# ll.show_current_status(ll.head_node)
# tree.show_current_status(tree.root)
# queue.show_current_status(queue.head_node)
stack.show_current_status(stack.top)
