class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        contain = value
        while temp is not None:
            if contain < temp.value:
                temp = temp.left
            elif contain > temp.value:
                temp = temp.right
            else:
                return True
        return False


binary_search_tree = BinarySearchTree()
binary_search_tree.insert(47)
binary_search_tree.insert(21)
binary_search_tree.insert(76)
binary_search_tree.insert(18)
binary_search_tree.insert(27)
binary_search_tree.insert(52)
binary_search_tree.insert(82)
print(binary_search_tree.contains(18))
print(binary_search_tree.contains(11))
