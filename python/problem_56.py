#!/usr/bin/python3

"""
    A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""

def euler56() -> int:
    maxi = 0
    for a in range(1, 100):
        for b in range(1, 100):
            num = a**b
            val = sum(map(int, list(str(num))))
            if maxi < val:
                maxi = val
    return maxi

tot = euler56()
print(tot)
