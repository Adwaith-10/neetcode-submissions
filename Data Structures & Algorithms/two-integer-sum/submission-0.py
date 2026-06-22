class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # dictionary: num -> index
        for i, num in enumerate(nums):
            complement = target - num   # the number we want to find
            if complement in seen:      # have we already seen it?
                return [seen[complement], i]
            seen[num] = i               # store this num for future
        return []