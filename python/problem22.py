#Project Euler Problem 22

names = list()
total_sum = 0

#finding the sum of characters of a name
def char_sum(name):
	sum = 0
	for i in name:
		if i != '"':
			sum += (ord(i)-ord('A')+1)
	return sum

#sorting the names 
filename = 'p022_names.txt'
with open (filename) as fin: 
	for line in fin:
		names = line.split(",")

names.sort()


#finding the total sum
for i in range(len(names)):
	temp = char_sum(names[i]) * (i+1)
	total_sum += temp

print(total_sum)