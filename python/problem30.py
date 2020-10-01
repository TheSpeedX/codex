import time


"""
The main thing about finding the upper limit for the search bound.
The upper limit will be 9^5 + 9^5 + 9^5 + 9^5 + 9^5.
"""


def check_sum(num):
    curr_sum = 0
    temp = num
    while temp > 0:
        r = temp % 10
        curr_sum = curr_sum + (r ** 5)
        temp = temp // 10
    if curr_sum == num:
        return True
    else:
        return False


def digit_five_sum(exp):
    sums = 0
    for i in range(2, (5*9**5+1)):
        if check_sum(i) is True:
            sums += i
    print(sums)


start = time.time()
digit_five_sum(5)
end = time.time()
print("It took {} s".format(end-start))
        
