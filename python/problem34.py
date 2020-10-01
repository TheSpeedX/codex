# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 22:33:50 2020

@author: HP
"""

# Problem 34
def factorial(num):
    product = num
    for i in range(2, num):
        product *= i
    return product

def check_sum(number):
    list_digits = list(str(number))
    check_sum = 0
    for digit in list_digits:
        check_sum += factorial(int(digit))
    if check_sum == number:
        return True

def find_final_sum():
    final_list = []
    final_sum = 0
    counter = 3
    while counter < 1499999:
        if check_sum(counter):
            final_list.append(counter)
            counter += 1
        else:
            counter += 1

    for j in final_list:
        final_sum += j
    print(final_sum)

find_final_sum()

