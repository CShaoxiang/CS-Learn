# python3
import random

def build_heap(data):
    """
    Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a min heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []

    #0 indexing 
    size = len(data)-1

    for i in range(len(size)//2  ,-1,-1):
       siftDown(i,size,data,swaps)
     
    return swaps


def siftDown(i,size,Heap : list,swaps : list):

    # root of the current subTree
    min_index = i


    # compite leftCHild index 
    leftChild = 2 * i +1

    # check leftChild in the hip and is smaller than the root 
    if leftChild <= size and Heap[leftChild] < Heap[min_index]:

        min_index = leftChild


    # compute rightChild Index 
    rightChild = leftChild + 1

    # check rightChild in the hip and is smaller than the root 
    if rightChild <=size and Heap[rightChild] < Heap[min_index]:
        
        min_index = rightChild

    if i != min_index:
         # Perform swap
        Heap[i], Heap[min_index] = Heap[min_index], Heap[i]

        swaps.append((i, min_index))

        # Recursively adjust the affected subtree
        siftDown(min_index, size, Heap, swaps)

    return  swaps 





def main():
    n = int(input())

    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


def gen_tests():
    test_cases = []
    for _ in range(1000):
        n = random.randint(1,1000)

        single_test = []
        for i in range(n):
            random_node = random.randrange(0,100)
            single_test.append(random_node)

        test_cases.append(single_test)
    return test_cases


def run_stress_test():
    test_cases = gen_tests()
    for test_counter, single_test in enumerate(test_cases):
        try:
            # Make a copy of the test case to validate heap property
            original_data = single_test[:]
            swaps = build_heap(single_test)

            # Validate heap property
            is_valid = validate_heap(single_test)
            if not is_valid:
                print(f"Test case {test_counter + 1} failed: Heap property violated.")
                print(f"Original: {original_data}")
                print(f"Heap: {single_test}")
                print(f"Swaps: {swaps}")
                return

            print(f"Test case {test_counter + 1} passed.")
        except Exception as e:
            print(f"Test case {test_counter + 1} failed with exception: {e}")


def validate_heap(heap):
    """Validate the heap property for a min-heap."""
    size = len(heap)
    for i in range(len(heap) // 2,-1,-1):
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < size and heap[i] > heap[left_child]:
            return False
        if right_child < size and heap[i] > heap[right_child]:
            return False
    return True


if __name__ == "__main__":
    main()