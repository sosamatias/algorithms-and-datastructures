# Kth Largest Element in an Array
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Note2 space should be equal to O(k)

from heapq import heappush, heappop
from typing import List


class Solution:
    # Time O(k log k + n log k) Space O(k)
    def kth_largest(self, arr: List[int], k: int) -> int:
        heap: List[int] = []
        for value in arr:
            if len(heap) < k:
                heappush(heap, value)
                continue
            if value > heap[0]:  # is bigger than smallest element
                heappop(heap)
                heappush(heap, value)

        return heap[0]
