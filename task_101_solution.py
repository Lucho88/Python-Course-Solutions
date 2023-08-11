def run():
    count = 0
    for c in range(1, 48):
        for b in range(1, c):
            for a in range(1, b):
                print('{}, {}, {}'.format(a, b, c))
                count += 1
    print(f'Count of the Pythagorean triples is {count}')

