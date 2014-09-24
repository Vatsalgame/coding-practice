class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self, node):
        self.head = node


def print_linked_list(linked):
    current = linked.head
    while current is not None:
        print(str(current.value) + "->"),
        current = current.next_node


def sort_linked(linked):
    current = linked.head
    while current is not None:
        other = Node(current.next_node.value, current.next_node.next_node)
        while other is not None:
            if current.value > other.value:
                temp = Node(current.value, current.next_node)
                current.value = other.value
                current.next_node = other.next_node
                other.value = temp.value
                other.next_node = temp.next_node
            other = other.next_node
        current = current.next_node

if __name__ == "__main__":
    node1 = Node(1, None)
    node2 = Node(2, node1)
    node4 = Node(4, node2)
    node7 = Node(7, node4)

    linked_list = LinkedList(node7)
    print_linked_list(linked_list)

    print("")
    sort_linked(linked_list)
    print_linked_list(linked_list)
