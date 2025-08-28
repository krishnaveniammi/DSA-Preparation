class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self , data):
        if data == self.data:
            return 
        if data <self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)
    def inorder_traversal(self):
        elements =[]
        if self.left: # check if left child exists
            elements += self.left.inorder_traversal()
        elements.append(self.data) # visit base node
        
        if self.right: # check if right child exists
            elements += self.right.inorder_traversal()
        return elements
    def preorder_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preorder_traversal()
        if self.right:
            elements += self.right.preorder_traversal()
        return elements
    def search(self,val):
        if self.data == val:
            return True
        if val < self.data: # search in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False
        else :
            if self.right:
                return self.right.search(val) 
            else:
                return False   
    
def bulid_tree(elements):
    root = BinaryTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
# Creating the binary tree and adding elements
if __name__ == "__main__":
    numbers = [17,4,1,20,9,23,18,34]
    binary_tree = bulid_tree(numbers)
    print("Inorder Traversal :")
    print(binary_tree.inorder_traversal())
    print("Preorder Traversal :")
    print(binary_tree.preorder_traversal())
    print ("Search for 9 in the tree :")
    print(binary_tree.search(9))
    