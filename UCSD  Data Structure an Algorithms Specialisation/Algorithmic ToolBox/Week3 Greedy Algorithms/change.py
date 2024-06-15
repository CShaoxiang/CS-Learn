def change(money,coins_count = 0 ):
    # write your code here
    coins = [10,5,1]

    for i in range(len(coins)):

        if money >= coins[i]:

            return change(money- coins[i],coins_count+1)

    return coins_count

if __name__ == '__main__':
    m = int(input())
    print(change(m))
