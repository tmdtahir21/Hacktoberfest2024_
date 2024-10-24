class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert(self, data):
        new_node = Node(data)
        self.size += 1

        if not self.head:
            self.head = new_node
            self.head.next = self.head  # Points to itself for circular nature
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def search(self, key):
        if not self.head:
            return False
        
        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    def remove(self, key):
        if not self.head:
            return

        current = self.head
        prev = None
        
        # Finding the node to remove
        while current.data != key:
            if current.next == self.head:
                print("Element not found")
                return
            prev = current
            current = current.next

        self.size -= 1
        
        # If the node to be deleted is the only node
        if current == self.head and current.next == self.head:
            self.head = None
            return
        
        # If more than one node, and node to be deleted is the head
        if current == self.head:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
        else:
            prev.next = current.next

    def find_middle(self):
        if not self.head:
            return None
        slow = self.head
        fast = self.head

        # Fast moves 2 steps, slow moves 1 step to get the middle element
        while fast.next != self.head and fast.next.next != self.head:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def display(self):
        if not self.head:
            print("Empty list")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print()


# Example usage:
clist = CircularLinkedList()
clist.insert(10)
clist.insert(20)
clist.insert(30)
clist.insert(40)
clist.insert(50)

print("Original List:")
clist.display()

print(f"Search 30: {clist.search(30)}")
print(f"Middle element: {clist.find_middle()}")

print("\nRemoving 30:")
clist.remove(30)
clist.display()

print(f"Middle element after removal: {clist.find_middle()}")
