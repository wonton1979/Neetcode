"""
Top K Frequent Elements

Status: Solved on the second attempt, total time used : half an hour

Problems description:

Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

"""

"""
My Solution:

1. set the list to remove the duplicates and convert it back to list and assign it.

2. loop through the new list to count the frequent for each number.

3. Add each number with it's frequent to a dictionary, then sort the dictionary buy using frequent. 

then cut the list to match the length of 'k'.

4. append the first element of each list inside to final result.

"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequent_dic = {}
        result:list = []
        set_list = list(set(nums))
        for num in set_list:
            count:int = nums.count(num)
            frequent_dic[num] = count
        matched_list = sorted(frequent_dic.items(), key=lambda x: x[1], reverse=True)[:k]
        for num in matched_list:
            result.append(num[0])
        return result