from typing import List


class Solution:
    """448. Find All Numbers Disappeared in an Array
    See here: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

    Given an array nums of n integers where nums[i] is in the range [1, n],
    return an array of all the integers in the range [1, n] that do not appear in nums.
    """

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            val = abs(nums[i])
            pos = val - 1
            if nums[pos] > 0:
                nums[pos] *= -1
        result = [i + 1 for i in range(len(nums)) if nums[i] > 0]
        return result

    def findDisappearedNumbersCycleSort(self, nums: List[int]) -> List[int]:
        i = 0

        while i < len(nums):
            pos = nums[i] - 1
            if nums[i] != nums[pos]:
                nums[pos], nums[i] = nums[i], nums[pos]
            else:
                i += 1
        # print(nums)
        result = [i + 1 for i in range(len(nums)) if nums[i] != i + 1]
        return result
