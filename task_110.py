import sys
import random

printed_permutations = 0


def generate_permutations(a, n):
    global printed_permutations
    if n == 0:
        sys.exit(0)
    else:
        for i in range(n + 1):
            j = random.randint(0, n)
            k = random.randint(0, n)
            a[j], a[k] = a[k], a[j]
            print(''.join(a))
            generate_permutations(a, n - 1)
            printed_permutations += 1
            if printed_permutations >= 20:
                sys.exit(0)
        generate_permutations(a, n-1)


if len(sys.argv) != 2:
    sys.stderr.write('Exactly one argument is required\n')
    sys.exit(1)


word = sys.argv[1]
print('the length of the word - 1 is', len(word) - 1)
generate_permutations(list(word), len(word) - 1)