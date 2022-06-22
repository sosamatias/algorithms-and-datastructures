from collections import deque


# Time O(n log n), Space O(n)
def mergesort(arr):  # example arr = [1,5,2,3,4]
    to_order = deque()
    for e in arr:
        to_order.append(deque([e]))  # to_order = [[1],[5],[2],[3],[4]]

    while len(to_order) > 1:
        merged = _merge(to_order.popleft(), to_order.popleft())
        to_order.append(deque(merged))
    return list(to_order[0])


def _merge(collection_a: deque, collection_b: deque):
    result = []
    while len(collection_a) > 0 or len(collection_b) > 0:
        if len(collection_a) > 0 and len(collection_b) > 0:
            if collection_a[0] < collection_b[0]:
                result.append(collection_a[0])
                collection_a.popleft()
            else:
                result.append(collection_b[0])
                collection_b.popleft()

        elif len(collection_a) > 0:
            result.append(collection_a[0])
            collection_a.popleft()

        elif len(collection_b) > 0:
            result.append(collection_b[0])
            collection_b.popleft()

    return result
