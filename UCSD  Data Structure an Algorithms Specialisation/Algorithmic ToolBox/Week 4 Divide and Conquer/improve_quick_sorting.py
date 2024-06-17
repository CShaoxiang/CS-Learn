from random import randint


def partition3(array, left, right):
    # write your code here
    pass


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


def quicksort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left < right:
        pivot_value = median_of_medians(arr, left, right)
        pivot_index = quick_sort_partition(arr, left, right, pivot_value)

        # print(pivot_index, pivot_value)
        # print(arr)

        quicksort(arr, left, pivot_index - 1)
        quicksort(arr, pivot_index + 1, right)

def quick_sort_partition(arr, low, high,pivot_value):

    pivot_index = arr.index(pivot_value, low, high+1)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    store_index = low
    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]

            store_index += 1

    arr[store_index], arr[high] = arr[high], arr[store_index]

    return store_index


def median_of_medians(arr, left, right):
    n = right - left + 1

    # Base Case
    if n <= 10:
        return partition5(arr, left, right)

    array_of_medians = []

    for i in range(left, right + 1, 5):
        right_head = i + 4 if i + 4 <= right else right

        median = partition5(arr, i, right_head)

        array_of_medians.append(median)


    # recursively compute medians untill len(medians) < 10)
    return median_of_medians(array_of_medians, 0, len(array_of_medians) - 1)


'''
sorts a small sublist (of up to 5 elements) 
and returns the index of the median of this sublist within the original array. 
'''


def partition5(arr, left, right):
    sub_list = arr[left:right + 1]
    sub_list.sort()


    return sub_list[(len(sub_list) // 2)]

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    quicksort(elements, 0, len(elements) - 1)
    print(*elements)
