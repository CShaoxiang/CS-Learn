def majority_element_naive(elements):
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0

def majority_element(elements):
    quicksort(elements, 0, len(elements) - 1)

    if len(elements) == 0:
        return 0

    count , temp_value = 0 , elements[0]

    for e in range(len(elements)):
        if elements[e] == temp_value:
            count += 1

        else:
            temp_value = elements[e]
            count = 1

        if count > len(elements) / 2:
            return 1


    return 0


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
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))

    # arr = [1,2,3,4,1,1]
    #
    #
    # print(majority_element(arr))
