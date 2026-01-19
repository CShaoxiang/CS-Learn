def compute_operations(n):
    memo_array = [0] * (n + 1)

    pred_array = [0] * (n + 1)

    sequence = []

    for i in range(1, n + 1):

        memo_array[i] = memo_array[i - 1] + 1
        pred_array[i] = i - 1

        if i % 3 == 0:
            if memo_array[i // 3] + 1 < memo_array[i]:
                memo_array[i] = memo_array[i // 3] + 1

                pred_array[i] = (i // 3)

        if i % 2 == 0:
            if memo_array[i // 2] + 1 < memo_array[i]:
                memo_array[i] = memo_array[i // 2] + 1

                pred_array[i] = (i // 2)

    while n > 0:
        sequence.append(n)
        n = pred_array[n]

    sequence.reverse()

    return sequence


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
