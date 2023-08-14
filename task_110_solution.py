import sys
import random

printed_permutations = 0


def generate_permutations(a, n):
    global printed_permutations
    if n == 0:
        print(''.join(a))
    else:
        for i in range(n):
            generate_permutations(a, n-1)
            j = random.randint(0, i)
            a[j], a[n] = a[n], a[j]
            printed_permutations += 1
            if printed_permutations >= 20:
                sys.exit(0)
        generate_permutations(a, n-1)


if len(sys.argv) != 2:
    sys.stderr.write('Exactly one argument is required\n')
    sys.exit(1)

word = sys.argv[1]

generate_permutations(list(word), len(word) - 1)

