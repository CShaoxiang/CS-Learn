def gcd(a, b):
    if b == 0 :
        return a
    if a == 0:
        return b


    if a == b:
        return a

    if a > b:

        return gcd(b, a % b)

    return gcd(a,b%a)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
