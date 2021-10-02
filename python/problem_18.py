# Sweta Snigdha Sahoo
# author-swetasahoo29
# question

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom of the triangle below:
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

import time

#time at the start of execution
start = time.time()

#numbers copied as string
n = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

#splitting the number into a list
n = n.strip().split('\n')

#converting each and every list of strings to int
for i in range(1,len(n)):
	n[i] = n[i].strip().split(' ')
	n[i] = [int(x) for x in n[i]]

#adding the first number bcz we could not do the above
#operation as this one one number
n[0] = [75]

#counter for counting number of iterations
counter = 0

#for loop for bottom-up approach
for i in range(len(n)-2,-1,-1):
	for j in range(len(n[i])):
		n[i][j] = n[i][j] + max(n[i+1][j], n[i+1][j+1])
		counter += 1
	n.pop()

#printing the output
print ('Found {} in {} iterations'.format(n[0][0],counter))

#time at the end of execution
end = time.time()

#printing the total time
print (end-start)
