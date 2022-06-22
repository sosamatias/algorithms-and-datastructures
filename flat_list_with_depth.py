"""
Given a list like this: [5, [6, [7, 8], 4], 3]
return each element in a flat list with depth: [(1,5), (2,6), (3,7), (3,8), (2,4), (1,3)]
"""
from collections import deque


def flat_recursive(input: list, result: list, depth=1):
    for x in input:
        if type(x) == list:
            flat_recursive(x, result, depth+1)
        else:
            result.append((depth, x))


def flat_iterative(input: list, result: list, depth=1):
    dque = deque([(depth, x) for x in input])
    while dque:
        depth, x = dque.popleft()
        if type(x) == list:
            for i in range(len(x)-1, -1, -1):
                dque.appendleft((depth+1, x[i]))
        else:
            result.append((depth, x))
