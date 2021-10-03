"""
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.

"""

def is_bouncy(n):
    inc, dec, s = False, False, str(n)
    for i in range(len(s)-1):
        if s[i+1] > s[i]: inc = True
        elif s[i+1] < s[i]: dec = True
        if inc and dec: return True
    return False

n, p = 21780, 0.90
b = n * p
while p != 0.99:
    n += 1
    if is_bouncy(n): b += 1
    p = b / n

print "Project Euler 112 Solution:", n
