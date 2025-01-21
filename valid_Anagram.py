"""
Valid Anagram

Status: Solved on the third attempt

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string,
but the order of the characters can be different.

"""


# Convert two strings to two list which then can user the 'sorted' function to sort the string in order.
# compare two lists to get the result.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_array: list[str] = sorted(list(s))
        t_array: list[str] = sorted(list(t))
        return s_array == t_array
