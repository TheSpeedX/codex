n = int(input("Enter the Length of the number"))

# first two terms
n1, n2 = 1, 1
count = 0
nth=0
# check if the number of terms is valid
if n < 1:
   print("Please enter a positive integer")
else :
   print("First occurance is:")
   while len(str(nth))< n:
       
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
   #count + 2 gives the right output
   print(count+2)
       
