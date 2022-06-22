from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node = None
        self.right: Node = None


def bfs_iterative(head: Node, result: list):
    queue: deque[Node] = deque()
    queue.append(head)

    while queue:
        result.append(queue[0].data)

        if queue[0].left is not None:
            queue.append(queue[0].left)

        if queue[0].right is not None:
            queue.append(queue[0].right)

        queue.popleft()


def bfs_recursive(head: Node, queue: deque[Node], result: list):
    if not queue:
        return

    result.append(queue[0].data)

    if queue[0].left is not None:
        queue.append(queue[0].left)

    if queue[0].right is not None:
        queue.append(queue[0].right)

    queue.popleft()

    bfs_recursive(head, queue, result)
