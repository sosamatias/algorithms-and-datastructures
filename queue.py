class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


class Queue:  # FIFO
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, data):
        new = Node(data)
        if not self.first:
            self.first = new
            self.last = new
        else:
            self.last.next = new
            self.last = self.last.next

    def dequeue(self):
        if not self.first:
            return None
        result = self.first.val
        self.first = self.first.next
        return result
