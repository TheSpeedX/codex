#Python program to find factorial digit sum

import math
n = 100
print(sum(map(int, str(math.factorial(n)))))
