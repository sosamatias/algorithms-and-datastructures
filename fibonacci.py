from typing import Optional


# Time O(2^n) Space O(n) because the call stack is using memory temporally
def fibonacci_recursive(n):
    if n == 1 or n == 2:
        return n - 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# memoize to improve time complexity
# Time O(n) Space O(n)
def fibonacci_recursive_memo(n, memo={}):
    if n == 1 or n == 2:
        return n - 1
    return _get_from_memo(n-1, memo) + _get_from_memo(n-2, memo)


def _get_from_memo(n, memo):
    result = 0
    if n in memo:
        result = memo[n]
    else:
        result = fibonacci_recursive_memo(n, memo)
        memo[n] = result
    return result


# Time O(n) Space O(1)
def fibonacci_iterative(n: int) -> Optional[int]:
    if n == 1 or n == 2:
        return n - 1

    prev2 = 0
    prev1 = 1
    result = None
    for _ in range(2, n):
        result = prev1 + prev2
        prev2 = prev1
        prev1 = result
    return result
