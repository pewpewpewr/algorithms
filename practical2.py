import random

MIN = -500
MAX = 666


def generate_array(length):
    return [random.randint(MIN, MAX) for _ in range(length)]


def print_array(arr):
    for i, val in enumerate(arr):
        print(f"[cell - {i}, value - {val}]")


def bubble_sort(arr, reverse=False):
    arr = arr[:] 
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if (reverse and arr[j] < arr[j + 1]) or (not reverse and arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr, reverse=False):
    arr = arr[:] 
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while (reverse and j >= 0 and arr[j] < current) or (not reverse and j >= 0 and arr[j] > current):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


def selection_sort(arr, reverse=False):
    arr = arr[:]  
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if (reverse and arr[j] > arr[min_index]) or (not reverse and arr[j] < arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


arr = generate_array(100)
print_array(arr)

print("Bubble Sort ASC:", bubble_sort(arr, False))
print("Bubble Sort DESC:", bubble_sort(arr, True))
print("Insertion Sort ASC:", insertion_sort(arr, False))
print("Insertion Sort DESC:", insertion_sort(arr, True))
print("Selection Sort ASC:", selection_sort(arr, False))
print("Selection Sort DESC:", selection_sort(arr, True))
