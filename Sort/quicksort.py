def quicksort(a, left, right):
    if left < right:
        pivot = partition(a, left, right)
        quicksort(a, left, pivot - 1)
        quicksort(a, pivot + 1, right)


def partition(a, left, right):
    """

    :param a:
    :param left:
    :param right:
    :return:
    """
    pivot = left
    while left < right:
        while right > pivot and a[right] > a[pivot]:
            right -= 1
        if right != pivot:
            a = swap(a, pivot, right)
            pivot = right

        while left < pivot and a[left] <= a[pivot]:
            left += 1

        if left != pivot:
            a = swap(a, pivot, left)
            pivot = left

    return pivot


def swap(a, x, y):
    tmp = a[x]
    a[x] = a[y]
    a[y] = tmp
    return a


if __name__ == '__main__':
    a = [5, 2, 6, 1, 3, 4]
    size = len(a)
    quicksort(a, 0, size - 1)
    print a
