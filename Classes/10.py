# Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())
print(queue.dequeue())
