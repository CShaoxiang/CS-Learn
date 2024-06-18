from random import randint


def partition3(array, left, right):
    pivot_value = array[left]
    # print(f'Pivot: {pivot_value}')

    low = left
    high = right
    i = left

    while i <= high:

        if array[i] < pivot_value:
            array[low], array[i] = array[i], array[low]
            low += 1
            i += 1
        elif array[i] > pivot_value:
            array[i], array[high] = array[high], array[i]
            high -= 1
        else:
            i += 1

    # print(f'Array after partition: {array}')
    # print(f'low = {low}, high = {high}')

    return low, high

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)

    array[left], array[k] = array[k], array[left]


    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
    # arr = [5, 7, 7, 3, 2, 5, 1, 3, 5, 6, 7, 3, 0, 9, 9, 7]
    # randomized_quick_sort(arr, 0, len(arr) - 1)
