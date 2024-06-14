def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    n = n + 1

    memo = [0] * n
    memo[1] = 1

    for index in range(2, n):
        memo[index] = (memo[index - 1] + memo[index - 2])

    return gcd(memo[n - 1], m)


def gcd(a, b):
    if b == 0:
        return a
    if a == 0:
        return b

    if a == b:
        return a

    if a > b:
        return gcd(b, a % b)

    return gcd(a, b % a)


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
