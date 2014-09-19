class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def print_nodes(node):
    if node is not None:
        print(node.value)
        if node.left is not None:
            print(node.value + "-Left:")
            print_nodes(node.left)
        if node.right is not None:
            print(node.value + "-Right:")
            print_nodes(node.right)


def binary_search(node, value):
    if node.value == value:
        return True
    else:
        found = False
        if node.left is not None:
            found = binary_search(node.left, value)
        if not found and node.right is not None:
            found = binary_search(node.right, value)
        return found

if __name__ == "__main__":
    node1LeftRight = Node("node1leftright", None, None)
    node1Left = Node("node1left", None, node1LeftRight)

    node1RightLeft = Node("node1rightleft", None, None)
    node1Right = Node("node1right", node1RightLeft, None)

    node1 = Node("node1", node1Left, node1Right)

    print_nodes(node1)

    print(binary_search(node1, "node1rightleft"))