import random

MIN = -200
MAX = 500

def generate_array(length):
    return [random.randint(MIN, MAX) for _ in range(length)]


def print_array(arr):
    for i, val in enumerate(arr, start=1):
        print(f"[Елемент_{i}_значення_{val}]")


def calculate_count_and_sum_even(arr, min_val, max_val):
    count = 0
    total_sum = 0
    for val in arr:
        if min_val <= val <= max_val and val % 2 == 0:
            count += 1
            total_sum += val
    return {"count": count, "sum": total_sum}


def calculate_avg(arr):
    return sum(arr) / len(arr) if arr else 0


def calculate_avg_and_count(arr):
    avg = calculate_avg(arr)
    count = sum(1 for val in arr if val > avg)
    return {"avg": avg, "count": count}


def sum_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return []
    return [a + b for a, b in zip(arr1, arr2)]


def concat_arrays(*arrays):
    result = []
    for arr in arrays:
        result.extend(arr)
    return result


def swap_max_and_min(arr):
    if not arr:
        return arr

    max_val = max(arr)
    min_val = min(arr)

    return [min_val if x == max_val else max_val if x == min_val else x for x in arr]


def split_array(arr):
    positive = [x for x in arr if x >= 0]
    negative = [x for x in arr if x < 0]
    return {"positive": positive, "negative": negative}


def remove_duplicates_of_min_max(arr):
    if not arr:
        return arr

    min_val = min(arr)
    max_val = max(arr)

    result = []
    min_found = False
    max_found = False

    for val in arr:
        if val == min_val:
            if not min_found:
                result.append(val)
                min_found = True
        elif val == max_val:
            if not max_found:
                result.append(val)
                max_found = True
        else:
            result.append(val)

    return result


def array_between_averages(arr1, arr2):
    avg1 = calculate_avg(arr1)
    avg2 = calculate_avg(arr2)

    min_avg = min(avg1, avg2)
    max_avg = max(avg1, avg2)

    combined = concat_arrays(arr1, arr2)

    return [x for x in combined if min_avg <= x <= max_avg]


main_arr = generate_array(10)
arr_for_sum = generate_array(10)
arr_for_concat = generate_array(5)

print_array(main_arr)
print(calculate_count_and_sum_even(main_arr, -20, 40))
print(calculate_avg_and_count(main_arr))
print(sum_arrays(main_arr, arr_for_sum))
print(concat_arrays(main_arr, arr_for_concat))
print(swap_max_and_min(main_arr))
print(split_array(main_arr))
print(remove_duplicates_of_min_max(main_arr))
print(array_between_averages(main_arr, arr_for_sum))
