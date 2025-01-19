from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ptr: int = 0
        longest_substring: int = 0
        seen = {}

        for i, current in enumerate(s):
            if current in seen and seen[current] >= ptr:
                ptr = seen[current] + 1
            seen[current] = i
            longest_substring = max(longest_substring, i - ptr + 1)

        return longest_substring


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring('abcccbabxc'))