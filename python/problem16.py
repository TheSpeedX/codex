
# To find the sum of digits of the number 2^1000

#splitting each digit and mapping it to an integer, and finally passing it to a sum function
s = sum(map(int, str(2**1000)))  
print(s)

