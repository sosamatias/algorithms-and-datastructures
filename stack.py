class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


class Stack:  # LIFO
    def __init__(self):
        self.last = None

    def push(self, data):
        new = Node(data)
        if not self.last:
            self.last = new
        else:
            temp = self.last
            self.last = new
            new.next = temp

    def pop(self):
        if self.last:
            result = self.last.val
            self.last = self.last.next
            return result
        return None
