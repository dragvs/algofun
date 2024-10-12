from typing import List


class Solution:
    """41. First Missing Positive
    See here: https://leetcode.com/problems/first-missing-positive/description/

    Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

    You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

    Solution: Use Cycle sort in-place
    """

    def firstMissingPositive(self, nums: List[int]) -> int:
        # in: [3, 4, -1, 1]
        # out: [1, -1, 3, 4]
        for i in range(len(nums)):
            cur_val = nums[i]
            while 1 <= cur_val <= len(nums) and cur_val != nums[cur_val - 1]:
                nums[cur_val - 1], nums[i] = cur_val, nums[cur_val - 1]
                cur_val = nums[i]
                # 1: [_-1, 4, 3, 1]
                # 2: [-1, _1, 3, 4]
                # 3: [1, _-1, 3, 4]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
