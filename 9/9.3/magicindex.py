# 9.3: A magic index in an array A[0..n-1] is defined to be an index such
# that A[i] = i. Given a sorted array of distinct integers, write a method
# to find a magic index, if one exists, in array A.

# The simplest solution would be to make a linear pass through the array.

def find_magic(list_):
    for index, val in enumerate(list_):
        if index == val:
            return index

    return None

# However, this method runs in O(n) time in the worst case, if the magic
# index is the last list position.

# Another approach might be to use modified binary search. For example,
# if the middle element of the list is examined first, and it is found
# that A[i] > i, then the magic index cannot be to the right of this
# position, since the list is sorted.

def find_magic(list_):
    return _find_magic(list_, 0, len(list_))

def _find_magic(list_, start, end):
    if start >= end:
        return None

    middle = (start + end) // 2
    if middle == list_[middle]:
        return middle
    elif middle < list_[middle]:
        return _find_magic(list_, start, middle)
    else:
        return _find_magic(list_, middle + 1, end)

# However, this function might not work properly if the input doesn't
# contain distinct integers. For example, take [0, 1, 1, 2]. The function
# above stops at index 2 when it finds that the value at 2 is less than 2,
# and decides to search right only. But, in this case, the magic index
# is to the left.

def _find_magic(list_, start, end):
    if start >= end:
        return None

    middle = (start + end) // 2
    middle_val = list_[middle]

    if middle == middle_val:
        return middle

    # always search left, up to and including the index that is the middle
    # value, since any value in that range could be a magic index
    left = _find_magic(list_, start, middle_val + 1)

    if left:
        return left
    else:
        return _find_magic(list_, middle + 1, end)

# This function gives us the benefit of sublinear time and the ability to
# handle non-distinct elements.
