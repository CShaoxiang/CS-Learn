"""
    Determines whether a given sequence of numbers contains an element that appears more than half the times
    using a divide-and-conquer approach.

    The function follows these steps:
    1. If the sequence is empty, return 0.
    2. Recursively divide the sequence into two halves until the base case of a single element is reached.
    3. Combine the results of the two halves to determine the majority element in the entire sequence.

    Args:
        elements (list): A list of integers representing the sequence.

    Returns:
        int: Returns 1 if there is an element that appears more than n/2 times, otherwise returns 0.


    Time Complexity:
        O(n * log n)
        Recursive Calls: The array is recursively split into two halves, resulting in  O(log n) levels of recursion.

        Counting Elements:
            At each level of recursion,
            counting the occurrences of the majority elements in the combined subarray takes O(n) time.

        Overall: Combining these, the overall time complexity is  O(n * log n).
"""


def majority_element(elements):
    def majority_divide_conquer(start, end):

        # Base case: if the subarray contains only one element, that element is the majority

        if start == end:
            return elements[start]

        # Divide: find the midpoint of the current subarray
        mid = (start + end) // 2

        # Conquer: recursively find the majority element in the left and right halves
        left = majority_divide_conquer(start, mid)
        right = majority_divide_conquer(mid + 1, end)

        if left == right:
            return left


        else:
            left_count = 0
            right_count = 0

            for i in range(start, end):
                if elements[i] == left:
                    left_count += 1

                else:
                    right_count += 1

            return left if left_count > right_count else right

    n = len(elements)
    if n == 0:
        return 0

    candidate = majority_divide_conquer(0, n - 1)

    # Verify the candidate
    if elements.count(candidate) > n / 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))

    # arr = []
    #
    # print(majority_element(arr))
