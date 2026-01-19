def fibonacci_huge(n, m):

    n = n % Cal_Pisano_period(m)

    if n <= 1:
        return n

    f0, f1 = 0, 1

    for index in range(n-1):
        fn = (f0 + f1) % m
        f0, f1 = f1, fn

    return f1


'''
Pisano Period: The length of the cycle in which the sequence of Fibonacci numbers modulo m repeats. Denoted as π(m).
Periodic Behavior: Fibonacci numbers modulo m repeat after every π(m) numbers.


Calculate Pisano Period π(m):

The Pisano period can be calculated by simulating the Fibonacci sequence modulo  m until the sequence 0, 1 appears again.
The maximum length of the Pisano period , Maximum Period = M * M 

Reduce the Problem Size:

Instead of computing Fibonacci(n), compute Fibonacci(n % π(m)). This is because Fibonacci(n) mod m = Fibonacci(n%π(m)) mod m.
Reducing n significantly reduces the number of Fibonacci calculations required, especially for large n

Complexity : O(m^2), since the maximum period length is m * m
'''

def Cal_Pisano_period(m):

    if m <=1 :
        return m

    f0 , f1 = 0 , 1
    for index in range(0, m*m):
        f0 , f1 = f1 , (f0 + f1) % m

        if f0 == 0 and f1 == 1:

            return index+1


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))
