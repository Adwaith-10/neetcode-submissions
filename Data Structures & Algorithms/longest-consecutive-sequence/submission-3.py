from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0

        for x in s:
            if x - 1 not in s:       # only start a streak at the beginning
                curr = x
                length = 1
                while curr + 1 in s: # expand streak
                    curr += 1
                    length += 1
                best = max(best, length)

        return best
