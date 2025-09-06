class BinaryTreeNode:
    def __init__(self,data):
        self.data = data;
        self.left = None;
        self.right = None;
    def add_child(self, data):
        if data == self.data:
            return
        if data <self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)
                print(f"Inserted {data} to the left of {self.data}")
        else:
            if data > self.data:
                if self.right:
                    self.right.add_child(data)
                else:
                    self.right = BinaryTreeNode(data)
                    print(f"Inserted {data} to the right of {self.data}") 
    def inorder_traversal(self):
        elements =[]
        if self.left: # check if left child exists
            elements += self.left.inorder_traversal()
        elements.append(self.data) # visit base node
        
        if self.right: # check if right child exists
            elements += self.right.inorder_traversal()
        return elements 
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
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
             if self.left is None and self.right is None:
                 return None
             if self.left is None:
                 return self.right
             if self.right is None:
                 return self.left 
             
            # For node with two children, replace with max from left subtree or use right subtree's min value 
             max_value = self.left.find_max()
             self.data = max_value
             self.left = self.left.delete(max_value)
        return self   
    def build_tree(elements):
        root = BinaryTreeNode(elements[0])
        for i in range(1,len(elements)):
            root.add_child(elements[i])
        return root  
if __name__ == "__main__":
    numbers = [17,4,1,20,9,23,18,34]
    binary_tree = BinaryTreeNode.build_tree(numbers)
    print("Inorder Traversal :")
    print(binary_tree.inorder_traversal())
    print("Min value :")
    print(binary_tree.find_min())
    print("Max value :")
    print(binary_tree.find_max())
    
    # Deleting a node
    binary_tree.delete(17)
    print("Inorder Traversal after deleting 20:")
    print(binary_tree.inorder_traversal())             
        