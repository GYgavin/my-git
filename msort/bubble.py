#!/usr/bin/env python

def maopao(nums):
    for i in range(len(nums)-1):    
        for j in range(len(nums)-i-1): 
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [5,2,7,6,8,2,1]
print nums
print maopao(nums)
