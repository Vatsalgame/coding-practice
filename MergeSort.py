def merge_sort(numlist):
    if len(numlist) == 0:
        raise IOError
    elif len(numlist) == 1:
        return numlist
    else:
        midpoint = len(numlist) / 2
        left_half = merge_sort(numlist[0:midpoint])
        right_half = merge_sort(numlist[midpoint:])
        return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = 0
    j = 0
    while i < len(left) or j < len(right):
        if i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged += [left[i]]
                i += 1
            else:
                merged += [right[j]]
                j += 1
        elif i < len(left):
            merged += [left[i]]
            i += 1
        else:
            merged += [right[j]]
            j += 1

    return merged

if __name__ == "__main__":
    merged = merge_sort([4, 5, 1, 7, 0, 6])
    print(merged)
