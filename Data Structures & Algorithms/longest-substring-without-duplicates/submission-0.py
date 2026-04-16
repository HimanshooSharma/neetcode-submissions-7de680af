class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window_set = set()

        left_pointer = 0
        result = 0

        for right in range(len(s)):
            while s[right] in window_set:
                window_set.remove(s[left_pointer])
                left_pointer+=1 
            window_set.add(s[right])
            result = max(result, right-left_pointer+1)
        return result

        