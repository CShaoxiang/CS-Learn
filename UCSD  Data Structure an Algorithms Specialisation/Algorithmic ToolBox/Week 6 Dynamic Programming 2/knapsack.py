from sys import stdin


'''
1 : create a 2-D array , i * w 
    i : the number of items available to select
    w : the capacity of knapsack 
    
    Fill the role with 0 ,  where i = 0 , w (0 - capacity)
    Fill the role with 0 ,  where w = 0 , i (0 - number of weights)
    
2 : for the number of items available to select from (1 : len(weight+1), 
    
'''
def maximum_gold(capacity, weights):
    dp_array = [[0 for i in range(capacity+1)] for j in range(len(weights)+1)]

    for i in range(1,len(weights)+1):
        for w in range(1, capacity+1):

            dp_array[i][w] = dp_array[i - 1][w]



            if w >= weights[i-1]:

                value = dp_array[i-1][w - weights[i-1]] + weights[i-1]

                if value > dp_array[i][w]:
                    dp_array[i][w] = value


    return dp_array[-1][-1]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))


