# Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting and deleting nodes.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current:
            prev.next = current.next

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()
ll.delete(2)
ll.display()
