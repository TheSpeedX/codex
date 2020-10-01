import time

"""
def find_exp(x, y):
    res = 1
    while y > 0:
        if (y & 1):
            res = res * x
        y = y >> 1
        x = x * x
    return res
"""


# Brute Force Solution of checking all the pairs
def distinct_seq(a, b):
    lookup = set()
    for i in range(2, a+1):
        for j in range(2, b+1):
            # if find_exp(i, j) not in lookup:
            lookup.add(i**j)  # finding exponent in O(logj) time for each i

    print(len(lookup))


start = time.time()
distinct_seq(100, 100)
end = time.time()
print("It took {} s".format(end - start))



