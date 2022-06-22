# Time O(n * n!) , Space O(n * n!)
def permutations1(arr):
    def helper(i, arr, result):
        if i == len(arr) - 1:
            result.append(arr.copy())  # arr.copy() O(n)
        else:
            for j in range(i, len(arr)):  # for calling recursive helper O(n!)
                swap(arr, i, j)
                helper(i + 1, arr, result)
                swap(arr, i, j)

    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    result = []
    helper(0, arr, result)
    return result


# Time O(n!) - Space O(n^2)
def permutations2(arr):
    if not arr:
        return [[]]

    first = arr[0]
    rest = arr[1:]
    perm_without_first = permutations2(rest)

    result = []
    for perm in perm_without_first:
        for i in range(0, len(perm) + 1):
            new_perm = [*perm[:i], first, *perm[i:]]
            result.append(new_perm)
    return result
