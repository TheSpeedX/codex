#To get the millionth permutation of 0,1,2,3,4,5,6,7,8,9

import itertools
from itertools import isslice
array_nums = list(range(10)) #we get a list of all the digits from 0 to 9
num = itertools.islice(itertools.permutations(array_nums),999999,None) #itertools.islice is a 4 input method, check geeks for geeks for more
print("".join(str(x) for x in next(num)))
