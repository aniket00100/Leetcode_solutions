# Leetcode
"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
"""

class Solution:

    def calculate(self, J, S):
        new_dict = dict()
        for char in S:
            if new_dict.get(char) != None:
                new_dict.update({char: new_dict.get(char) + 1})
            else:
                new_dict.update({char: 1})
        jewels_count = 0
        for jewels in J:
            if new_dict.get(jewels) != None:
                jewels_count += new_dict.get(jewels)
        return jewels_count

J = input("J = ")
S = input("S = ")

ans = Solution()
print(ans.calculate(J, S))