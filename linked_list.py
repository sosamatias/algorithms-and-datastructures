class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        self.flag = 0


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def push(self, new_data):
        new = Node(new_data)
        new.next = self.head
        self.head = new

    # Time O(n) Space O(n)
    def detectLoop(self):
        s = set()
        curr = self.head
        while (curr):
            if (curr in s):
                return True
            s.add(curr)
            curr = curr.next
        return False

    # another approach is to add a flag into Node class
    # in that way we can have a Space of O(1)
    def detectLoopFlag(self):
        curr = self.head
        while curr:
            if curr.flag == 1:
                return True
            curr.flag = 1
            curr = curr.next
        return False

    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            new_node = Node(curr.data, prev)
            prev = new_node
            curr = curr.next
        self.head.data = prev.data
        self.head.next = prev.next
        return self.head
