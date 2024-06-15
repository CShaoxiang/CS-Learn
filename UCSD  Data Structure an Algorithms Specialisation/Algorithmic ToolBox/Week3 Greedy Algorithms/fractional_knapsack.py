from sys import stdin

''' 
computes the maximum value that can be carried in a knapsack with a given capacity, using a greedy approach. It selects items based on their value-to-weight ratio.

The loop runs as long as there is remaining capacity in the knapsack.

Within the loop:
best_item_weight is determined by calling the best_item function, which identifies the item with the highest value-to-weight ratio.

a is the amount of weight to take from the best item. It is the minimum of the remaining weight of the best item and the remaining capacity of the knapsack.

If the weight of the best item is 0, the function returns the current value since no more items can be added.

The value is updated by adding the value of the fraction of the best item added to the knapsack. This is calculated as a * (values[best_item_weight] / weights[best_item_weight]).

The capacity is reduced by a.
The weight of the best item is reduced by a.

Return Value:

The function returns the total value accumulated.



'''
def optimal_value(capacity, weights, values):
    value = 0

    if capacity == 0:
        return value
    while capacity > 0:
        best_item_weight = best_item(weights, values)


        a = min(weights[best_item_weight], capacity)

        if weights[best_item_weight] == 0 :
            return value

        value += a * (values[best_item_weight] / weights[best_item_weight])
        capacity -= a
        weights[best_item_weight] -= a


    return value



'''
This function identifies the item with the highest value-to-weight ratio from the list of available items.
'''
def best_item (weights, values):
    best_item = 0
    max_value = 0

    for i in range(len(values)):
        if weights[i] > 0:
            if values[i] / weights[i] > max_value:
                max_value = values[i] / weights[i]
                best_item = i


    return best_item




if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
