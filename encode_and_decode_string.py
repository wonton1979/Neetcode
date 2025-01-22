"""
Encode and Decode Strings

Status: Solved on the thirteen's attempt, total time used : one hour and twenty minutes.

Problems description:

Design an algorithm to encode a list of strings to a single string.

The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

"""

"""
My Solution:

1. User can input two type of data: Normal Input or Empty List

2. For normal input,we extract the string from list one by one and and '|' between each string to separate them.

remove the last '|' before return, otherwise, the additional empty string will be add to the end of decode list.

In the decode function, it is very handy to use the split function and using the '|' as the separator. 

3. If user input empty list, we need to handle it separately

"""

class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_str:str = ""
        if len(strs) > 0:
            if len(strs) == 1:
                return strs[0]
            else:
                for each_str in strs:
                    encoded_str += each_str + "|"
        else:
            return "Empty List"
        return encoded_str[:-1]

    def decode(self, s: str) -> list[str]:
        if s == "Empty List":
            return []
        if len(s) > 0 and "|" in s:
            return s.split("|")
        else:
            return s.split(" ")