def quicksort(arr):
    if len(arr) == 0:
        return []

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):  # skip first element
        if arr[i] > pivot:
            right.append(arr[i])
        else:
            left.append(arr[i])

    return [*quicksort(left), pivot, *quicksort(right)]
