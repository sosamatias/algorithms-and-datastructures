# Time O(2^n) - Space O(n^2)
def combinations(arr: list):
    if not arr:
        return [[]]

    first = arr[0]
    rest = arr[1:]
    comb_without_first = combinations(rest)

    comb_with_first = []
    for comb in comb_without_first:
        new_comb = [first, *comb]
        comb_with_first.append(new_comb)

    return [*comb_with_first, *comb_without_first]
