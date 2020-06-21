# Leetcode

"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

class Solution:

    def calculate(self, ransomNote, magazine):
        ransom_dict = self.get_dict(ransomNote, dict())
        magazine_dict = self.get_dict(magazine, dict())
        for key in ransom_dict.keys():
            if magazine_dict.get(key) == None:
                return False
            if ransom_dict.get(key) > magazine_dict.get(key):
                return False
        return True

    def get_dict(self, str, dct):
        for char in str:
            if dct.get(char) != None:
                dct.update({char: dct.get(char) + 1})
            else:
                dct.update({char: 1})
        return dct


ransomNote = input("ransomNote = ")
magazine = input("magazine = ")
ans = Solution()
print(ans.calculate(ransomNote, magazine))

