# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        max = 1
        if len(s) == 0:
            return 0
        elif s.isspace():
            return 1
        for indice, char in enumerate(s):
            if len(s[indice+1:]) <= 1 and len(substring) > 0 or len(substring) == len(s) or len(s) - len(substring) == 1 :
                break
            if char not in substring:
                substring.append(char)
            for letra in s[indice+1:]:
                if letra in substring:
                    max = len(substring) if len(substring) > max else max
                    substring.clear()
                    break
                else:
                    substring.append(letra)
        return max if max > len(substring) else len(substring)

s = Solution()
# print(s.lengthOfLongestSubstring(''))
print(s.lengthOfLongestSubstring('ckilbkd'))
print(s.lengthOfLongestSubstring('c'))
print(s.lengthOfLongestSubstring('xxzqi'))
print(s.lengthOfLongestSubstring('brnk'))
print(s.lengthOfLongestSubstring('aa'))
print(s.lengthOfLongestSubstring('au'))