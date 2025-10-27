import random

MIN = -1000
MAX = 1000

def generate_array(length):

    return [random.randint(MIN, MAX) for _ in range(length)]

def swap(arr, i, j):

    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, left, right, asc):

    pivot = arr[right]
    

    i = left - 1

    for j in range(left, right):
        if asc:

            if arr[j] < pivot:
                i += 1
                swap(arr, i, j)
        else:

            if arr[j] > pivot:
                i += 1
                swap(arr, i, j)

    swap(arr, i + 1, right)

    return i + 1

def quick_sort(arr, left=None, right=None, asc=True):

    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1

    if left < right:

        pivot_index = partition(arr, left, right, asc)

        quick_sort(arr, left, pivot_index - 1, asc)
        quick_sort(arr, pivot_index + 1, right, asc)

    return arr

arr = generate_array(60)

arr2 = arr.copy()

print("Сортування за зростанням:")
print(quick_sort(arr, asc=True))

print("\nСортування за спаданням:")
print(quick_sort(arr2, asc=False))