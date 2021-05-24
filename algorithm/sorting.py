"""sorting algorithms"""


def merge_sort(given_list: list) -> list:
    '''merge sort'''
    if len(given_list) > 1:
        mid = len(given_list)//2  # Finding the mid of the array
        L = given_list[:mid]  # Dividing the array elements
        R = given_list[mid:]  # into 2 halves

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                given_list[k] = L[i]
                i += 1
            else:
                given_list[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            given_list[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            given_list[k] = R[j]
            j += 1
            k += 1


def bubble_sort(given_list: list) -> list:
    '''bubble sort'''
    l = len(given_list)
    for i in range(l):
        swap = False
        for j in range(0, l - i - 1):
            if given_list[j] > given_list[j + 1]:
                given_list[j], given_list[j +
                                          1] = given_list[j + 1], given_list[j]
            swap = True
        if not swap:
            break
    return given_list


def quick_sort(given_list: list, low: int, high: int) -> list:
    """ quick sort"""
    def partition(arr, low, high):
        i = (low - 1)
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] < pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i + 1)
    #
    if low < high:
        pi = partition(given_list, low, high)

        quick_sort(given_list, low, pi-1)
        quick_sort(given_list, pi+1, high)

    pass


def intersection_sort(given_list: list) -> list:
    '''intersection sort'''
    pass


def selection_sort(given_list: list) -> list:
    '''selection sort'''
    pass


def shell_sort(given_list: list) -> list:
    '''shell sort'''
    pass


def counting_sort(given_list: list) -> list:
    """
    counting sort
    """
    pass


def radix_sort(given_list: list) -> list:
    """
    radix sort
    """
    pass


def bucket_sort(given_list: list) -> list:
    """
    bucket_sort sort
    """
    pass


if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    # merge_sort(sample)
    quick_sort(sample, 0, len(sample)-1)
    print(sample)
