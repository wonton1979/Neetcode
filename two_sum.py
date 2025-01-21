"""
Two Sum

Status: Solved on the third attempt, Time between first attempt and last attempt was 35 minutes.


Problems description:

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

"""

"""
My Solution:

Looping through the list, for each loop, use the target number to subtract current number in list, if the remainder is

in the list, then use 'index' function to find the remainder's index.

Problem met: if first and remainder are same number, then you need check if this number appears in the list more than once.

this because otherwise the 'index' function gives you the same index as it is the only one list. 

if the number appears in the list more than once, then we need to offset the 'index' function in order to get the second

index which the number appears in the list.

"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            num_after_subtract = target - nums[i]
            if num_after_subtract in nums :
                if nums[i] == num_after_subtract:
                    if nums.count(num_after_subtract) > 1:
                        return [i, nums.index(num_after_subtract,i+1)]
                else:
                    return [i, nums.index(num_after_subtract)]
