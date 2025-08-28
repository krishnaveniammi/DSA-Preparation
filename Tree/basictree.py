class TreeNode:
    def __init__(self, data):
        self.data = data          # ✅ store the data
        self.children = []        # ✅ list to hold children nodes

    def add_child(self, childnode):
        self.children.append(childnode)

    def print_tree(self, level=0):
        # Print the node value with indentation based on level
        print(" " * level * 3 + str(self.data))
        for child in self.children:
            child.print_tree(level + 1)  # Recursive call for children


# Creating the tree
root = TreeNode("subburao")
child1 = TreeNode("sadhya")
child2 = TreeNode("swapna")

root.add_child(child1)
root.add_child(child2)

child1_1 = TreeNode("navya")
child1_2 = TreeNode("likku")
child1.add_child(child1_1)
child1.add_child(child1_2)

child2_1 = TreeNode("satwika")
child2_2 = TreeNode("sunny")
child2.add_child(child2_1)
child2.add_child(child2_2)

# Print the tree
print("Tree structure :")
root.print_tree()

          