# linear serach

#  binarysearch
import math


def b_search(given_list, key):
    left = 0
    right = len(given_list) - 1
    found = False
    while left <= right and not found:
        mid = left + (right - left) // 2
        if given_list[mid] == key:
            found = True
            return found, mid
        else:
            if key < given_list[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return False, None


def j_search(given_list, key):
    '''
    Jump_search:
    Works only sorted arrays
    '''
    l = len(given_list)
    step = int(math.sqrt(l))
    given_list.sort()
    curr = 0
    while given_list[curr] < key:
        curr += step
        if curr >= l:
            return None
    for i in range(curr - step, curr):
        if given_list[i] == key:
            return i
    else:
        return None


def fib_search(given_list: list, key: int):
    '''
    fibonacci serach
    work for the sorted list
    '''
    n = len(given_list)
    # Initialize fibonacci numbers
    fibMMm2 = 0  # (m-2)'th Fibonacci No.
    fibMMm1 = 1  # (m-1)'th Fibonacci No.
    fibM = fibMMm2 + fibMMm1  # m'th Fibonacci

    # fibM is going to store the smallest
    # Fibonacci Number greater than or equal to n
    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1

    # Marks the eliminated range from front
    offset = -1

    # while there are elements to be inspected.
    # Note that we compare arr[fibMm2] with x.
    # When fibM becomes 1, fibMm2 becomes 0
    while (fibM > 1):

        # Check if fibMm2 is a valid location
        i = min(offset+fibMMm2, n-1)

        # If x is greater than the value at
        # index fibMm2, cut the subarray array
        # from offset to i
        if (arr[i] < key):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i

        # If x is greater than the value at
        # index fibMm2, cut the subarray
        # after i+1
        elif (arr[i] > key):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1

        # element found. return index
        else:
            return i

    # comparing the last element with x */
    if(fibMMm1 and arr[offset+1] == key):
        return offset+1

    # element not found. return -1
    return None


if __name__ == "__main__":
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    print(b_search(arr, 55))
    print(j_search(arr, 55))
    print(fib_search(arr, 55))
