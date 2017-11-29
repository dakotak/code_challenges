
MULTIPLES = [3, 5]

def sum_multiples(multiples, n):
    total = 0
    for i in range(1, n):
        total += sum([i for m in multiples if i % m == 0])
    return total


if __name__ == '__main__':
    import sys
    n = int(sys.argv[1])
    print(sum_multiples(MULTIPLES, n))
