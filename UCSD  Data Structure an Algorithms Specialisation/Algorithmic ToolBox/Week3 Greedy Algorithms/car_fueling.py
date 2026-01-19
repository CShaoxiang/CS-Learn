from sys import stdin
import random

def min_refills(distance, tank, stops):
    if tank == 0 or  (tank + stops[len(stops) - 1] < distance):
        return -1

    if tank >= distance:
        return 0

    if tank < stops[0]:
        return -1

    stops.append(distance)

    fill = 0
    current_distance = 0

    current_tank_level = tank

    for i in range(len(stops)-1):

        if tank + stops[i] < stops[i+1]:
            return -1

        current_tank_level -= stops[i] - current_distance
        current_distance += stops[i] - current_distance

        if current_tank_level + stops[i]< stops[i+1]:

            current_tank_level = tank
            fill += 1

        else:

            if i == len(stops)-1 and  tank + stops[i] < stops[i+1]:
                return -1

            elif i == len(stops)-1 and current_tank_level + stops[i] < stops[i+1]:

                fill += 1


    return fill


def generate_test_cases():
    # Edge cases
    test_cases = []

    # Random cases
    for _ in range(10):
        d = random.randint(1, 10000)
        m = random.randint(1, 500)
        n = random.randint(1, 100)
        stops = sorted(random.sample(range(1, d), n))
        test_cases.append((d, m, stops))

    return test_cases

def run_stress_test():
    test_cases = generate_test_cases()
    for i, (d, m, stops) in enumerate(test_cases):
        try:
            result = min_refills(d, m, stops)
            print(f"Test case {i + 1}: d = {d}, m = {m}, stops = {stops}")
            print(f"Result: {result}")
            print()
        except Exception as e:
            print(f"Test case {i + 1} failed with exception: {e}")

if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
    # run_stress_test()