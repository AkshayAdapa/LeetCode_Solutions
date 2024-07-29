
# Longest Substring Without Repeating Charecters:

class Solution(object):

    def lengthOfLongestSubstring(self, s):
        char_set = set()
        left = 0
        max_length = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length
obj =Solution()
s = input("Enter your string : ")
A = obj.lengthOfLongestSubstring(s)
print(A)   

#input : s = "abcabcbb"
#output : 3
#input : s = "bbbbb"
#output : 1