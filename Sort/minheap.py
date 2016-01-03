# [8, 5, 3, 1, 9, 6, 0, 7, 4]
#  0, 1, 2, 3, 4, 5, 6, 7, 8
def heapsort(aList):
    # convert aList to heap
    length = len(aList) - 1
    leastParent = length / 2
    for i in range(leastParent, -1, -1):
        moveDown(aList, i, length)

    # flatten heap into sorted array
    for i in range(length, 0, -1):
        if aList[0] > aList[i]:
            swap(aList, 0, i)
            moveDown(aList, 0, i - 1)

    print aList


def moveDown(aList, parent, last):
    largest = 2 * parent + 1
    while largest <= last:
        # right child exists and is larger than left child
        if (largest < last) and (aList[largest] < aList[largest + 1]):
            largest += 1

        # right child is larger than parent
        if aList[largest] > aList[parent]:
            swap(aList, largest, parent)
            # move down to largest child
            parent = largest;
            largest = 2 * parent + 1
        else:
            return  # force exit


def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp


if __name__ == '__main__':
    heapsort([8, 5, 3, 1, 9, 6, 0, 7, 4])
