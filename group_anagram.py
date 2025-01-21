"""
Group Anagram

Status: Solved on the first attempt, total time used : 2 hours

Problems description:

Given an array of strings strs, group all anagrams together into sub-lists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string,

but the order of the characters can be different.

"""

"""
My Solution:

1. Sort the list of strings and and append them into a new list. from the new list, we can see which of them are anagrams

2. Deep copy the new list. list is mutable, by deep copy, any change made on copied list will not affect the original list.

3. Change back the copied list to a set to remove duplicate anagrams.

4. loop through the original sorted list to find out the anagrams. as the list index on sorted list match the original list,

so the string in original list will add to the grouped anagrams list accordingly.

"""

from copy import deepcopy


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strs_list : list = []
        group_anagrams:list = []
        for each_str in strs:
            strs_list.append(sorted(list(each_str)))

        copy_of_strs_list: list = deepcopy(strs_list)
        for index,each_str in enumerate(copy_of_strs_list):
            copy_of_strs_list[index] = "".join(each_str)

        copy_of_strs_set: list= list(set(copy_of_strs_list))

        for index,each_str in enumerate(copy_of_strs_set):
            copy_of_strs_set[index] = list(each_str)

        outer_index:int = 0

        while len(copy_of_strs_set) > 0:
            group_anagrams.append([])
            for index, each_str in enumerate(strs_list):
                if each_str == copy_of_strs_set[0]:
                    group_anagrams[outer_index].append(strs[index])

            del (copy_of_strs_set[0])
            outer_index += 1

        return group_anagrams