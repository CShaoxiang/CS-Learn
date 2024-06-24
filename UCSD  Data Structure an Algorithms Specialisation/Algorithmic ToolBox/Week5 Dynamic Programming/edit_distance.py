def edit_distance(first_string, second_string):
    m = len(first_string)
    n = len(second_string)

    # Initialize the previous row to handle empty string cases
    prev = [j for j in range(n + 1)]
    current = [0] * (n + 1)

    for i in range(1, m + 1):
        current[0] = i
        for j in range(1, n + 1):
            if first_string[i - 1] == second_string[j - 1]:
                current[j] = prev[j - 1]
            else:
                current[j] = min(prev[j], current[j - 1], prev[j - 1]) + 1
        prev = current.copy()

    return prev[n]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
