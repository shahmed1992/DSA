import time


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current:
                if current.value == value:
                    break
                prev = current
                current = current.next
            if current == None:
                return
            prev.next = current.next
            current = None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        count = 1
        current = self.head
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        while current:
            if count + 1 == position:
                new_element.next = current.next
                current.next = new_element
                return
            else:
                count += 1
                current = current.next
            # break

    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
ll = LinkedList(e1)
print("Adding first element to linked list")
ll.print()
time.sleep(1)
print("Appending 2")
ll.append(e2)
ll.print()
print("Inserting 3 at the 3rd position")
time.sleep(1)
ll.insert(e3, 3)
ll.print()
time.sleep(1)
ll.delete(3)
print("Linked List after deleting 3")
ll.print()
time.sleep(1)
e4 = Node(4)
ll.append(e4)
time.sleep(1)
print("Linked List After adding 4")
ll.print()

