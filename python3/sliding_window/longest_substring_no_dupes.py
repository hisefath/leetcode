class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        max_count = 0
        right_pointer = 0
        for left_pointer in range(len(s)):
            while right_pointer < len(s) and s[right_pointer] not in substring:
                substring.add(s[right_pointer])
                max_count = max(max_count, len(substring))
                right_pointer += 1
            while left_pointer < right_pointer:
                substring.remove(s[left_pointer])

        return max_count
