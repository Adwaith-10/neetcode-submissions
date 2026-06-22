
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                # sort enables two-pointers + easy duplicate skipping
        n = len(nums)
        res: List[List[int]] = []

        for i in range(n):
            a = nums[i]

            # (A) stop early: if a > 0, remaining nums are >= a → sums can't reach 0
            if a > 0:
                break

            # (B) skip duplicate first elements
            if i > 0 and a == nums[i - 1]:
                continue

            # (C) two-pointer sweep for pairs summing to -a
            l, r = i + 1, n - 1
            while l < r:
                total = a + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])

                    # (D) skip duplicates on both sides before moving
                    left_val, right_val = nums[l], nums[r]
                    while l < r and nums[l] == left_val:
                        l += 1
                    while l < r and nums[r] == right_val:
                        r -= 1

        return res
