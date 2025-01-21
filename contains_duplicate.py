"""
Contains Duplicate

Status: Solved on the first attempt, Time between first attempt and last attempt was 0

Problems description:

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

"""


# use 'set' to eliminate any duplicate items and then compare length with original list.

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        return not (len(set(nums)) == len(nums))