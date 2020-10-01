from itertools import count

def polygonal_numbers(sides):
    result = 0
    for n in count():
        yield result
        result += (sides - 2) * n + 1

tt, pp, hh = polygonal_numbers(3), polygonal_numbers(5), polygonal_numbers(6)
t = p = 0 
for h in hh:
    while p < h: p = next(pp)
    while t < h: t = next(tt)
    if t == p == h > 40755:
        print(h)
        break