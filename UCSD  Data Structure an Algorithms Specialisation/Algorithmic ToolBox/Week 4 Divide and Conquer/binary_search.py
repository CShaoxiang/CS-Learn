def binary_search(keys, query, left=0, right=None):
    if right is None:
        right = len(keys) - 1

    if left > right:
        return -1
    
    #  left + (right - left) // 2 == (left + right) // 2 , prevent overflow 
    mid = left + (right - left) // 2

    if query < keys[mid]:
        return binary_search(keys, query, left, mid - 1)
    elif query > keys[mid]:
        return binary_search(keys, query, mid + 1, right)
    else:
        return mid


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
