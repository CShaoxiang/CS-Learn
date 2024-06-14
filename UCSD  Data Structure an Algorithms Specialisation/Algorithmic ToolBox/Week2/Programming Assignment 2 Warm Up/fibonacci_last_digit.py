def fibonacci_last_digit(n):
    if n <= 1:
        return n

    n = n+1

    memo = [0]*n
    memo[1] = 1

    for index  in range(2,n):
        memo[index] = (memo[index-1]+ memo[index-2]) %10

    return memo[n-1]


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
