from typing import List


class Solution:
    """442. Find All Duplicates in an Array
    See here: https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

    Given an integer array nums of length n where all the integers of nums are in the range [1, n]
    and each integer appears once or twice, return an array of all the integers that appears twice.

    You must write an algorithm that runs in O(n) time and uses only constant auxiliary space,
    excluding the space needed to store the output
    """

    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []

        # [2,2,1,3] -> [2]

        for i in range(len(nums)):
            cur_val = abs(nums[i])
            pos = cur_val - 1

            if nums[pos] > 0:
                nums[pos] *= -1
            else:
                duplicates.append(cur_val)
        return duplicates

    def findDuplicatesCycleSort(self, nums: List[int]) -> List[int]:
        # O(N) time and space
        i = 0

        while i < len(nums):
            pos = nums[i] - 1
            if nums[i] != nums[pos]:
                nums[pos], nums[i] = nums[i], nums[pos]
            else:
                i += 1
        # print(nums)
        result = [nums[i] for i in range(len(nums)) if nums[i] != i + 1]
        return result
