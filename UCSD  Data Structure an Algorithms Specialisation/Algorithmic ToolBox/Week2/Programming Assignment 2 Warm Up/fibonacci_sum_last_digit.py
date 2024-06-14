def fibonacci_sum(n):
    n = n % Cal_Pisano_period(10)


    if n <= 1:
        return n

    n = n + 1  # Adjusting n as per the original code logic

    a, b = 0, 1  # Initializing the first two Fibonacci numbers
    sum = 1  # Starting with the sum of the first Fibonacci number (F1)

    for index in range(2, n):
        c = (a + b) % 10  # Next Fibonacci number modulo 10
        sum = (sum + c) % 10  # Adding to the sum modulo 10
        a, b = b, c  # Updating the last two Fibonacci numbers

    return sum


def Cal_Pisano_period(m):

    if m <=1 :
        return m

    f0 , f1 = 0 , 1
    for index in range(0, m*m):
        f0 , f1 = f1 , (f0 + f1) % m

        if f0 == 0 and f1 == 1:

            return index+1

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
