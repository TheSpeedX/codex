'''

By replacing the 1st digit of the 2-digit number *3, 
it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, 
this 5-digit number is the first example having seven primes among the ten generated numbers, 
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, 
being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) 
with the same digit, is part of an eight prime value family.

'''

from collections import Counter

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

# Generating all prime numbers between 1 to 1million
primes = primes(1000000)

# primes with 3 replacable places
primes = [x for x in primes if len(str(x)) - len(set(str(x))) >= 3]


def pdr(s):
    """take a number and return a list with families
    for example if the input number is 566003 then
    the result will be
    [[566003,566113,566223,566333,566443,566553,566663,566773,566883,566993],
    [500003,511003,522003,533003,544003,555003,566003,577003,588003,599003]]"""
    s = str(s)
    sol = []
    for duplicate in (Counter(s) - Counter(set(s))):
        a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        temp = [int(s.replace(duplicate, x)) for x in a]
        sol.append(temp)
    return sol

# list to store all the checked numbers, so not to repeat
checked = []


def check(l):
    """take a list and remove all the values which are
    not prime numbers, finally return a list with only
    prime numbers"""
    for i in l:
        checked.append(i)
        if i not in primes:
            l.remove(i)
    return l

# condition for while loop
flag = True

# while loop iterator
i = 0

# while loop
while flag:
    # check if we have not check the number before
    if primes[i] not in checked:
        # find the family of the given number
        replacements = pdr(primes[i])
        for j in replacements:
            if len(check(j)) == 8:
                print (j[0])
                flag = False
                break
    i += 1
