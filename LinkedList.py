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


def insert_in_pos(linked, node):
    current = linked.head
    while current.next_node is not None:
        if node.value > current.next_node.value:
            temp = current.next_node
            current.next_node = node
            node.next_node = temp
            break
        current = current.next_node


if __name__ == "__main__":
    node1 = Node(1, None)
    node2 = Node(2, node1)
    node4 = Node(4, node2)
    node7 = Node(7, node4)

    linked_list = LinkedList(node7)
    print_linked_list(linked_list)

    print("")
    node3 = Node(3, None)
    insert_in_pos(linked_list, node3)
    print_linked_list(linked_list)
