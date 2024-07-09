from sys import stdin

'''
3 Partition Problem :
    An equal subset dp_arrayition problem  determines whether  a given set can be partitioned
    into 3  subsets such that the sum of elements in all subsets are the same 
    
    
    1. If Sum (total) is not divisible by 3, we can’t divide the array into three subsets with an equal sum. 
'''


def partition3(values):
    if len(values) < 3 or sum(values) % 3 != 0:
        return 0

    subset_sum = sum(values) // 3

    dp_array = [[[0 for i in range(subset_sum+1)] for i in range(len(values) + 1)] for i in range(len(values)+ 1)]

    # zero sum

    for i in range(subset_sum + 1):
        for j in range(subset_sum + 1):
            dp_array[0][i][j] = 1

    for i in range(1, len(values) + 1):

        num = values[i - 1]

        for s_1 in range(subset_sum + 1):
            for s_2 in range(subset_sum + 1):
                pass

    return (subset_sum, len(dp_array), len(dp_array[0]), len(dp_array[0][0]), dp_array)


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))

    # 13
