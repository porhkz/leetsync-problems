class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        chars = {}
        max_length = 0
        curr_length = 0

        for right in range(len(s)):
            if chars.get(s[right]) is not None and chars.get(s[right]) >= left:
                left = chars[s[right]] + 1
            
            curr_length = right - left + 1
            max_length = max(curr_length, max_length)
            chars[s[right]] = right

        return max_length
        