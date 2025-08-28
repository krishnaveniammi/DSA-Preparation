class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def iab(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning of the linked list.")
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
    def iap(self, data ,pos):
        new_node = Node(data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            print(f"Inserted {data} at position {pos} of the linked list.")
            return
        current = self.head
        for _ in range(pos - 1):
            if current is None:
                print("Position out of bounds.")
                return
            current = current.next
        if current is None:
            print("Position out of bounds.")
            return
        new_node.next = current.next
        current.next = new_node
        print(f"Inserted {data} at position {pos} of the linked list.")   
        
    def search(self, key):
        pos = 1
        current = self.head
        while current:
            if current.data == key:
                print(f"Value {key} found at position {pos}.")
                return
            current = current.next
            pos += 1
        print(f"Value {key} not found in the linked list.")
        
    def display(self):
        current = self.head
        if not current :
            print("The linked list is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("none")
li = LinkedList()
while True:
    print("\n linked list operations")
    print("1. Insert at Beginning")
    print("2. Insert at Back")
    print("3. Insert at Position")
    print("4. search")
    print("5. Display")    
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        data = int(input("Enter the data to insert: "))
        li.iab(data)
    elif choice == '2':
        data = int(input("Enter the data to insert: "))
        li.ab(data)
    elif choice == '3':
        data = int(input("Enter the data to insert: "))
        pos = int(input("Enter the position to insert at: "))
        li.iap(data, pos)
    elif choice == '4':
        val = int(input("Enter the value to search: "))
        li.search(val)
    elif choice == '5':
        li.display()
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")



