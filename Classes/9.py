# Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping and displaying elements.
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def display(self):
        print(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

stack = Stack()
stack.push(1)
stack.push(2)
stack.display()
print(stack.pop())
stack.display()
