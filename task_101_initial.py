def run():
    for c in range(1, 48):
        for b in range(1, c):
            for a in range(1, b):
                print('{}, {}, {}'.format(a, b, c))
