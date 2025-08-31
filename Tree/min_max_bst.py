class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:   # Avoid duplicates
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)

    def find_max(self):
        # keep going right until there is no right child
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        # keep going left until there is no left child
        if self.left is None:
            return self.data
        return self.left.find_min()


def build_tree(elements):
    root = BinaryTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    binary_tree = build_tree(numbers)

    print("Max value :")
    print(binary_tree.find_max())

    print("Min value :")
    print(binary_tree.find_min())
      