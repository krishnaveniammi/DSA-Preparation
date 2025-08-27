class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def ab(self, data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                print(f"Inserted {data} at the back of the linked list.")
                return
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            print(f"Inserted {data} at the back of the linked list.")
li = LinkedList()
li.ab(10)
li.ab(20)
li.ab(30)   