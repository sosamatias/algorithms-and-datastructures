from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node = None
        self.right: Node = None


def dfs_iterative(head: Node, result: list):
    stack: List[Node] = [head]
    while stack:
        curr = stack.pop()
        while(curr):
            result.append(curr.data)
            if curr.right is not None:
                stack.append(curr.right)
            curr = curr.left


def dfs_recursive(head: Node, result: list):
    if head is None:
        return
    result.append(head.data)
    dfs_recursive(head.left, result)
    dfs_recursive(head.right, result)
