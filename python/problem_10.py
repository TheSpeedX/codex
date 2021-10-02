#!/usr/bin/env python

"""  Provides the sum of all the primes below two million"""

def is_prime(num):
  """is_prime checks for the number "num"
   if the number "num" is prime  it returns true 
   if not prime returns false"""

  if (num<=1):
     return False
  for i in range(2,int (num**0.5)+1):
        if (num%i == 0):
            return False
  return True
#initialize  variable "sum" 
sum = 0
#iterate the loop from 2 to 2 million
for i in range(2,2000000):
 #check if num is prime 
    if ( is_prime(i)):
 # If num is prime , Add num to variable sum 
        sum = sum + i
#print value of sum
print(sum)
