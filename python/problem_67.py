import re
import time

f = open("euler67.txt")

def getNumbers(str): 
    array = re.findall(r'[0-9]+', str) 
    return array

data = []

start = time.time()
for lines in f.readlines():
    data.append(getNumbers(lines))

for i in range(98,-1,-1):
    temp = []
    l = i + 1
    for j in range(l):
        addend = max(int(data[i+1][j]),int(data[i+1][j+1]))
        Sum = str(int(data[i][j]) + addend)
        temp.append(Sum)
    data = data[:i] + [temp]

end = time.time()

print(f"answer: {data[0][0]}")
print(f"execution time : {end - start} seconds")