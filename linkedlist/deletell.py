class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Inserted {data} at the back of the linked list.")
        
    def delete_node(self, key):
        current = self.head
        previous = None
        
        if current is None:
            print("The linked list is empty.")
            return
        
        # If the node to be deleted is the head
        if current.data == key:
            self.head = current.next
            print(f"Deleted {key} from the linked list.")
            return
        
        while current and current.data != key:
            previous = current
            current = current.next
        
        if current is None:
            print(f"Value {key} not found in the linked list.")
            return
        
        previous.next = current.next
        print(f"Deleted {key} from the linked list.")
    def delete_node_begin(self, key):
        if self.head is None:
            print("The linked list is empty.")
            return
        deleted_data = self.head.data
        self.head = self.head.next
        print(f"Deleted {deleted_data} from the beginning of the linked list.") 
    def delete_node_end(self, key):
        if self.head is None:
            print("The linked list is empty.")
            return
        current = self.head
        previous = None
        
        while current.next:
            previous = current
            current = current.next
        
        if previous is None:
            self.head = None
        else:
            previous.next = None
        print(f"Deleted {current.data} from the end of the linked list.")
        
        
li = LinkedList()
li.append(10)
li.append(20)
li.append(30)
li.append(40)
li.append(50)
li.delete_node_end()
