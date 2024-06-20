def change(money):
    # write your code here
    coin_array = [1, 3, 4]

    memo_array = [float('inf')] * (money + 1)
    memo_array[0] = 0

    for i in range(money + 1):

        for j in coin_array:
            if i >= j:
                memo_array[i] = min(memo_array[i], memo_array[i - j] + 1)

    return memo_array[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
