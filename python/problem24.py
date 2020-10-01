import math


def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def reverse(nums, start):
    nums[start:] = reversed(nums[start:])


class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = len(nums)-2
        while(pos >= 0 and nums[pos+1] <= nums[pos]):
            pos -= 1
        if(pos >= 0):
            j = len(nums)-1
            while(j >= 0 and nums[j] <= nums[pos]):
                j -= 1
            swap(nums, pos, j)
        reverse(nums, pos+1)
        print(nums)


s = Solution()
for i in range(1, math.factorial(10)+1):
    s.nextPermutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
