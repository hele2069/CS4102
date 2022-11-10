# A python3 program to find a peak
#  element using divide and conquer

# A binary search based function
# that returns index of a peak element
from math import floor


def findPeak_helper(array, low, high):
    mid = floor(low + (high - low) / 2)
    if array[mid - 1] < array[mid] and array[mid + 1] < array[mid]:
        return array[mid]
    if mid > 1 and array[mid - 1] > array[mid]:
        return findPeak_helper(array, low, (mid - 1))
    elif mid < high + 1 and array[mid + 1] > array[mid]:
        return findPeak_helper(array, (mid + 1), high)


def findPeak(array):
    n = len(array)
    return findPeak_helper(array, 2, n - 3)


# Driver code
array = [0, 1, 4, 23, 18, 14, 15, 13, 1, 0]  # 23 15
array1 = [0, 1, 4, 1, 0]  # 4
array2 = [0, 1, 1, 1, 0]  # none
array3 = [0, 1, 1, 0]  # none
array4 = [0, 1, 4, 23, 2, 14, 15, 100, 1, 0]  # 23 100
array5 = [0, 1, 3, 2, 1, 6, 5, 4, 1, 1, 1, 1, 1, 0]  # 3
array5 = [0, 1, 2, 3, 4, 5, 6, 10, 12, 9, 1, 1, 1, 0]  # 3

print("Index of a peak point is", findPeak(array))
print("Index of a peak point is", findPeak(array1))
print("Index of a peak point is", findPeak(array2))
print("Index of a peak point is", findPeak(array3))
print("Index of a peak point is", findPeak(array4))
print("Index of a peak point is", findPeak(array5))
