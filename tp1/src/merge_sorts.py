def k_merge(left, right):
    """
    Each of left and right are array of sorted arrays
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += [left[l] for l in range(i, len(left))]
    result += [right[r] for r in range(j, len(right))]

    return result


def merge_sort(arrays, merge_func=k_merge):
    if len(arrays) == 1:
        return arrays[0]

    half = len(arrays) // 2
    left = arrays[:half]
    right = arrays[half:]

    sorted_left = merge_sort(left, merge_func)
    sorted_right = merge_sort(right, merge_func)

    return merge_func(sorted_left, sorted_right)
