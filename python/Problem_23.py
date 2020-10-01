# defining a function to find factors
def factors(x):
    temp = []
    for i in range(1, x + 1):
        if x % i == 0:
            temp.append(i)
    return temp
# A function to check whether a number is abundant
def check_abundance(x):
    sum = 0;
    for k in factors(x):
        sum += k
    if sum > x:
        return True
    else:
        return False
# Getting a list of abundant numbers between 1 and 28123
abundance_list = []
for i in range(1,28124):
    if check_abundance(i):
        abundance_list.append(i)
sum_of_abundance_list = []
# Getting a list of sum of 2 abundant numbers upto 28123
for i in range(0,len(abundance_list)):
    for j in range(i,len(abundance_list)):
        sum_of_abundance_list.append(abundance_list[i]+abundance_list[j])
num_list = range(1,28124)
ans_list = []
#comparing the lists.
for ele in num_list:
    if not ele in sum_of_abundance_list:
        ans_list.append(ele)
ans = 0
for ele in ans_list:
    ans += ele
print("The sum of all the positive integers which cannot be written as a sum of 2 abundant numbers is " + ans + ".")
