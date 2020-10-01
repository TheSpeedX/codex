import time


def get_next_digit(numer, denom):
    quotient, remainder = divmod(numer, denom)
    yield (quotient, remainder)
    while True:
        remainder *= 10
        quotient, remainder = divmod(remainder, denom)
        yield (quotient, remainder)


def main(n):
    max_cycle_len = 0
    for q in range(n, 0, -1):
        dig_iter = get_next_digit(1, q)
        lookup = set()
        while True:
            t = next(dig_iter)
            if t[1] == 0 or t[1] in lookup:
                break
            lookup.add(t[1])

        if len(lookup) > max_cycle_len:
            max_cycle_len = len(lookup)
            if max_cycle_len == q-1:
                return q, max_cycle_len
    return max_cycle_len


if __name__ == '__main__':
    start = time.time()
    print(main(1000))
    end = time.time()
    print("It took {} ms ".format(end - start))

