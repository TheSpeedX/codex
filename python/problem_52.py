'''

It can be seen that the number, 125874, and its double, 251748, 
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

'''

# while loop iterator
i = 1

# while loop
while True:
    if set(str(i)) == set(str(6*i)):
        if set(str(i)) == set(str(5*i)):
            if set(str(i)) == set(str(4*i)):
                if set(str(i)) == set(str(3*i)):
                    if set(str(i)) == set(str(2*i)):
                        print (i)
                        break
    i += 1
	
